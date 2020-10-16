from flask import (Flask,render_template,abort,request,
                   current_app,url_for)
import os 

dir_now = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg','png','jpeg','.gif'] # allowed extensions
app.config['SECRET_KEY'] = os.urandom(12) # generate secret key
app.config['DIR_UPLOADS'] = os.path.join(dir_now,'img') 
