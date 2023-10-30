# app.py
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name)

# Create and train a simple ML model
model = RandomForestClassifier()

# Define a simple endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
