from flask import Flask, render_template
app = Flask(__name__)

def insert_style(document):
    with open('style.css') as f:
        style = f.read()
    document = document.replace('<style>', '<style>\n' + style) # insert the style into the html cause serving serparately somehow doesn't work
    return document

def get_file(path):
    with open(path) as f:
        return f.read()

def get_styled_html(path):
    return insert_style(get_file(path))

@app.route('/')
def index():
    return get_styled_html('index.html')

@app.route('/logo.png')
def logo():
    with open('logo.png', 'rb') as f:
        return f.read()

@app.route('/signup.html')
def signup():
    return get_styled_html('signup.html')

if __name__ == '__main__':
    app.run(debug=True)