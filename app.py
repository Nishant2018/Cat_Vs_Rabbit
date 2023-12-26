from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from PIL import Image

app = Flask(__name__,static_folder='static')

# Ensure the 'uploads' directory exists
uploads_dir = os.path.join(app.root_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

# Load the trained model
model = keras.models.load_model("my_model.h5")

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_class(prediction):
    if prediction > 0.5:
        return "Cat"
    else:
        return "Rabbit"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file and allowed_file(file.filename):
        # Save the file in the 'uploads' directory
        filename = secure_filename(file.filename)
        file_path = os.path.join(uploads_dir, filename)
        file.save(file_path)

        # Preprocess the image
        img = image.load_img(file_path, target_size=(256, 256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        prediction = model.predict(img_array)

        # Remove the uploaded file
        os.remove(file_path)

        # Convert prediction to class label
        class_label = predict_class(prediction[0][0])

        return jsonify({"prediction": class_label})

    return jsonify({"error": "Invalid file format"})

if __name__ == '__main__':
    app.run(debug=True)
