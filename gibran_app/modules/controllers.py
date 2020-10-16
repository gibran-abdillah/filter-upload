from gibran_app import *
from gibran_app.form.validation import * 
from werkzeug.utils import secure_filename

@app.route('/')
def index_page():
    return render_template('index.html',form=FileForm())

@app.route('/upload',methods=['POST','GET'])

def index_upload():

    uploaded_file = request.files['my_file']
    if request.method == 'POST':
        nama_file = uploaded_file.filename # get filename
        ext_file = nama_file.split('.')[1] # get file extension
        if ext_file in app.config['UPLOAD_EXTENSIONS']: # if file extension in configuration
            uploaded_file.save(os.path.join(app.config['DIR_UPLOADS'],nama_file)) # upload your file ..
        else:
            abort(403) # return forbidden if file extensions is not allowed

    return redirect(url_for('index_page'))