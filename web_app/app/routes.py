from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/', methods = ['GET', 'POST'])
def get_recommendations():
    
    return 'Hello World'
