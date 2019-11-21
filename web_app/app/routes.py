from flask import render_template, flash, redirect, url_for, flash
from app import app
from app.forms import Menu, Registration, AESK,SK_Update, Password_Altered
from app.algorithms.old.user import MobileUser as MobileUserOld
from app.algorithms.old.home_agent import HomeAgent as HomeAgentOld
from app.algorithms.old.foreign_agent import ForeignAgent as ForeignAgentOld
from app.algorithms.proposed.user import MobileUser as MobileUserProposed
from app.algorithms.proposed.home_agent import HomeAgent as HomeAgentProposed
from app.algorithms.proposed.foreign_agent import ForeignAgent as ForeignAgentProposed


mu_old = MobileUserOld()
ha_old = HomeAgentOld()
fa_old = ForeignAgentOld()
mu_proposed = MobileUserProposed()
ha_proposed = HomeAgentProposed()
fa_proposed = ForeignAgentProposed()
time_taken = {'old': {'registration': 0, 'aesk': 0, 'sk_update': 0, 'password_altered': 0},
            'proposed': {'registration': 0, 'aesk': 0, 'sk_update': 0, 'password_altered': 0}}

@app.route('/', methods = ['GET', 'POST'])
@app.route('/old', methods = ['GET', 'POST'])
def old():
    form = Menu()
    if form.validate_on_submit():
        choice = form.menu.data
        return redirect(url_for(choice, algo = 'old'))

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
    
    return render_template('stats.html', time_taken = time_taken)


@app.route('/registration/<algo>', methods = ['GET', 'POST'])
def registration(algo):
    form = Registration()

    if form.validate_on_submit():
        if algo == 'old':
            mobile_user = mu_old
            home_agent = ha_old
            foreign_agent = fa_old
        else:
            mobile_user = mu_proposed
            home_agent = ha_proposed
            foreign_agent = fa_proposed
            foreign_agent.agent_registration(home_agent)

        IDmu = form.IDmu.data
        PWmu = form.PWmu.data
        s = form.s.data
        status, time = mobile_user.registration(IDmu, PWmu, s, home_agent, foreign_agent)
        if status == 0:
            flash('Registration Successful')
            time_taken[algo]['registration'] = time
        else:
            flash('error')

        return redirect(url_for(algo))

    return render_template('registration.html', form = form)


@app.route('/aesk/<algo>', methods = ['GET', 'POST'])
def aesk(algo):
    form = AESK()

    if form.validate_on_submit():
        if algo == 'old':
            mobile_user = mu_old
            home_agent = ha_old
            foreign_agent = fa_old
        else:
            mobile_user = mu_proposed
            home_agent = ha_proposed
            foreign_agent = fa_proposed

        PW1mu = form.PW1mu.data
        snew = form.snew.data
        Nm = form.Nm.data
        Nf = form.Nf.data
        Nf2 = form.Nf2.data
        if(mobile_user.PWmu != PW1mu):
            flash ('Incorrect Password')
            return redirect('/aesk/{}'.format(algo))
        status, time = mobile_user.aesk(PW1mu, snew, Nm, Nf, Nf2, home_agent, foreign_agent)
        if status == 0:
            flash('AESK Successful')
            time_taken[algo]['aesk'] = time
        else:
            flash('error')

        return redirect(url_for(algo))

    return render_template('aesk.html', form = form)


@app.route('/sk/<algo>', methods = ['GET', 'POST'])
def sk_update(algo):
    form = SK_Update()

    if form.validate_on_submit():
        if algo == 'old':
            mobile_user = mu_old
            home_agent = ha_old
            foreign_agent = fa_old
        else:
            mobile_user = mu_proposed
            home_agent = ha_proposed
            foreign_agent = fa_proposed

        Nstarm = form.Nstarm.data
        Nstarf = form.Nstarf.data
        Kmf = form.Kmf.data
        status, time = mobile_user.session_key_update(Nstarm, Nstarf, Kmf, home_agent, foreign_agent)
        if status == 0:
            flash('SK Update Successful')
            time_taken[algo]['sk_update'] = time
        else:
            flash('error')

        return redirect(url_for(algo))

    return render_template('sk_update.html', form = form)


@app.route('/password/<algo>', methods = ['GET', 'POST'])
def password_altered(algo):
    form = Password_Altered()

    if form.validate_on_submit():
        if algo == 'old':
            mobile_user = mu_old
            home_agent = ha_old
            foreign_agent = fa_old
        else:
            mobile_user = mu_proposed
            home_agent = ha_proposed
            foreign_agent = fa_proposed

        IDmu = form.IDmu.data
        PWmu = form.PWmu.data
        PWmu_new = form.PWmu_new.data
        status, time = mobile_user.password_altered(IDmu, PWmu, PWmu_new, home_agent, foreign_agent)
        if status == 0:
            flash('Password Alter Successful')
            time_taken[algo]['password_altered'] = time
        else:
            flash('error')

        return redirect(url_for(algo))

    return render_template('password_altered.html', form = form)
