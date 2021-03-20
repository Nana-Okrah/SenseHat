from flask import Flask, render_template, request, current_app as app
from sense_hat import SenseHat
import os
import requests
import datetime
sense =SenseHat()
#color = text_colour[255,165,0] #orange

time = datetime.datetime.now()
app = Flask(__name__)

@app.route('/message')
def index():
	return render_template('message.html')
	
@app.route('/success', methods=['GET','POST'])
def success():
   message = request.form['message']
   name = request.form['name']
   sense.show_message(name +":" + message)
   return render_template('sended_messages.html', name = name, message = message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

