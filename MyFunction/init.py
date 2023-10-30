# MyFunction/__init__.py
from flask import Flask
from app import app

func = Flask(__name__)

@func.route("/")
def main(req: func.HttpRequest) -> func.HttpResponse:
   return func.Response(app, mimetype="text/html")

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=80)
