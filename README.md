# Phishing Email Detection

A Django-based web application that uses a Random Forest Classifier to detect phishing emails based on email headers and other structural "symbols".

## Features

- **Web Interface**: Easy-to-use UI for inputting email symbols.
- **Machine Learning**: Integration with a pre-trained Random Forest model (`.pickle`).
- **Real-time Prediction**: Immediate feedback on whether an email is likely to be phishing.

## Project Structure

```text
.
├── manage.py
├── requirements.txt
├── static/              # CSS and Images
├── symbol_predict/      # Django app and ML logic
│   ├── water.py         # ML prediction logic
│   ├── RandomForestClassifier_20231121.pickle  # Pre-trained model
│   └── ...
├── templates/           # HTML templates
└── ...
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yao021019/Phishing-Email-Detection.git
   cd Phishing-Email-Detection
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

2. **Open your browser** and go to `http://127.0.0.1:8000/`.

3. **Enter symbols**: Input the symbols extracted from an email (separated by spaces) into the text area and click "send".

## Model Details

The application uses a Random Forest model trained on various email features (symbols) such as `ARC_NA`, `ASN`, `BAYES_SPAM`, etc. The model outputs a probability, which is then used to classify the email.
