
# END-TO-END DATA SCIENCE PROJECT - IRIS SPECIES PREDICTION 🌸

**COMPANY:** CODTECH IT SOLUTIONS  
**NAME:** BATHULA SRI HEMANTH NAGA SAI  
**INTERN ID:** CT06DK242  
**DOMAIN:** DATA SCIENCE  
**DURATION:** 6 WEEKS  
**MENTOR:** NEELA SANTOSH  

---

## 🔍 Project Overview

This project is a simple **Flask web application** that predicts the species of an Iris flower using a trained **machine learning model** based on user inputs:  
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

---

## 📁 Project Structure

```

END-TO-END-DATA-SCIENCE-PROJECT/
│
├── app.py                  # Flask app to run the web interface
├── train\_iris\_model.py     # Script to train and save the ML model
├── iris\_model.pkl          # Trained machine learning model
├── iris\_features.pkl       # Feature names for prediction
├── iris\_target\_names.pkl   # Target class labels
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # HTML template for the web UI
│
└── static/                 # (Optional) For CSS, JS, images

````

---

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.7 or above
- pip package manager

### 📦 Installation

```bash
git clone https://github.com/Nagasai-197/END-TO-END-DATA-SCIENCE-PROJECT.git
cd END-TO-END-DATA-SCIENCE-PROJECT
pip install -r requirements.txt
````

---

## 🧠 Model Training

Before running the app, train your ML model:

```bash
python train_iris_model.py
```

This will generate the model and feature/target mapping files.

---

## 🚀 Running the Web App

Start the Flask server:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧪 How to Use

1. Enter the Sepal and Petal measurements (in cm).
2. Click on **Predict**.
3. The app will display the **predicted Iris species**.

---

## 💻 Technologies Used

* Python 3
* Flask
* Scikit-learn
* Jinja2 (HTML templating)
* HTML/CSS

---

## 📸 Output Screenshot

![Image](https://github.com/user-attachments/assets/3d22a34f-317d-4bc0-b389-03e484df2e21)





