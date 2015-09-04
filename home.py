import os
from flask import Flask, escape, redirect, render_template, request, session, url_for
import json

from data import *

app = Flask(__name__)


app.secret_key='gpknangaxqppgnk'; 


@app.route('/')
def homePage():
    session.clear()
    return render_template('home.html')


@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('SampleJs'))

@app.route('/SampleJs')
def SampleJs():
    return render_template('SampleJs.html')

@app.route('/YourJ')
def YourJ():
    return render_template('YourJ.html')



#UCSD Jeopardy
@app.route('/Jucsd')
def Jucsd():
    return render_template('Jucsd.html')

@app.route('/Qucsd/<cat>/<dollar>',methods=['GET','POST'])
def Qucsd(cat, dollar):
    session[(int(cat)+int(dollar))]='usedQ'
    return render_template('Qucsd.html', cat=int(cat), dollar=int(dollar), topics=ucsdCats, Qs=ucsdQs)

@app.route('/Aucsd/<cat>/<dollar>')
def Aucsd(cat, dollar):
    return render_template('Aucsd.html', cat=int(cat), dollar=int(dollar), topics=ucsdCats, As=ucsdAs)

@app.route('/instruction')
def instruction():
    return render_template('instruction.html')




#Foundation of CS Jeopardy 222222222222222
@app.route('/Qfocs.json/<cat>/<dollar>',methods=['GET','POST'])
def QfocsJSON(cat, dollar):
    index = int(cat) + int(dollar);
    # session[index]='usedQ'
    valueDict = { "question": focsQs[index], "answer" : focsAs[index] }
    return json.dumps(valueDict)

@app.route('/Jfocs2')
def Jfocs2():
    return render_template('Jfocs2.html')




if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")
