# app.py
from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello MIS604 Class !</h1>"

