from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import Menu, Registration, AESK,SK_Update, Password_Altered
from app.algorithms.old import *

@app.route('/', methods = ['GET', 'POST'])
@app.route('/old', methods = ['GET', 'POST'])
def old():
    form = Menu()
    
    if form.validate_on_submit():
        choice = form.menu.data
        return redirect(url_for(choice, algo = 'proposed'))

    return render_template('menu.html', form = form)

@app.route('/proposed', methods = ['GET', 'POST'])
def proposed():
    form = Menu()

    if form.validate_on_submit():
        choice = form.menu.data
        return redirect(url_for(choice, algo = 'proposed'))
        
    return render_template('menu.html', form = form)

@app.route('/stats', methods = ['GET', 'POST'])
def stats():
    form = Menu()
    return render_template('menu.html', form = form)


@app.route('/registration/<algo>', methods = ['GET', 'POST'])
def registration(algo):
    form = Registration()

    if form.validate_on_submit():
        return redirect(url_for('stats'))

    return render_template('registration.html', form = form)


@app.route('/aesk/<algo>', methods = ['GET', 'POST'])
def aesk(algo):
    form = AESK()

    if form.validate_on_submit():
        return redirect(url_for('stats'))

    return render_template('aesk.html', form = form)


@app.route('/sk/<algo>', methods = ['GET', 'POST'])
def sk_update(algo):
    form = SK_Update()

    if form.validate_on_submit():
        return redirect(url_for('stats'))

    return render_template('sk_update.html', form = form)


@app.route('/password/<algo>', methods = ['GET', 'POST'])
def password_altered(algo):
    form = Password_Altered()

    if form.validate_on_submit():
        return redirect(url_for('stats'))

    return render_template('password_altered.html', form = form)
