from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
import tempfile

app = Flask(__name__)

# Load the logistic regression model
model_filename = 'logistic_regression_model.sav'
model_path = os.path.join(os.path.dirname(__file__), model_filename)

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print(f"Error: Model file '{model_filename}' not found in the specified directory.")
    raise

# Sample machine learning function (replace with your actual model prediction logic)
def predict(input_data):
    # Assuming your input_data is a DataFrame
    features = input_data.values

    # Replace the following line with your actual machine learning model prediction
    prediction_result = model.predict(features)

    return prediction_result


@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = None

    if request.method == 'POST':
        if 'input_file' not in request.files:
            return render_template('index.html', predictions={"Error": "No file uploaded"})

        file = request.files['input_file']

        if file.filename == '':
            return render_template('index.html', predictions={"Error": "No file selected"})

        try:
            # Read CSV file into a DataFrame
            df = pd.read_csv(file)
        except pd.errors.EmptyDataError:
            return render_template('index.html', predictions={"Error": "Empty file"})

        # Perform prediction
        predictions = {"Row " + str(i + 1): "Fraud" if pred == 1 else "Not Fraud" for i, pred in enumerate(predict(df))}

    return render_template('index.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
