from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register

if __name__ == "__main__"":
    sample.run(host="0.0.0.0", port=5000)
