from flask import Flask, render_template, redirect, url_for, flash,request
from flask.helpers import send_from_directory
from flask_cors import CORS,cross_origin

app = Flask(__name__,static_url_path='',static_folder='../client/build')
CORS(app)
@app.route('/')
@cross_origin()
def home():
    return send_from_directory(app.static_folder,'index.html')
@app.route('/api')
@cross_origin()
def api():
    return {"members":['goremi','gogo','eromi']}
@app.route('/data',methods=['GET','POST'])
def memebrs():
   if request.method == 'POST':
       data =request.get_json()
       print(data)
       user =data['user']
       return {"message":f"Received{user}"} 
if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000)