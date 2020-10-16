from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField


class FileForm(FlaskForm):
    my_file = FileField('File',_name='gibran_file')
    submit = SubmitField('Upload')

