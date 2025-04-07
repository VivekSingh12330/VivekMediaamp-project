from flask import Flask
import time

app = Flask(__name__)

def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route("/")
def index():
    return "Greetings from VIVEK SINGH!"

@app.route("/compute")
def compute_time():
    start_time = time.time()
    result = generate_fibonacci(10000)
    end_time = time.time()
    duration = end_time - start_time
    return f"Task completed in {duration:.2f} seconds."
