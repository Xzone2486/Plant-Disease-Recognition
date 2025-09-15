# import streamlit as st
# import tensorflow as tf
# import numpy as np

# # Tensor flow model prediction 
# def model_prediction(test_image):
#     model = tf.keras.models.load_model('trained_model.h5')
#     image  = tf.keras.preprocessing.image.load_img(test_image, target_size=[128,128])
#     input_arr = tf.keras.preprocessing.image.img_to_array(image)
#     input_arr = np.array([input_arr])
#     prediction = model.predict(input_arr)
#     result_index = np.argmax(prediction)
#     return result_index


# # Sidebar

# st.sidebar.title("Dashboard")
# app_mode = st.sidebar.selectbox("Select Psge",['Home','About','Disease Recognition'])

# # Home Page

# if(app_mode == 'Home'):
#     st.header("Plant Disease Recognition System")
#     image_path = "Plant-diseases-980x380.jpg"
#     st.image(image_path,use_column_width=True)
#     st.markdown("""
# # 🌿 Plant Disease Recognition System 🔍

# Welcome to the **Plant Disease Recognition System**!  
# Our mission is to help farmers, researchers, and gardeners **identify plant diseases quickly and accurately**, ensuring healthier crops and improved harvests.

# ---

# ## 🚀 How It Works
# 1. **Upload an Image**  
#    Go to the **Disease Recognition** page and upload a photo of your plant.  

# 2. **Smart Analysis**  
#    Our AI-powered system analyzes the image using advanced machine learning algorithms.  

# 3. **Get Results**  
#    View detected diseases (if any) along with actionable recommendations.  

# ---

# ## 🌟 Why Choose Us?
# - **High Accuracy** → State-of-the-art ML models for reliable detection.  
# - **User-Friendly** → Clean, intuitive interface for everyone.  
# - **Fast & Efficient** → Get results in just a few seconds.  

# ---

# ## 🏁 Get Started
# 👉 Click on the **Disease Recognition** page in the sidebar, upload an image, and experience the power of AI in plant health monitoring!  

# ---

# ## 👥 About Us
# Learn more about our **team, project goals, and vision** on the **About** page. Together, let’s protect crops and secure a sustainable future. 🌱
# """)
    
# # About Page

# elif(app_mode=='About'):
#     st.header("About")
#     st.markdown("""
# ## 📊 About the Dataset

# This dataset has been **recreated using offline augmentation** from the original dataset.  
# The original dataset can be found on the corresponding [GitHub repository](#).  

# - Contains **~87,000 RGB images** of healthy and diseased crop leaves.  
# - Images are categorized into **38 different classes**.  
# - The dataset is split into an **80/20 ratio** for training and validation, while preserving the original directory structure.  
# - Additionally, a new **test directory** with 33 images was created for prediction purposes.  

# ---

# ## 📂 Dataset Structure

# 1. **Train** → 70,295 images  
# 2. **Validation** → 17,572 images  
# 3. **Test** → 33 images  

# """)

# elif(app_mode== "Disease Recognition"):
#     st.header("Disease Recognition")
#     test_image = st.file_uploader("Choose an Image: ")
#     if(st.button("Show Image")):
#         st.image(test_image,use_column_width=True)
#     #predict button
#     if(st.button("Predict")):
#         st.write("Our Prediction")
#         result_index = model_prediction(test_image)
#         #Define Class
#         class_name = ['Apple___Apple_scab',
#  'Apple___Black_rot',
#  'Apple___Cedar_apple_rust',
#  'Apple___healthy',
#  'Blueberry___healthy',
#  'Cherry_(including_sour)___Powdery_mildew',
#  'Cherry_(including_sour)___healthy',
#  'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
#  'Corn_(maize)___Common_rust_',
#  'Corn_(maize)___Northern_Leaf_Blight',
#  'Corn_(maize)___healthy',
#  'Grape___Black_rot',
#  'Grape___Esca_(Black_Measles)',
#  'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
#  'Grape___healthy',
#  'Orange___Haunglongbing_(Citrus_greening)',
#  'Peach___Bacterial_spot',
#  'Peach___healthy',
#  'Pepper,_bell___Bacterial_spot',
#  'Pepper,_bell___healthy',
#  'Potato___Early_blight',
#  'Potato___Late_blight',
#  'Potato___healthy',
#  'Raspberry___healthy',
#  'Soybean___healthy',
#  'Squash___Powdery_mildew',
#  'Strawberry___Leaf_scorch',
#  'Strawberry___healthy',
#  'Tomato___Bacterial_spot',
#  'Tomato___Early_blight',
#  'Tomato___Late_blight',
#  'Tomato___Leaf_Mold',
#  'Tomato___Septoria_leaf_spot',
#  'Tomato___Spider_mites Two-spotted_spider_mite',
#  'Tomato___Target_Spot',
#  'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
#  'Tomato___Tomato_mosaic_virus',
#  'Tomato___healthy']
#         st.success("Model is Predicting it's a {}".format(class_name[result_index]))



    
#GPT code
import streamlit as st
import tensorflow as tf
import numpy as np

# ✅ Cache the model so it doesn't reload every time
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('trained_model.keras')

model = load_model()

# ✅ Prediction function
def model_prediction(test_image):
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image) / 255.0  # normalize
    input_arr = np.expand_dims(input_arr, axis=0)  # add batch dimension
    prediction = model.predict(input_arr)
    return np.argmax(prediction)

# ✅ Class labels (dict for cleaner mapping)
CLASS_NAMES = {
    0: 'Apple___Apple_scab',
    1: 'Apple___Black_rot',
    2: 'Apple___Cedar_apple_rust',
    3: 'Apple___healthy',
    4: 'Blueberry___healthy',
    5: 'Cherry_(including_sour)___Powdery_mildew',
    6: 'Cherry_(including_sour)___healthy',
    7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    8: 'Corn_(maize)___Common_rust_',
    9: 'Corn_(maize)___Northern_Leaf_Blight',
    10: 'Corn_(maize)___healthy',
    11: 'Grape___Black_rot',
    12: 'Grape___Esca_(Black_Measles)',
    13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    14: 'Grape___healthy',
    15: 'Orange___Haunglongbing_(Citrus_greening)',
    16: 'Peach___Bacterial_spot',
    17: 'Peach___healthy',
    18: 'Pepper,_bell___Bacterial_spot',
    19: 'Pepper,_bell___healthy',
    20: 'Potato___Early_blight',
    21: 'Potato___Late_blight',
    22: 'Potato___healthy',
    23: 'Raspberry___healthy',
    24: 'Soybean___healthy',
    25: 'Squash___Powdery_mildew',
    26: 'Strawberry___Leaf_scorch',
    27: 'Strawberry___healthy',
    28: 'Tomato___Bacterial_spot',
    29: 'Tomato___Early_blight',
    30: 'Tomato___Late_blight',
    31: 'Tomato___Leaf_Mold',
    32: 'Tomato___Septoria_leaf_spot',
    33: 'Tomato___Spider_mites Two-spotted_spider_mite',
    34: 'Tomato___Target_Spot',
    35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    36: 'Tomato___Tomato_mosaic_virus',
    37: 'Tomato___healthy'
}

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ['Home', 'About', 'Disease Recognition'])

# Home Page
if app_mode == 'Home':
    st.header("Plant Disease Recognition System")
    st.image("Plant-diseases-980x380.jpg", use_column_width=True)
    st.markdown("""
# 🌿 Plant Disease Recognition System 🔍

Welcome to the **Plant Disease Recognition System**!  
Our mission is to help farmers, researchers, and gardeners **identify plant diseases quickly and accurately**, ensuring healthier crops and improved harvests.

---

## 🚀 How It Works
1. **Upload an Image**  
   Go to the **Disease Recognition** page and upload a photo of your plant.  

2. **Smart Analysis**  
   Our AI-powered system analyzes the image using advanced machine learning algorithms.  

3. **Get Results**  
   View detected diseases (if any) along with actionable recommendations.  

---

## 🌟 Why Choose Us?
- **High Accuracy** → State-of-the-art ML models for reliable detection.  
- **User-Friendly** → Clean, intuitive interface for everyone.  
- **Fast & Efficient** → Get results in just a few seconds.  

---

## 🏁 Get Started
👉 Click on the **Disease Recognition** page in the sidebar, upload an image, and experience the power of AI in plant health monitoring!  

---

## 👥 About Us
Learn more about our **team, project goals, and vision** on the **About** page. Together, let’s protect crops and secure a sustainable future. 🌱
""")

# About Page
elif app_mode == 'About':
    st.header("About")
    st.markdown(""" 
## 📊 About the Dataset

This dataset has been **recreated using offline augmentation** from the original dataset.  
The original dataset can be found on the corresponding [GitHub repository](#).  

- Contains **~87,000 RGB images** of healthy and diseased crop leaves.  
- Images are categorized into **38 different classes**.  
- The dataset is split into an **80/20 ratio** for training and validation, while preserving the original directory structure.  
- Additionally, a new **test directory** with 33 images was created for prediction purposes.  

---

## 📂 Dataset Structure

1. **Train** → 70,295 images  
2. **Validation** → 17,572 images  
3. **Test** → 33 images  
 """)

# Disease Recognition Page
elif app_mode == "Disease Recognition":
    st.header("🌱 Disease Recognition")
    test_image = st.file_uploader("Upload a plant leaf image:", type=["jpg", "png", "jpeg"])

    if test_image:
        st.image(test_image, use_column_width=True, caption="Uploaded Image")
        
        if st.button("🔍 Predict"):
            with st.spinner("Analyzing image... Please wait"):
                result_index = model_prediction(test_image)
                prediction = CLASS_NAMES[result_index]
                st.success(f"✅ Model Prediction: **{prediction}**")
