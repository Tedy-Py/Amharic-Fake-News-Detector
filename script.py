# -*- coding: UTF-8 -*-

#import os
#import numpy as np
import flask
#import pickle
import joblib
from joblib import load
from flask import Flask, render_template, request
import sklearn
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
	_username = request.form.get('username')  # get(attr) returns None if attr is not present
	model = joblib.load("model.joblib")
	_username=[_username]
	result = model.predict(_username)
	if int(result) == 1:
		#username= 'በተደረገው ማጣራት መሰረት ያስገቡት ዜና የተሳሳተ(Fake) ነው'
		return render_template('response.html', username= 'ያስገቡት ዜና አጠራጣሪ ነው! (Fake)')
	else:
		#prediction= 'በተደረገው ማጣራት መሰረት ያስገቡት ዜና ትክክለኛ(Real) ነው'
		return render_template('response.html', username= 'ያስገቡት ዜና ከሞላ ጎደል ተአማኝ ነው!(Real)')
        

if __name__ == '__main__':
	app.run(debug=True)
