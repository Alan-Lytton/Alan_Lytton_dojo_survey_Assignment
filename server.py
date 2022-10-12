from crypt import methods
from operator import methodcaller
from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "dojo!09Form-jk981-vn"  # Change the secret key so each assignment is unique.

@app.route('/')
def display_form():
    return render_template('index.html')

@app.route('/results')
def display_results():
    return render_template('results.html')

@app.route('/results/process', methods=['POST'])
def process_results():
    session['f_name'] = request.form['f_name']
    session['l_name'] = request.form['l_name']
    session['age'] = request.form['user_age']
    session['location'] = request.form['location']
    session['language'] = request.form['fav_lang']
    session['comments'] = request.form['user_comments']
    return redirect('/results')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform