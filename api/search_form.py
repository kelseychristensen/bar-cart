from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    ingredients = TextAreaField("What's in your bar? (Separate items by comma.)", validators=[DataRequired()])
    submit = SubmitField("Submit")
