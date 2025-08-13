from flask import Flask, request, jsonify
import pickle
import os
from flask_cors import CORS
import re
import string

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS for cross-origin requests
CORS(app)

# Define paths to the saved model and vectorizer
# Ensure these files are in the same directory as this app.py file
MODEL_PATH = 'mnb_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

# Initialize model and vectorizer variables
mnb = None
cv = None

def preprocess_text(text):
    """
    Function to preprocess the text. This should be an EXACT match
    of the preprocessing steps used when the model was trained.
    
    Common steps include:
    1. Lowercasing the text.
    2. Removing punctuation.
    3. Removing numbers.
    4. Removing extra whitespace.
    """
    if not isinstance(text, str):
        return ""
        
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove extra spaces and strip leading/trailing whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def load_models():
    """Loads the pre-trained model and vectorizer from disk."""
    global mnb, cv
    try:
        # Construct absolute paths to the model files
        current_dir = os.getcwd()
        model_file_path = os.path.join(current_dir, MODEL_PATH)
        vectorizer_file_path = os.path.join(current_dir, VECTORIZER_PATH)

        if not os.path.exists(model_file_path):
            raise FileNotFoundError(f"Model file not found: {model_file_path}")
        if not os.path.exists(vectorizer_file_path):
            raise FileNotFoundError(f"Vectorizer file not found: {vectorizer_file_path}")
            
        with open(model_file_path, 'rb') as model_file:
            mnb = pickle.load(model_file)
        
        with open(vectorizer_file_path, 'rb') as vectorizer_file:
            cv = pickle.load(vectorizer_file)
        
        print("Models loaded successfully!")
    except Exception as e:
        print(f"Error loading models: {e}")
        mnb = None
        cv = None

@app.route('/predict', methods=['POST'])
def predict_spam():
    """
    API endpoint to classify a message as spam or ham.
    Expects a JSON payload with a 'message' key.
    """
    if not mnb or not cv:
        return jsonify({"error": "Model not loaded. Server is not ready."}), 503

    try:
        data = request.get_json(force=True)
        message = data.get('message')

        if not message:
            return jsonify({"error": "No 'message' key found in the JSON payload. Please send data in the format: {'message': 'your text here'}"}), 400

        # Preprocess the message using the same logic as training
        processed_message = preprocess_text(message)
        print(f"Original message: '{message}'")
        print(f"Preprocessed message: '{processed_message}'")

        # Use the loaded vectorizer to transform the preprocessed message
        message_transformed = cv.transform([processed_message])
        
        # Make the prediction
        prediction = mnb.predict(message_transformed)[0]
        
        # Convert prediction to a human-readable string
        result = "spam" if prediction == 'spam' else "ham"
        
        # Return the prediction as a JSON response
        return jsonify({"prediction": result})

    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Load models when the application starts
    load_models()
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
