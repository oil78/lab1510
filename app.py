import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    version = os.environ.get("APP_VERSION", "v1.0")
    return f"Hello from Cloud Run! Running version: {version}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
