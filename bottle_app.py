
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, request

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

	

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <style>
			body{
				background-color : #800000;
				text-align : center;
			}
			select{
				width:50%%;
				text-align : center;
			}
			table{
				
				border : 5 px solid black;
				width : 50%%;
				border-collapse:collapse;
			}
			th{
				height : 50px;
				background-color : #800000;
				color : #FFD700;
			}
			td{
				border:3px solid gold;
			}
			tr:hover{
				background-color : #FFD700;
			}

			.submit{
				width:25%%;
			}
		</style>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page

def index():
	text = """
	
	<form action="/checklist" method="POST">
		<input type="checkbox" name="checklist" value="1">1985</input>
		<input type="checkbox" name="checklist" value="2">1986</input>
		<input type="checkbox" name="checklist" value="3">1987</input>
		<input type="checkbox" name="checklist" value="4">1988</input>
		<input type="checkbox" name="checklist" value="5">1989</input>
		<p>\t</p>
		<input type="checkbox" name="checklist" value="6">1990</input>
		<input type="checkbox" name="checklist" value="7">1991</input>
		<input type="checkbox" name="checklist" value="8">1992</input>
		<input type="checkbox" name="checklist" value="9">1993</input>
		<input type="checkbox" name="checklist" value="10">1994</input>
		<p>\t</p>
		<input type="checkbox" name="checklist" value="11">1995</input>
		<input type="checkbox" name="checklist" value="12">1996</input>
		<input type="checkbox" name="checklist" value="13">1997</input>
		<input type="checkbox" name="checklist" value="14">1998</input>
		<input type="checkbox" name="checklist" value="15">1999</input>
		<p>\t</p>
		<input type="checkbox" name="checklist" value="15">2000</input>
		<input type="checkbox" name="checklist" value="15">2001</input>
		<input type="checkbox" name="checklist" value="15">2002</input>
		<input type="checkbox" name="checklist" value="15">2003</input>
		<input type="checkbox" name="checklist" value="15">2004</input>
		
		<p>\t</p>
		<input type="submit" value="Lets Search!">
	</form><br/>
	<form action="/year" method="POST">
		<select name="year">
			<option value="1">1985-1999</option>
			<option value="2">2000-2014</option>
		</select>
		<input type="submit" value="Lets Search!">
	</form><br/>
	<form action="/trades" method="POST">
		<input type="textbox" name="trade" placeholder="Capitol letters matters"/>
		<input type="submit" value="Lets Search!">
	</form><br/>
	<p>Made by HK</p>
	
	"""
	return htmlify("Foreign Trades by Years",text)

def trades():
	userinput = request.POST["trade"]
	text ="""<table>
			<tr>
				<th></th>
				<th>[----1985----]</th>
				<th>[----1986----]</th>
				<th>[----1987----]</th>
				<th>[----1988----]</th>
				<th>[----1989----]</th>
				<th>[----1990----]</th>
				<th>[----1991----]</th>
				<th>[----1992----]</th>
				<th>[----1993----]</th>
				<th>[----1994----]</th>
				<th>[----1995----]</th>
				<th>[----1996----]</th>
				<th>[----1997----]</th>
				<th>[----1998----]</th>
				<th>[----1999----]</th>
				<th>[----2000----]</th>
				<th>[----2001----]</th>
				<th>[----2002----]</th>
				<th>[----2003----]</th>
				<th>[----2004----]</th>
				<th>[----2005----]</th>
				<th>[----2006----]</th>
				<th>[----2007----]</th>
				<th>[----2008----]</th>
				<th>[----2009----]</th>
				<th>[----2010----]</th>
				<th>[----2011----]</th>
				<th>[----2012----]</th>
				<th>[----2013----]</th>
				<th>[----2014----]</th>
			</tr>\n	
				"""
	for x in contents :
		if userinput in x[0]:
			text += """<tr>
					<td>%(0)s</td>
					<td>%(1)s</td>
					<td>%(2)s</td>
					<td>%(3)s</td>
					<td>%(4)s</td>
					<td>%(5)s</td>
					<td>%(6)s</td>
					<td>%(7)s</td>
					<td>%(8)s</td>
					<td>%(9)s</td>
					<td>%(10)s</td>
					<td>%(11)s</td>
					<td>%(12)s</td>
					<td>%(13)s</td>
					<td>%(14)s</td>
					<td>%(15)s</td>
					<td>%(16)s</td>
					<td>%(17)s</td>
					<td>%(18)s</td>
					<td>%(19)s</td>
					<td>%(20)s</td>
					<td>%(21)s</td>
					<td>%(22)s</td>
					<td>%(23)s</td>
					<td>%(24)s</td>
					<td>%(25)s</td>
					<td>%(26)s</td>
					<td>%(27)s</td>
					<td>%(28)s</td>
					<td>%(29)s</td>
					<td>%(30)s</td>
				</tr>
			""" % { "0":x[0], "1" : x[1],  "2":x[2], "3":x[3], "4":x[4], "5":x[5], "6":x[6] ,"7":x[7] ,"8":x[8] ,"9":x[9] ,"10":x[10] ,"11":x[11] ,"12":x[12] ,"13":x[13] ,"14":x[14] ,"15":x[15] ,"16":x[16] ,"17":x[17] ,"18":x[18] ,"19":x[19] ,"20":x[20] ,"21":x[21] ,"22":x[22] ,"23":x[23] ,"24":x[24] ,"25":x[25] ,"26":x[26] ,"27":x[27] ,"28":x[28] ,"29":x[29] ,"30":x[30] }
	text += "</table>"
	return htmlify("Title", text)

def year():
	userinput = request.POST["year"]
	text = ""
	if userinput == "1":
		text ="""<table>
			
				"""
		for x in contents :
			if x[0] == "TRADE":
				continue
			text += """<tr>
				<td>%(0)s</td>
				<td>%(1)s</td>
				<td>%(2)s</td>
				<td>%(3)s</td>
				<td>%(4)s</td>
				<td>%(5)s</td>
				<td>%(6)s</td>
				<td>%(7)s</td>
				<td>%(8)s</td>
				<td>%(9)s</td>
				<td>%(10)s</td>
				<td>%(11)s</td>
				<td>%(12)s</td>
				<td>%(13)s</td>
				<td>%(14)s</td>
				<td>%(15)s</td>
							</tr>
			""" % {"0":x[0], "1":x[1], "2":x[2], "3":x[3], "4":x[4], "5":x[5], "6":x[6], "7":x[7], "8":x[8], "9":x[9], "10":x[10], "11":x[11], "12":x[12], "13":x[13], "14":x[14], "15":x[15]}		
	else :
		text ="""<table>
		
				"""
		for x in contents :
			if x[0] == "TRADE":
				continue
			text += """<tr>
				<td>%(0)s</td>
				<td>%(16)s</td>
				<td>%(17)s</td>
				<td>%(18)s</td>
				<td>%(19)s</td>
				<td>%(20)s</td>
				<td>%(21)s</td>
				<td>%(22)s</td>
				<td>%(23)s</td>
				<td>%(24)s</td>
				<td>%(25)s</td>
				<td>%(26)s</td>
				<td>%(27)s</td>
				<td>%(28)s</td>
				<td>%(29)s</td>
				<td>%(30)s</td>
							</tr>
			""" % {"0":x[0], "16":x[16],"17":x[17], "18":x[18] ,"19":x[19] ,"20":x[20] ,"21":x[21] ,"22":x[22] ,"23":x[23] ,"24":x[24] ,"25":x[25] ,"26":x[26] ,"27":x[27] ,"28":x[28] ,"29":x[29] ,"30":x[30]}					
	text += "</table>"
	return htmlify("Title", text)

def checklist():
	userinput = request.POST.getall("checklist")
	print(userinput)	
	text = """<table>
				<tr>
					"""
	for hk in userinput:
		print(hk)
		if hk == "1":
			print("1st header added")
			
		if hk == "2":
			print("2nd header added")
			
		if hk == "3":
			print("3rd header added")
			
		if hk == "4":
			print("4th header added")
			
		if hk == "5":
			print("5th header added")
			
		if hk == "6":
			print("6th header added")
			
		if hk == "7":
			print("7th header added")
			
		if hk == "8":
			print("8th header added")
			
		if hk == "9":
			print("9th header added")
			
		if hk == "10":
			print("10th header added")
			
		if hk == "11":
			print("11st header added")
			
		if hk == "12":
			print("12nd header added")
			
		if hk == "13":
			print("13rd header added")
			
		if hk == "14":
			print("14th header added")
			
		if hk == "15":
			print("15th header added")
			
		if hk == "16":
			print("16th header added")
			
		if hk == "17":
			print("17th header added")
			
		if hk == "18":
			print("18th header added")
			
		if hk == "19":
			print("19th header added")
			
		if hk == "20":
			print("20th header added")
			
			print (text)		
	text += """		</tr>\n"""
	for x in contents:
		if x[0] == "TRADE":
				continue
		text += """<tr>
					<td>%s</td>"""	% x[0]
		for hk in userinput :
			if hk =="1":
				text += """
					<td>%(1)s</td>
				""" % { "1":x[1]}
			elif hk =="2":
				text += """
					<td>%(2)s</td>
				""" % {"2":x[2]}
			elif hk =="3":
				text += """
					<td>%(3)s</td>
				""" % {"3":x[3]}
			elif hk =="4":
				text += """
					<td>%(4)s</td>
				""" % {"4":x[4]}
			elif hk =="5":
				text += """
					<td>%(5)s</td>
				""" % {"5":x[5]}
			elif hk =="6":
				text += """
					<td>%(6)s</td>
				""" % {"6":x[6]}
			elif hk =="7":
				text += """
					<td>%(7)s</td>
				""" % {"7":x[7]}
			elif hk =="8":
				text += """
					<td>%(8)s</td>
				""" % {"8":x[8]}
			elif hk =="9":
				text += """
					<td>%(9)s</td>
				""" % {"9":x[9]}
			elif hk =="10":
				text += """
					<td>%(10)s</td>
				""" % {"10":x[10]}
			elif hk =="11":
				text += """
					<td>%(11)s</td>
				""" % {"11":x[11]}
			elif hk =="12":
				text += """
					<td>%(12)s</td>
				""" % {"12":x[12]}
			elif hk =="13":
				text += """
					<td>%(13)s</td>
				""" % {"13":x[13]}
			elif hk =="14":
				text += """
					<td>%(14)s</td>
				""" % {"14":x[14]}
			elif hk =="15":
				text += """
					<td>%(15)s</td>
				""" % {"15":x[15]}
			elif hk =="16":
				text += """
					<td>%(16)s</td>
				""" % {"16":x[16]}
			elif hk =="17":
				text += """
					<td>%(17)s</td>
				""" % {"17":x[17]}
			elif hk =="18":
				text += """
					<td>%(18)s</td>
				""" % {"18":x[18]}
			elif hk =="19":
				text += """
					<td>%(19)s</td>
				""" % {"19":x[19]}
			elif hk =="20":
				text += """
					<td>%(20)s</td>
				""" % {"20":x[20]}
		text += """		</tr>\n"""
	text += """	</table>\n"""						
	return htmlify("Title", text)

route('/', 'GET', index)
route('/trades', 'POST', trades)
route('/year', 'POST', year)
route('/checklist', 'POST', checklist)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

