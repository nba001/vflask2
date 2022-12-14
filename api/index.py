from flask import Flask, render_template
import productsList

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('Products.html', products=productsList.products)


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
    return 'Test'


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict)
