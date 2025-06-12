# END-TO-END-DATA-SCIENCE-PROJECT


**COMPANY:** CODTECH IT SOLUTIONS  
**NAME:** BATHULA SRI HEMANTH NAGA SAI  
**INTERN ID:** CT06DK242  
**DOMAIN:** DATA SCIENCE  
**DURATION:** 6 WEEKS  
**MENTOR:** NEELA SANTOSH  

---
# Iris Species Prediction Web App

This is a simple Flask web application that predicts the species of an Iris flower based on user input features (sepal length, sepal width, petal length, petal width) using a trained machine learning model.

---

## Project Structure

```

task-3/
│
├── app.py                    # Flask application with prediction logic
├── train\_iris\_model.py       # Script to train and save the model
├── iris\_model.pkl            # Saved trained model
├── requirements.txt          # Python dependencies
│
├── templates/                # HTML templates
│   └── index.html            # User-friendly frontend
│
└── static/                   # (Optional) Static assets like CSS/JS/images

````

---

## Getting Started

### Prerequisites

- Python 3.7 or above
- pip (Python package manager)

### Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd task-3
````

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Train the Model

Run the training script to create the model file:

```bash
python train_iris_model.py
```

### Run the Flask Application

Start the Flask server:

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000` to access the app.

---

## Usage

* Enter the sepal length, sepal width, petal length, and petal width (in cm) of an Iris flower.
* Click **Predict**.
* The app will display the predicted Iris species.

---

## Technologies Used

* Python 3
* Flask
* Scikit-learn
* Jinja2 (templating engine)
* HTML/CSS



