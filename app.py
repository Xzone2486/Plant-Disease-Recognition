import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from model import load_model, predict_image # <-- 1. Import your model functions

app = Flask(__name__)

# --- Load the model when the app starts ---
load_model() # <-- 2. Call the load_model function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading.'}), 400

    if file:
        filename = secure_filename(file.filename)
        # Save the file to a temporary location
        # NOTE: For production, a more robust solution might be needed.
        temp_dir = 'temp_uploads'
        os.makedirs(temp_dir, exist_ok=True)
        filepath = os.path.join(temp_dir, filename)
        file.save(filepath)

        # --- 3. Call the prediction function ---
        prediction_result = predict_image(filepath)

        # Optional: Clean up the saved file after prediction
        os.remove(filepath)

        # --- 4. Return the model's prediction ---
        if "error" in prediction_result:
             return jsonify(prediction_result), 500
        else:
             return jsonify(prediction_result)

    return jsonify({'error': 'An unknown error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)