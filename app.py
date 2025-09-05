from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask! 🚀</h1><p>Ceci sera notre future To-Do List.</p>"

if __name__ == "__main__":
    app.run(debug=True)
