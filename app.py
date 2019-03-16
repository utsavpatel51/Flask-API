'''
How to use as api
URL: http://localhost:5000/register
Content-Type:application/json
Raw-Body: 
		{
			"username":"kira",
			"password":"kira"
		}
'''
from flask import Flask, url_for, render_template, request, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
#create app
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
bcrypt =Bcrypt(app)

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('register.html')

@app.route('/register/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		password=''
		try:
			username=request.json['username'].strip()
			if request.json['password'].strip():
				password=bcrypt.generate_password_hash(request.json['password'].strip())
		except:
			username=request.form['username'].strip()
			if request.form['password'].strip():
				password=bcrypt.generate_password_hash(request.form['password'].strip())
		try:
			if username and  password:
				new_user = User(username=username, password=password)
				db.session.add(new_user)
				db.session.commit()
				return '<h1>Data send successfully</h1>'
			return '<h1>username or password required</h1>,403'
		except IntegrityError:
			db.session.rollback()
			return '<h1>User already exists</h1>'
	return render_template('register.html')


if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.run(host='127.0.0.1')