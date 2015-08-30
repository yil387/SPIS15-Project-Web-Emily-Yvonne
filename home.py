import os
from flask import Flask, escape, redirect, render_template, request, session, url_for

app = Flask(__name__)

#Trying to use session to remember which links are visited, in progress
app.secret_key='gpknangaxqppgnk'; 


app.catagories = ['UCSD alumni', 'UCSD places', 'UCSD facts', 'UCSD colleges', 'UCSD events', 'UCSD orgs']

ucsdCats = ['History', 'Student Life', 'Campus Services', 'Colleges', 'People', 'Academics']

#I can't think of any catagory for this game
focsCats = []

ucsdQs = {100:'<pre>Famously originating in 1965 from a physics exam question centering on the velocity on impact of a dropped object</pre>',\
          200:'<pre>One of the oldest and largest centers for ocean and Earth science research, public service, undergraduate and graduate training in the world</pre>',\
          300:'<pre>Created in 1999, it is a charter school located on UCSD</pre>',\
          400:'<pre>Hall\'s interior design contains triangular wood and plaster surfaces that fold around the room in order to diffuse sound throughout the space</pre>',\
          500:'<pre>University celebrated the opening of this building on 18 May 2008?</pre>',\
          101:'<pre>Save 10% on every purchase at all UC San Diego Housing and Dining Services locations</pre>',\
          201:'<pre>March 2nd is the deadline for this program</pre>',\
          301:'<pre>Rich opportunities for learning, community building, and engagement outside the classroom</pre>',\
          401:'<pre>This contains a 44,000-square-foot floor space</pre>',\
          501:'<pre>The only multi-arts presenting program on campus, ArtPower brings nationally and internationally recognized performing artists to campus</pre>',\
          102:'<pre>Peterson Hall(both ways), Warren Apartements(both ways), and TPCS(counterclockwise)</pre>',\
          202:'<pre>Free tutoring on campus</pre>',\
          302:'<pre>UC San Diego\'s database of off-campus jobs, internships, volunteer opportunities, and on-campus jobs (including work-study)</pre>',\
          402:'<pre>Provides medical care, including urgent care and support services such as laboratory, pharmacy, and x-ray</pre>',\
          502:'<pre>Offers workshops on violence prevention for the entire UCSD campus and provides free and confidential services for students, staff, and faculty impacted by violence, with a focus on survivors of sexual assault, relationship violence, and stalking</pre>',\
          103:'<pre>Founded in 1988 as Fifth College</pre>',\
          203:'<pre>Shortest Writing Sequence</pre>',\
          303:'<pre>College opened at the height of the American environmentalist movement triggered by Rachel Carson\'s book Silent Spring</pre>',\
          403:'<pre>Hosts the Chocolate Festival</pre>',\
          503:'<pre>Created more academic departments and programs than any other college at UCSD, including Third World Studies, Ethnic Studies, Education Studies, African American Studies Minor, and Urban Studies and Planning</pre>',\
          104:'<pre>Pradeep Khosla</pre>',\
          204:'<pre>Bianca Ibarra, Viera Kair, and Ivonne Avila</pre>',\
          304:'<pre>Creator of the GoPro</pre>',\
          404:'<pre>Author of A Thousand Splendid Suns</pre>',\
          504:'<pre>Played Elizabeth Cutler on Star Trek: Enterprise</pre>',\
          105:'<pre>Major with the most number of students at UCSD</pre>',\
          205:'<pre>Graduate-level business school</pre>',\
          305:'<pre>List Courses Required and Completed needed for graduation</pre>',\
          405:'<pre>Drop without a W grade</pre>',\
          505:'<pre>Design and Analysis of Algorithms</pre>'}


focsQs = {100:'<pre>import turtle<br>turtle.forward (100)<br>turtle.left (120)<br>turtle.forward (200)<br>turtle.left (150)<br>turtle.forward (173)</pre>',\
	  200:'<pre>def myLen(List):<br>   if List == []:<br>      return 0<br>   else:<br>      return 1 + myLen(List[1:])</pre>',\
	  300:'<pre>def doubleIt(a):<br>   """return two times a"""<br>   return _ _ _</pre>',\
	  400:'<pre>Base 2 raised to this number equals 8,192</pre>',\
	  500:'<pre>0001 0010</pre>',\
          101:'<pre>Divide a problem into several subproblems and solve each subproblem recursively.</pre>',\
	  201:'<pre>Origin starts at the upper left-hand corner</pre>',\
	  301:'<pre>def numToBinary(N):<br>   if N == 0:<br>      return N</pre>',\
	  401:'<pre>Name Located in the Centered and is the biggest size in this document</pre>',\
	  501:'<pre>Continously connected, goes from top to bottom, and connects by edge or corner</pre>',\
          102:'<pre>15%4 is an example of this</pre>',\
	  202:'<pre>Take the best step and never look back</pre>',\
	  302:'<pre>Recommended to be efficent, resilent, and flexible</pre>',\
	  402:'<pre>Biggest taboo for a programmer, can be used instead of repeating over and over</pre>',\
	  502:'<pre>Former Google Employee</pre>',\
          103:'<pre>Will be working at UC Santa Barbara this fall?</pre>',\
	  203:'<pre>Former Ph.D student at UC San Diego?</pre>',\
	  303:'<pre>Indentation for this code does not matter, but is recommended</pre>',\
	  403:'<pre>Vim and Emacs</pre>',\
	  503:'<pre>Shows hidden files from A-z \n  HINT: 3 lines to imput in Command Prompt</pre>',\
          104:'<pre>Things that don\'t change</pre>',\
	  204:'<pre>These are examples of two types of code - Hello.java and Hello.class</pre>',\
	  304:'<pre>for x in range( 0, width ):<br>   for y in range( 0, height ):<br>      (red, green, blue) = im.getpixel((x, y))<br>      newRed = 255-red<br>      newGreen = 255-green<br>      newBlue = 255-blue<br>      draw.point([(x, y)], (newRed, newGreen, newBlue))</pre>',\
	  404:'<pre>These are letters used to move in vim</pre>',\
	  504:'<pre>Considers all possibilites when looking for a solution, even if it means going to the previous step.</pre>',\
          105:'<pre>git add file<br>git ____ ______ ________<br>git status<br>git commit</pre>',\
	  205:'<pre>Identity what the function does to the image<br>def function(im):<br>   draw = ImageDraw.Draw(im)<br>   imsize = im.size<br>   width = imsize[0]<br>   height = imsize[1]<br>   for x in range( 0, width ):<br>      for y in range( 0, height ):<br>         (red, green, blue) = im.getpixel((x, y))<br>         newRed = (0.21*red)<br>         newGreen = (0.72*green)<br>         newBlue = (0.7*blue)<br>         gray = (newRed + newGreen + newBlue)<br>         gray = int(gray)<br>         draw.point([(x, y)], (gray, gray, gray))<br>   im.show()</pre>',\
	  305:'<pre>Includes information about you, experiences, and goals</pre>',\
	  405:'<pre>Identify what is happening:<br>for x in range(0, 5):<br>   print "Hello World"</pre>',\
	  505:'<pre>Tests code often and sets a false function to check if its working</pre>'}



ucsdAs = {100:'<pre>What is the Watermelon drop?</pre>',\
          200:'<pre>What is the Scripps Institution of Oceanography?</pre>',\
	  300:'<pre>What is the Preuss School?</pre>',\
	  400:'<pre>What is the Conrad Prebys Music Center?</pre>',\
	  500:'<pre>What is Price Center East?</pre>',\
          101:'<pre>What is Triton Cash?</pre>',\
	  201:'<pre>What is FAFSA?</pre>',\
	  301:'<pre>What is the Center for Student Involvement?</pre>',\
	  401:'<pre>What is RIMAC?</pre>',\
	  501:'<pre>What is ArtPower?</pre>',\
          102:'<pre>What are the Campus Loop Shuttles?</pre>',\
	  202:'<pre>What is OASIS?</pre>',\
	  302:'<pre>What is Port Trition?</pre>',\
	  402:'<pre>What is Student Health Services?</pre>',\
	  502:'<pre>What is Center for Advocacy, Resources, and Education (CARE)?</pre>',\
          103:'<pre>What is the Eleanor Roosevelt College?</pre>',\
	  203:'<pre>What is Earl Warren College?</pre>',\
	  303:'<pre>What is John Muir College?</pre>',\
	  403:'<pre>What is Sixth College?</pre>',\
	  503:'<pre>What is Thurgood Marshall College?</pre>',\
          104:'<pre>Who is the Chancellor of UC San Diego?</pre>',\
	  204:'<pre>Who are the Computer Science advisors?</pre>',\
	  304:'<pre>Who is Nicholas D. Woodman?</pre>',\
	  404:'<pre>Who is Khaled Hosseini?</pre>',\
	  504:'<pre>Who is Kellie Waymire?</pre>',\
          105:'<pre>What is Biology?</pre>',\
	  205:'<pre>What is the Rady School of Management?</pre>',\
	  305:'<pre>What is the degree audit?</pre>',\
	  405:'<pre>What is the Week 4 Deadline?</pre>',\
	  505:'<pre>What is CSE 101?</pre>'}


focsAs = {100:'<pre>What is a RIGHT TRIANGLE?</pre>',\
	  200:'<pre>What is return the Length of My List?</pre>',\
	  300:'<pre>What is a+a?</pre>',\
	  400:'<pre>What is 2^13 (or 13)?</pre>',\
	  500:'<pre>What is 34 in binary?</pre>',\
          101:'<pre>What is Divide and Conquer method?</pre>',\
	  201:'<pre>What is the coordinate system of an image?</pre>',\
	  301:'<pre>What is a base case?</pre>',\
	  401:'<pre>What is a Resume?</pre>',\
	  501:'<pre>What are seams?</pre>',\
          102:'<pre>What is a mod?</pre>',\
	  202:'<pre>What is the Greedy Problem Solution?</pre>',\
	  302:'<pre>What is a better code?</pre>',\
	  402:'<pre>What is a loop?</pre>',\
	  502:'<pre>Who is Neil Rhodes?</pre>',\
          103:'<pre>Who is Phill Conrad?</pre>',\
	  203:'<pre>Who is Diba Mirza?</pre>',\
	  303:'<pre>What is Java?</pre>',\
	  403:'<pre>What are text editors?</pre>',\
	  503:'<pre>What is quota -vs\ndu -sh*\ndu -sh .[A-z]*',\
          104:'<pre>What are invarients?</pre>',\
	  204:'<pre>What is a source code and object code?</pre>',\
	  304:'<pre>What is an invert function?</pre>',\
	  404:'<pre>What are h (left), j (down), k (up), and l (right)?</pre>',\
	  504:'<pre>What is backtracking?</pre>',\
          105:'<pre>What is git push origin master?</pre>',\
	  205:'<pre>What is a grayscale?</pre>',\
	  305:'<pre>What is an elevator pitch?</pre>',\
	  405:'<pre>What is a for loop?</pre>',\
	  505:'<pre>What is test driven development?</pre>'}


@app.route('/')
def homePage():
    return render_template('home.html')

#Trying to use session to remember which links are visited, in progress
#@app.route('/startOver')
#def startOver():
#    session.clear()
#    return redirect(url_for('homePage'))

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




#Phill's example
@app.route('/practiceBoard')
def practiceBoard():
    return render_template('practiceBoard.html')

@app.route('/answer/<cat>/<dollar>')
def answer(cat, dollar):
    return render_template('answer.html', cat=int(cat), dollar=dollar, topics=app.catagories)







#Testing css styling
@app.route('/teststyle')
def teststyle():
    return render_template('styletester.html')

@app.route('/testJstyle')
def testJstyle():
    return render_template('Jstyletester.html')


if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")
