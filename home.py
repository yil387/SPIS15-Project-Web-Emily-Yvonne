import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)


app.secret_key='gpknangaxqppgnk'; 


app.catagories = ['UCSD alumni', 'UCSD places', 'UCSD facts', 'UCSD colleges', 'UCSD events', 'UCSD orgs']

ucsdCats = ['History', 'Student Life', 'Campus Services', 'Colleges', 'People', 'Academics']

focsCats = []

ucsdQs = {100:'Famously originating in 1965 from a physics exam question centering on the velocity on impact of a dropped object',\
          200:'One of the oldest and largest centers for ocean and Earth science research, public service, undergraduate and graduate training in the world',\
          300:'Created in 1999, it is a charter school located on UCSD',\
          400:'Hall\'s interior design contains triangular wood and plaster surfaces that fold around the room in order to diffuse sound throughout the space',\
          500:'University celebrated the opening of this building on 18 May 2008?',\
          101:'Save 10% on every purchase at all UC San Diego Housing and Dining Services locations',\
          201:'March 2nd is the deadline for this program',\
          301:'Rich opportunities for learning, community building, and engagement outside the classroom',\
          401:'This contains a 44,000-square-foot floor space',\
          501:'The only multi-arts presenting program on campus, ArtPower brings nationally and internationally recognized performing artists to campus',\
          102:'Peterson Hall(both ways), Warren Apartements(both ways), and TPCS(counterclockwise)',\
          202:'Free tutoring on campus',\
          302:'UC San Diego\'s database of off-campus jobs, internships, volunteer opportunities, and on-campus jobs (including work-study)',\
          402:'Provides medical care, including urgent care and support services such as laboratory, pharmacy, and x-ray',\
          502:'Offers workshops on violence prevention for the entire UCSD campus and provides free and confidential services for students, staff, and faculty impacted by violence, with a focus on survivors of sexual assault, relationship violence, and stalking',\
          103:'Founded in 1988 as Fifth College',\
          203:'Shortest Writing Sequence',\
          303:'College opened at the height of the American environmentalist movement triggered by Rachel Carson\'s book Silent Spring',\
          403:'Hosts the Chocolate Festival',\
          503:'Created more academic departments and programs than any other college at UCSD, including Third World Studies, Ethnic Studies, Education Studies, African American Studies Minor, and Urban Studies and Planning',\
          104:'Pradeep Khosla',\
          204:'Bianca Ibarra, Viera Kair, and Ivonne Avila',\
          304:'Creator of the GoPro',\
          404:'Author of A Thousand Splendid Suns',\
          504:'Played Elizabeth Cutler on Star Trek: Enterprise',\
          105:'Major with the most number of students at UCSD',\
          205:'Graduate-level business school',\
          305:'List Courses Required and Completed needed for graduation',\
          405:'Drop without a W grade',\
          505:'Design and Analysis of Algorithms'}


focsQs = {100:'C1Q1', 200:'C1Q2', 300:'C1Q3', 400:'C1Q4', 500:'C1Q5',\
          101:'C2Q1', 201:'C2Q2', 301:'C2Q3', 401:'C2Q4', 501:'C2Q5',\
          102:'C3Q1', 202:'C3Q2', 302:'C3Q3', 402:'C3Q4', 502:'C3Q5',\
          103:'C4Q1', 203:'C4Q2', 303:'C4Q3', 403:'C4Q4', 503:'C4Q5',\
          104:'C5Q1', 204:'C5Q2', 304:'C5Q3', 404:'C5Q4', 504:'C5Q5',\
          105:'C6Q1', 205:'C6Q2', 305:'C6Q3', 405:'C6Q4', 505:'C6Q5'}



ucsdAs = {100:'What is the Watermelon drop?',\
          200:'What is the Scripps Institution of Oceanography?',\
	  300:'What is the Preuss School?',\
	  400:'What is the Conrad Prebys Music Center?',\
	  500:'What is Price Center East?',\
          101:'What is Triton Cash?',\
	  201:'What is FAFSA?',\
	  301:'What is the Center for Student Involvement?',\
	  401:'What is RIMAC?',\
	  501:'What is ArtPower?',\
          102:'What are the Campus Loop Shuttles?',\
	  202:'What is OASIS?',\
	  302:'What is Port Trition?',\
	  402:'What is Student Health Services?',\
	  502:'What is Center for Advocacy, Resources, and Education (CARE)?',\
          103:'What is the Eleanor Roosevelt College?',\
	  203:'What is Earl Warren College?',\
	  303:'What is John Muir College?',\
	  403:'What is Sixth College?',\
	  503:'What is Thurgood Marshall College?',\
          104:'Who is the Chancellor of UC San Diego?',\
	  204:'Who are the Computer Science advisors?',\
	  304:'Who is Nicholas D. Woodman?',\
	  404:'Who is Khaled Hosseini?',\
	  504:'Who is Kellie Waymire?',\
          105:'What is Biology?',\
	  205:'What is the Rady School of Management?',\
	  305:'What is the degree audit?',\
	  405:'What is the Week 4 Deadline?',\
	  505:'What is CSE 101?'}


focsAs = {100:'C1A1', 200:'C1A2', 300:'C1A3', 400:'C1A4', 500:'C1A5',\
          101:'C2A1', 201:'C2A2', 301:'C2A3', 401:'C2A4', 501:'C2A5',\
          102:'C3A1', 202:'C3A2', 302:'C3A3', 402:'C3A4', 502:'C3A5',\
          103:'C4A1', 203:'C4A2', 303:'C4A3', 403:'C4A4', 503:'C4A5',\
          104:'C5A1', 204:'C5A2', 304:'C5A3', 404:'C5A4', 504:'C5A5',\
          105:'C6A1', 205:'C6A2', 305:'C6A3', 405:'C6A4', 505:'C6A5'}


@app.route('/')
def homePage():
    return render_template('home.html')

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

@app.route('/Qucsd/<cat>/<dollar>')
def Qucsd(cat, dollar):
    return render_template('Qucsd.html', cat=int(cat), dollar=int(dollar), topics=ucsdCats, Qs=ucsdQs)

@app.route('/Aucsd/<cat>/<dollar>')
def Aucsd(cat, dollar):
    return render_template('Aucsd.html', cat=int(cat), dollar=int(dollar), topics=ucsdCats, As=ucsdAs)


#Foundation of CS Jeopardy
@app.route('/Jfocs')
def Jfocs():
    return render_template('Jfocs.html')

@app.route('/Qfocs/<cat>/<dollar>')
def Qfocs(cat, dollar):
    return render_template('Qfocs.html', cat=int(cat), dollar=int(dollar), topics=focsCats, Qs=focsQs)

@app.route('/Afocs/<cat>/<dollar>')
def Afocs(cat, dollar):
    return render_template('Afocs.html', cat=int(cat), dollar=int(dollar), topics=focsCats, As=focsAs)


#The Third Jeopardy(?)
@app.route('/page5')
def page5():
    return render_template('page5.html')



#Phill's example
@app.route('/practiceBoard')
def practiceBoard():
    return render_template('practiceBoard.html')

@app.route('/answer/<cat>/<dollar>')
def answer(cat, dollar):
    return render_template('answer.html', cat=int(cat), dollar=dollar, topics=app.catagories)


if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")
