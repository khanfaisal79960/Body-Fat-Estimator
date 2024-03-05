from flask import Flask, render_template, url_for, request
import joblib

model = joblib.load('./Model/Fat_Estimator.joblib')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Density = float(request.form['Density'])
        Age = float(request.form['Age'])
        Weight = float(request.form['Weight'])
        Height = float(request.form['Height'])
        Neck = float(request.form['Neck'])
        Chest = float(request.form['Chest'])
        Abdomen = float(request.form['Abdomen'])
        Hip = float(request.form['Hip'])
        Thigh = float(request.form['Thigh'])
        Knee = float(request.form['Knee'])
        Ankle = float(request.form['Ankle'])
        Biceps = float(request.form['Biceps'])
        Forearm = float(request.form['Forearm'])
        Wrist = float(request.form['Wrist'])
        x_test = [[Density, Age, Weight, Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist]]
        prediction = model.predict(x_test)
        prediction = f'{prediction[0]:.2f}'
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')