# 🌱 Plant Disease Recognition  

A deep learning-based web application that detects plant diseases from leaf images using **Flask** and **TensorFlow/Keras**.  
This project helps farmers and researchers quickly identify crop health issues and take preventive measures.  

---

## 📂 Project Structure  

```
.
├── app/                     # Flask application package
├── static/                  # Static files (CSS, JS, images)
├── templates/               # HTML templates for Flask
├── .devcontainer/           # Dev container setup
├── .streamlit/              # Old Streamlit config (before migration)
├── .ipynb_checkpoints/      # Jupyter notebook checkpoints
├── app.py                   # Flask entry point
├── main.py                  # Initial script (training/inference base)
├── model.py                 # Model loading and prediction logic
├── requirements.txt         # Project dependencies
├── Train_Plant_Disease.ipynb # Model training notebook
├── Test_plant_disease.ipynb  # Model testing notebook
├── trained_model.h5          # Trained model file
├── trained_model.keras       # Alternative saved model
├── training_hist.JSON        # Training history
├── Plant-diseases-980x380.jpg # Project image/banner
└── .gitignore               # Git ignore file
```

---

## 🚀 Features  

- Upload plant leaf images to detect diseases  
- Uses deep learning model (TensorFlow/Keras)  
- Flask-based web interface (migrated from Streamlit)  
- Visualization of training/testing process (via notebooks)  
- Pre-trained model available (`trained_model.h5`)

---

## 📚 Dataset Used  

The model was trained on the **[New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)** by *vipoooool* on Kaggle.  

- 📸 Contains **~87,000 RGB images** of healthy and diseased crop leaves  
- 🌿 Covers **38 different classes** (healthy + multiple disease types)  
- 🧪 Used for training and testing the deep learning model in this project  

---

## ⚙️ Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/plant-disease-recognition.git
   cd plant-disease-recognition
   ```

---



2. **Create virtual environment** (recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage  

1. **Run the Flask app**  
   ```bash
   python app.py
   ```

2. Open your browser at **http://127.0.0.1:5000/**  

3. Upload a plant leaf image → Get instant prediction  

---

## 📊 Model Information  

- Framework: **TensorFlow/Keras**  
- Model files:  
  - `trained_model.h5`  
  - `trained_model.keras`  
- Training/Testing notebooks:  
  - `Train_Plant_Disease.ipynb`  
  - `Test_plant_disease.ipynb`  

---

## 🛠️ Tech Stack  

- **Frontend:** HTML, CSS (Flask templates, static files)  
- **Backend:** Flask (Python)  
- **Machine Learning:** TensorFlow / Keras  
- **Deployment:** (Add if you plan: e.g., Heroku, Render, AWS)  

---

## 📌 Future Improvements  

- Add more plant species & diseases  
- Deploy on cloud (Heroku/Render/AWS)  
- Improve model accuracy with larger dataset  
- Add multilingual support for farmers  

---

## 🤝 Contributing  

Pull requests are welcome! For major changes, please open an issue first to discuss.  

---

## 📜 License  

This project is licensed under the **MIT License** – feel free to use and modify.  
