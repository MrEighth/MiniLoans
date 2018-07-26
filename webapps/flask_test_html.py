
from flask import Flask, render_template
from datetime import timedelta
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/<name>')
def about(name):
    return render_template("{}.html".format(name))

if __name__ == "__main__":
    app.jinja_env.auto_reload = True 
    app.run(host="0.0.0.0", port=1994, debug=True);