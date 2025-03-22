# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "<h1>Welcome to My Website</h1><p>This is the home page.</p>"
# @app.route('/about')
# def about():
#     return "<h1>About Me</h1><p>I love coding!</p>"
# @app.route('/contact')
# def contact():
#     return "<h1>Contact Me</h1><p>My favorite superhero is Spider-Man!</p>"
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title='Home', heading='Welcome to My Website', content='This is the home page.')
@app.route('/about')
def about():
    return render_template('index.html', title='About Me', heading='About Me', content='I love coding!')
@app.route('/contact')
def contact():
    return render_template('index.html', title='Contact Me', heading='Contact Me', content='My favorite superhero is Batman!')
if __name__ == '__main__':
    app.run(debug=True)                                        