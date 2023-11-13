from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('file:///home/devasc/MIDTERM/templates/login.html')

@app.route('/register')
def register():
    return render_template('file:///home/devasc/MIDTERM/templates/registration.html')

if __name__ == '__main__':
    app.run(port=5000)
