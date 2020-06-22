from flask import Flask,render_template
import json
app = Flask(__name__)
local_server=True
with open('config.json','r', encoding='utf8') as c:
    params=json.load(c)["params"]   
@app.route("/")
def home():
   return render_template('home.html',params=params)

app.run(debug=True)   