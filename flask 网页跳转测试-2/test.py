from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
import time
import json


app = Flask(__name__)

@app.route('/',methods=['GET'])  
def index():  

    return render_template('index.html') 

@app.route('/',methods=['POST']) 
def x():  
	id = request.form['staffid']
	return render_template('x.html', id=id)  

if __name__ == '__main__':
	app.run
