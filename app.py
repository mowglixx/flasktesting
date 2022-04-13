from flask import Flask, redirect, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), primary_key=True)
#     display_name = db.Column(db.String(20), primary_key=True)
#     password = db.Column(db.String(200), primary_key=True)
#     password = db.Column(db.String(200), primary_key=True)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


# def :


@app.route('/')
def index():
    return render_template('home.html', title="Home")


@app.route('/messagehelper/<string:title>')
@app.route('/messagehelper/<string:title>/<string:content>')
def message(
    title='Message Helper', 
    content='On this page you can add your own title by typing in the addressbar after the <code>/title/&ltHere & gt</code>'
    ):
    # decent example of GET use
    return render_template('messagehelper.html', title=title, content=content)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('Magic')
        return redirect('/messagehelper/Logged In/You have successfully logged in.')
    else:
        return render_template('login.html', title="Login")

if __name__ == "__main__":
    app.run(debug=True)
