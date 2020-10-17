from gibran_app import *
from gibran_app.form.validation import * 
from werkzeug.utils import secure_filename
import imghdr


def validate_image(gambar):
    idk = imghdr.what(None,gambar.read())
    if idk != None:
        return True 
    return idk
@app.route('/')
def index_page():
    return render_template('index.html',form=FileForm())

@app.route('/upload',methods=['POST','GET'])

def index_upload():
    form = FileForm()
    uploaded_file = request.files['my_file']
    if request.method == 'POST':
        if form.validate_on_submit():
            nama_file = uploaded_file.filename # get filename
            ext_file = nama_file.split('.')[1] # get file extension
            
            if ext_file in app.config['UPLOAD_EXTENSIONS'] and validate_image(uploaded_file.stream): # if file extension in configuration
                uploaded_file.save(os.path.join(app.config['DIR_UPLOADS'],nama_file))
                flash('File Uploaded')
            
            else:
                abort(403) # return forbidden if file extensions and image are not allowed

    return redirect(url_for('index_page'))