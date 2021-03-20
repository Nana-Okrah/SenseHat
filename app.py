from sense_hat import SenseHat
from flask import Flask, render_template, request, current_app as app
import os
import requests


app = Flask(__name__)

@app.route('/message')
def index():
	return render_template('message.html')
	
@app.route('/show_messages',methods =["POST","GET"])
def login():
	if request.method == 'POST':
		user = request.form['name', 'message']
		return redirect(url_for('/show_message', name =user))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

