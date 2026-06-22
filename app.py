from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 My First Docker Deployment!</h1><p>Built by Umar</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
