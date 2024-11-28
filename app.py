from flask import Flask, request
import time
import os

app = Flask(__name__)

@app.route("/")
def long_running_request():
    # Simulate a 4-minute delay
    delay = request.args.get("delay", 130)
    print("Request received")
    time.sleep(delay)
    return "Request completed", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)