from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    DevOps Platform Running............🚀
    Version: {os.getenv("APP_VERSION","v1")}
    Environment: {os.getenv("APP_ENV","dev")}
    """

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)