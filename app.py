# app.py
from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the input value from the form
            input_value = float(request.form['input_value'])

            # Sample data
            X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
            y = np.array([2, 4, 5, 4, 5])

            # Create a linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predict using the input value
            prediction = model.predict(np.array([[input_value]]))

            return render_template('result.html', input_value=input_value, prediction=prediction[0])

        except Exception as e:
            return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)

