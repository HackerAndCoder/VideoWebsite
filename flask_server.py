from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as f:
        index = f.read()
    with open('style.css') as f:
        style = f.read()
    index = index.replace('<style>', '<style>\n' + style) # insert the style into the html cause serving serparately somehow doesn't work
    return index

@app.route('/style.css')
def style():
    with open('style.css') as f:
        style = f.read()
    return style

@app.route('/logo.png')
def logo():
    with open('logo.png', 'rb') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)