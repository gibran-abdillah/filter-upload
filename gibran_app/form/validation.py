from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField,validators


class FileForm(FlaskForm):
    my_file = FileField('File',[validators.DataRequired('Select a file')])

    submit = SubmitField('Upload')

