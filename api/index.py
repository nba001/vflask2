from flask import Flask, render_template
from os.path import dirname, abspath, join
import json
dir = dirname(abspath(__file__))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('Products.html', products=getProducts())


@app.route('/about')
def about():
    return render_template('About Us.html')


@app.route('/contact')
def contact():
    return render_template('Contact Us.html')


@app.route('/contactForm')
def contactForm():
    return render_template('index.html')


@app.route('/test')
def test():
    data = {}
    with open(join(dir, '..', 'data', 'products.json'), 'r') as file:
        data = json.loads(file.read())
    return render_template('Products.html', products=data)
    # return res


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict)


def getProducts():
    data = {}
    with open(join(dir, '..', 'data', 'products.json'), 'r') as file:
        data = json.loads(file.read())
    return data
