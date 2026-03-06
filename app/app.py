from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")
    env = os.getenv("APP_ENV", "dev")
    return render_template("index.html", version=version, env=env)

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)