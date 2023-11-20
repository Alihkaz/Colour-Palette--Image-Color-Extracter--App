#
from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField
from flask_wtf.file import FileField, FileRequired , FileAllowed 


# WTForm for creating a product post
class CreateProductForm(FlaskForm):

    image = FileField( "Image",validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')]) # IMAGE
    submit = SubmitField("Extract Colours")
