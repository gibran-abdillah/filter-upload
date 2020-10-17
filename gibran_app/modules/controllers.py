from gibran_app import *
from gibran_app.form.validation import * 
from werkzeug.utils import secure_filename
import imghdr


def validate_image(gambar):
    header = gambar.read(512)
    gambar.seek(0)
    print(gambar.seek(0))
    if imghdr.what(None,header) != None:
        return True 
    return False
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
            if ext_file in app.config['UPLOAD_EXTENSIONS'] and validate_image(uploaded_file.stream):
                uploaded_file.save(os.path.join(app.config['DIR_UPLOADS'],nama_file))
                flash('Uploaded')
            
            
            else:
               abort(403) # return forbidden if file extensions and image are not allowed
        else:
            flash(form.errors[0])

    return redirect(url_for('index_page'))