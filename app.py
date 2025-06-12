from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('iris_model.pkl')
features = joblib.load('iris_features.pkl')
target_names = joblib.load('iris_target_names.pkl')

@app.route('/')
def home():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [float(request.form[feature]) for feature in features]
    except ValueError:
        return render_template('index.html', features=features, error="Please enter valid numbers")

    data = np.array([inputs])
    pred = model.predict(data)[0]
    species = target_names[pred]

    # <-- CHANGE THIS LINE: pass zip=zip to template
    return render_template('index.html', features=features, prediction=species, inputs=inputs, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)
