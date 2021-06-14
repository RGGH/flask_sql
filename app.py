from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return "hello"

@app.route('/jobs', methods=["GET", "POST"])
def jobs():
    return render_template('jobs.html', jobs=db.get_all_jobs())

if __name__ == "__main__":
    app.run(debug=True)