from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, FloatField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    num_bedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired()])
    num_bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    type = SelectField('Type', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only")])

    
