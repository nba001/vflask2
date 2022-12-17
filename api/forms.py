from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField, SubmitField, validators, DecimalField


class ContactForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(
        "Name is required"), validators.Length(min=3, max=25)])
    email = EmailField(
        "Email", [validators.DataRequired("Email is required"), validators.Length(min=6, max=40)])
    phone = DecimalField("Phone", [validators.Optional()])
    message = TextAreaField(
        "Message", [validators.DataRequired("Message is required")])
    submit = SubmitField("Send")
