from flask import Flask, redirect, render_template, url_for, session, send_from_directory, make_response, request
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


###############################
########## APP INIT ###########
###############################
def create_app():
    return app
