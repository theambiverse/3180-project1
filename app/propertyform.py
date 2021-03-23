from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class Propertyform(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    bedroom = StringField('No. of Rooms', validators=[InputRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    select = SelectField('Property Type', choices=['House', 'Apartment'] )
    desc=TextAreaField('Description', validators=[InputRequired()])
    photo=FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])