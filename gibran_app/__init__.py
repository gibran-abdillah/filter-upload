from flask import (Flask,render_template,abort,request,
                   current_app,url_for,redirect,flash,send_from_directory)
import os 


dir_now = os.path.dirname(os.path.abspath(__file__)) # dir this file 
app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.jpg','png','jpeg','.gif'] # allowed extensions
app.config['SECRET_KEY'] = os.urandom(12) # generate secret key
app.config['DIR_UPLOADS'] = os.path.join(dir_now,'img') 


list_file = os.listdir(app.config['DIR_UPLOADS'])