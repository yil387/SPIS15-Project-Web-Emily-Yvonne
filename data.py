ucsdCats = ['History', 'Student Life', 'Campus Services', 'Colleges', 'People', 'Academics']

#I can't think of any catagory for this game
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
          102:'Peterson Hall(both ways), Warren Apartments(both ways), and TPCS(counterclockwise)',\
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


focsQs = {100:'import turtle<br>turtle.forward (100)<br>turtle.left (120)<br>turtle.forward (200)<br>turtle.left (150)<br>turtle.forward (173)',\
	  200:'<pre>def myLen(List):<br>   if List == []:<br>      return 0<br>   else:<br>      return 1 + myLen(List[1:])</pre>',\
	  300:'<pre>def doubleIt(a):<br>   """return two times a"""<br>   return _ _ _</pre>',\
	  400:'Base 2 raised to this number equals 8,192',\
	  500:'0001 0010',\
          101:'Divide a problem into several subproblems and solve each subproblem recursively.',\
	  201:'Origin starts at the upper left-hand corner',\
	  301:'<pre>def numToBinary(N):<br>   if N == 0:<br>      return N</pre>',\
	  401:'Name Located in the Centered and is the biggest size in this document',\
	  501:'Continuously connected, goes from top to bottom, and connects by edge or corner',\
          102:'15%4 is an example of this',\
	  202:'Take the best step and never look back',\
	  302:'Recommended to be efficient, resilient, and flexible',\
	  402:'Biggest taboo for a programmer, can be used instead of repeating over and over',\
	  502:'Former Google Employee',\
          103:'Will be working at UC Santa Barbara this fall?',\
	  203:'Former Ph.D student at UC San Diego?',\
	  303:'Indentation for this code does not matter, but is recommended',\
	  403:'Vim and Emacs',\
	  503:'Shows hidden files from A-z <br>  HINT: 3 lines to input in Command Prompt',\
          104:'Things that don\'t change',\
	  204:'These are examples of two types of code - Hello.java and Hello.class',\
	  304:'<pre>for x in range( 0, width ):<br>   for y in range( 0, height ):<br>      (red, green, blue) = im.getpixel((x, y))<br>      newRed = 255-red<br>      newGreen = 255-green<br>      newBlue = 255-blue<br>      draw.point([(x, y)], (newRed, newGreen, newBlue))</pre>',\
	  404:'These are letters used to move in vim',\
	  504:'Considers all possibilities when looking for a solution, even if it means going to the previous step.',\
          105:'git add file<br>git ____ ______ ________<br>git status<br>git commit',\
	  205:'<pre>Identity what the function does to the image<br>def function(im):<br>   draw = ImageDraw.Draw(im)<br>   imsize = im.size<br>   width = imsize[0]<br>   height = imsize[1]<br>   for x in range( 0, width ):<br>      for y in range( 0, height ):<br>         (red, green, blue) = im.getpixel((x, y))<br>         newRed = (0.21*red)<br>         newGreen = (0.72*green)<br>         newBlue = (0.7*blue)<br>         gray = (newRed + newGreen + newBlue)<br>         gray = int(gray)<br>         draw.point([(x, y)], (gray, gray, gray))<br>   im.show()</pre>',\
	  305:'Includes information about you, experiences, and goals',\
	  405:'<pre>Identify what is happening:<br>for x in range(0, 5):<br>   print "Hello World"</pre>',\
	  505:'Tests code often and sets a false function to check if its working'}



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


focsAs = {100:'What is a RIGHT TRIANGLE?',\
	  200:'What is return the Length of My List?',\
	  300:'What is a+a?',\
	  400:'What is 2^13 (or 13)?',\
	  500:'What is 34 in binary?',\
          101:'What is Divide and Conquer method?',\
	  201:'What is the coordinate system of an image?',\
	  301:'What is a base case?',\
	  401:'What is a Resume?',\
	  501:'What are seams?',\
          102:'What is a mod?',\
	  202:'What is the Greedy Problem Solution?',\
	  302:'What is a better code?',\
	  402:'What is a loop?',\
	  502:'Who is Neil Rhodes?',\
          103:'Who is Phill Conrad?',\
	  203:'Who is Diba Mirza?',\
	  303:'What is Java?',\
	  403:'What are text editors?',\
	  503:'What is quota -vs<br>du -sh*<br>du -sh .[A-z]*',\
          104:'What are invariants?',\
	  204:'What is a source code and object code?',\
	  304:'What is an invert function?',\
	  404:'What are h (left), j (down), k (up), and l (right)?',\
	  504:'What is backtracking?',\
          105:'What is git push origin master?',\
	  205:'What is a grayscale?',\
	  305:'What is an elevator pitch?',\
	  405:'What is a for loop?',\
	  505:'What is test driven development?'}


