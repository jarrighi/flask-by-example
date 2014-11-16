from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
  errors = []
  results = {}
  if request.method == "POST":
    try: 
      url = request.form['url']
      print url[:7]
      if "http://" not in url[:7]:
        url = 'http://' + url
      r = requests.get(url)
      print r.text
    except:
      errors.append(
        "Unable to get URL. Please make sure it's valid and try again."
      )

  return render_template('index.html', errors=errors, results=results)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
  app.run(port=5050)