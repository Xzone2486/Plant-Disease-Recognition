import tensorflow as tf
import numpy as np
from PIL import Image

# --- Global variable to hold the model ---
# This way, we load the model only once.
model = None

# --- CORRECT class names from your Streamlit app ---
# This is a list to directly map the index from argmax.
CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

def load_model_on_startup():
    """
    Loads the trained Keras model from the .keras file.
    This function is called once when the Flask application starts.
    """
    global model
    try:
        # --- Load your trained model in the .keras format ---
        model_path = 'trained_model.keras'
        model = tf.keras.models.load_model(model_path)
        print(f"✅ Model loaded successfully from {model_path}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        # Depending on the application, you might want to exit if the model fails to load
        model = None

def predict_image(image_path):
    """
    Takes an image file path, preprocesses the image,
    and returns the model's prediction.
    """
    if model is None:
        return {"error": "Model is not loaded. Please check server logs."}

    try:
        # 1. Load and preprocess the image
        img = Image.open(image_path).convert('RGB')
        # --- CORRECT image size from your Streamlit app ---
        img = img.resize((128, 128))
        img_array = np.array(img)
        # Normalize the image
        img_array = img_array / 255.0
        # Create a batch (model expects a batch of images)
        img_batch = np.expand_dims(img_array, axis=0)

        # 2. Make a prediction
        prediction = model.predict(img_batch)

        # 3. Decode the prediction
        predicted_class_index = np.argmax(prediction[0])
        predicted_class_name = CLASS_NAMES[predicted_class_index]
        confidence = float(np.max(prediction[0])) * 100 # As a percentage

        # Clean up the class name for better display
        display_name = predicted_class_name.replace('___', ' - ').replace('_', ' ')


        print(f"Prediction: {display_name} with {confidence:.2f}% confidence.")

        # 4. Return the result as a dictionary
        return {
            'class': display_name,
            'confidence': f"{confidence:.2f}"
        }

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return {"error": "Failed to process the image and make a prediction."}

