# 💳 Credit Card Fraud Detection & Anomaly Detection System
Welcome to the Credit Card Fraud Detection & Anomaly Detection System. This project aims to detect fraudulent transactions using various machine learning algorithms and provide an intuitive web-based UI for user interaction. The project utilizes HTML and CSS for the front-end UI, Flask for the back-end API, and multiple machine learning models such as SVM, Logistic Regression, and KMeans to perform fraud detection and anomaly detection tasks.

## 📋 Project Overview
This project helps identify suspicious or fraudulent transactions in credit card usage. By employing several machine learning techniques, the system provides a high level of accuracy in detecting anomalies in transaction patterns. Users can interact with the system via a clean, intuitive web interface that allows for both data input and fraud detection results display.

## 🎯 Key Features
Multiple Machine Learning Algorithms: The system utilizes a variety of ML models to enhance accuracy:
- Support Vector Machine (SVM)
- Logistic Regression
- KMeans Clustering (for unsupervised anomaly detection)
- Random Forest (optional)
- Web-based UI: The front-end interface is built using HTML and CSS, providing a simple yet effective way to interact with the detection system.
- Flask API: The back-end is powered by Flask, which handles data processing and integrates the machine learning models with the UI.
- Real-time Detection: Users can input transaction data, and the system will immediately classify the transaction as 'Fraudulent' or 'Legitimate'.
- Visualization: The system can display graphical results of the anomaly detection process, showing patterns of suspicious transactions.
## 🚀 How to Run

### Prerequisites
- Python 3.x
- Flask
- Machine Learning libraries (scikit-learn, pandas, numpy, etc.)
- 
### Steps to Set Up the Project

#### Clone the Repository
Clone the project from GitHub:

```bash
git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
```
```bash
cd Credit-Card-Fraud-Detection
```
#### Create and Activate Virtual Environment
Set up a virtual environment and install the necessary libraries:

```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
#### Install Dependencies
Install all required Python libraries:

```bash
pip install -r requirements.txt
```
#### Run the Flask App
Start the Flask server:

```bash
python app.py
```
#### Access the Web UI
Open your browser and go to http://127.0.0.1:5000 to interact with the fraud detection system.

## 📊 Algorithms Used
- Support Vector Machine (SVM): A supervised learning algorithm used for classification that separates fraudulent and non-fraudulent transactions using hyperplanes.

- Logistic Regression: Another supervised learning algorithm, effective for binary classification problems, which predicts whether a transaction is fraudulent or legitimate.

- KMeans Clustering: An unsupervised learning algorithm used for anomaly detection, grouping transactions based on similarities and flagging unusual patterns.

- Random Forest: A powerful ensemble learning method that can be integrated for improved classification accuracy.

## 🛠 Tech Stack
#### Frontend:
- HTML
- CSS
#### Backend:
- Python
- Flask
#### Machine Learning Libraries:
- scikit-learn
- pandas
- numpy

## 🖥️ Usage
- Transaction Data Input: Users can input transaction details like amount, transaction time, and other relevant data through the web UI.

- Fraud Detection: Once the data is submitted, the system applies the machine learning algorithms to detect whether the transaction is fraudulent or not.

- Anomaly Detection: In addition to classification, KMeans clustering provides insights into outliers or anomalies in the dataset.

- Results Display: The system displays the prediction results (fraudulent or legitimate) on the web page and provides visualizations if needed.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

## 📄 License
This project is licensed under the MIT License.

