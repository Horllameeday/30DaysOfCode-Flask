from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/<name>')
def index(name="Instinct"):
    name = name
    return render_template('index.html', name=name)