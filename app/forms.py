from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    num_bedrooms = PasswordField('Password', validators=[InputRequired()])

    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only")])

    
