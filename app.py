from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is Pratyksh Gupta's Flask App"

if __name__ == "__main__":
    # Get the port from environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Ensure we're binding to 0.0.0.0 to accept external connections
    app.run(host="0.0.0.0", port=port)