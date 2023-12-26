# Flask Image Classification

This is a simple Flask web application for image classification using a pre-trained deep learning model. The application allows users to upload images, and the model predicts whether the image contains a "Cat" or a "Rabbit."

## Project Structure

- **app.py:** The main Flask application file that contains routes and logic for handling image uploads and predictions.

- **static/:** The directory for static files, including CSS and image files.

- **uploads/:** The directory where uploaded images are temporarily stored.

- **templates/:** HTML templates used for rendering pages, including `index.html` for the main page.

- **my_model.h5:** The pre-trained deep learning model for image classification.

## Prerequisites

Make sure you have the required Python packages installed. You can install them using the following command:

```bash
pip install -r requirements.txt

## Running the Application
1. Clone the repository to your local machine:
   git clone https://github.com/your-username/your-repository.git
2. Navigate to the project directory:
   cd your-repository
3. Run the Flask application:
   python app.py

   The application will run on http://127.0.0.1:5000/ by default.
4. Open your web browser and go to the provided URL.

5. Upload an image using the provided interface and receive real-time predictions.

Contributing

Feel free to contribute to the development of this project by submitting pull requests or reporting issues.

License

This project is licensed under the MIT License.
