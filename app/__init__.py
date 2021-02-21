from flask import Flask, redirect, render_template, url_for, session, send_from_directory, make_response, request, Response
import threading
import os
import time

###############################
######### SETTINGS ############
###############################

# App Settings #
app = Flask(__name__)


###############################
######### APP ROUTES ##########
###############################

@app.route('/')
def dashboard():
    with app.app_context():
        return render_template('index.html')


@app.route('/create_site', methods=['GET', 'POST'])
def create_site():
    if request.method == 'GET':
        return render_template('creation_form.html')
    elif request.method == 'POST':
        company = request.form['company']
        address = request.form['address']
        phone_number = request.form['phone_number']
        hours = request.form['hours']
        # color = request.form['color']
        if not company or not address or not phone_number or not hours:
            return redirect(url_for('create_site'))
        return render_template('website_template.html', company=company, address=address, phone_number=phone_number,
                               hours=hours)


###############################
########## APP INIT ###########
###############################
def create_app():
    return app
