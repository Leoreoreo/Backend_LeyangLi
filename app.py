# $ export PYTHONPATH=$PYTHONPATH:/Users/liyueyang/Desktop/

from flask import Flask, jsonify
from flask.helpers import send_from_directory
from flask_cors import CORS
from flask import render_template
from database import Database
app = Flask(__name__, static_folder='', static_url_path='')
CORS(app, resources=r'/*')

#-----------------  Define template filter  -----------------
def datetime_format(value, format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

app.add_template_filter(datetime_format, "dformat")
    # call by "mytime|dformat" in HTML
#-----------------  Define URLS -----------------------------
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/home/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    db = Database()
    db.cur.execute("SELECT * FROM resume")
    resume = db.cur.fetchall()
    db.close_connection()
    return jsonify(resume)

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    #app.run()
    app.run(host="0,0,0,0", port=5000)