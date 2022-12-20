from flask import Flask, render_template, request
from os.path import dirname, abspath, join
from flask_mail import Mail, Message
import json
import os
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField, SubmitField, validators, DecimalField


dir = dirname(abspath(__file__))

app = Flask(__name__)

app.secret_key = os.environ['secret_key']
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
Mail_Sender = os.environ['Mail_Sender']
Mail_Recipient = os.environ['Mail_Recipient']

app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('Products.html', products=getProducts())


@app.route('/about')
def about():
    return render_template('About Us.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('Contact Us.html', form=form)
        else:
            print("Form Data : " + form.email.data + " | " + form.name.data +
                  " | " + str(form.phone.data) + " | " + form.message.data)
            msg = Message(form.name.data + " submitted the Contact Form", sender=Mail_Sender,
                          recipients=[Mail_Recipient])
            msg.body = """
            From: %s <%s>
            Phone : %s
            %s
            """ % (form.name.data, form.email.data, str(form.phone.data), form.message.data)
            mail.send(msg)
            return render_template('Contact Us.html', success=True)
    elif request.method == 'GET':
        return render_template('Contact Us.html', form=form)
    return render_template('Contact Us.html', form=form)


@app.route('/test2')
def test():
    return Mail_Recipient
    # return res


def getProducts():
    data = {}
    with open(join(dir, '..', 'data', 'products.json'), 'r') as file:
        data = json.loads(file.read())
    return data


class ContactForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(
        "Name is required"), validators.Length(min=3, max=25)])
    email = EmailField(
        "Email", [validators.DataRequired("Email is required"), validators.Length(min=6, max=40)])
    phone = DecimalField("Phone", [validators.Optional()])
    message = TextAreaField(
        "Message", [validators.DataRequired("Message is required")])
    submit = SubmitField("Send")
