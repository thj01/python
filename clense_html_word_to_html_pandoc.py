#!/usr/bin/python3

### 	Use pandoc to convert docx to html before using script
###
###	pandoc -f docx -t html <name_of_document.docx> -o <name_of_output.html>
###
###	Changes h4 -> h5; h3 -> h4; h2 -> h3; h1 -> h2
###
###	Removes id, class from tags unless they are in TOC
###	Removes <strong> if it is covering the whole content of a tag - Unless it is in TOC (choice og design until now)
###	Removes pagenumbers from TOC text

import sys

file_name = sys.argv[1]

### Diverse variabler

new_filename_heading = "renset"

h1_changed = 0
h2_changed = 0
h3_changed = 0
h4_changed = 0
h5_changed = 0
keep_bold = 0
p_to_li = 0
id_removed = 0
class_removed = 0
table_head_changed = 0
strong_removed = 0
blockquote_removed = 0
image_fix = 0

TOC_level_1_size = "1.1em"
TOC_level_1_margin_top =".5em"
TOC_level_1_margin_bottom =".2em"
TOC_level_1_color="green"
TOC_level_2_margin_left = "15px"
TOC_level_2_color="blue"

### Navngivning af output filnavn

file_name_out = "{0}_{1}".format(new_filename_heading, file_name)

### indlæsning af dokumenr

file_in = open(file_name, "rt", encoding="utf-8")
file_out = open(file_name_out,"wt", encoding="utf-8")

### Det der gøres for hver linie

for line in file_in:	
	
	if "<h5" in line:
		line = line.replace("<h5","<h6")
		line = line.replace("</h5","</h6")
		h5_changed +=1

	elif "<h4" in line:
		line = line.replace("<h4","<h5")
		line = line.replace("</h4","</h5")
		h4_changed +=1
	
	elif "<h3" in line:
		line = line.replace("<h3","<h4")
		line = line.replace("</h3","</h4")
		h3_changed +=1
		
	elif "<h2" in line:
		line = line.replace("<h2","<h3")
		line = line.replace("</h2","</h3")		
		h2_changed +=1
				
	elif "<h1" in line:
		line = line.replace("<h1","<h2")
		line = line.replace("</h1","</h2")
		
		if "Indholdsfortegnelse" in line:
			keep_bold = 1
			p_to_li = 1
		else:
			keep_bold = 0
			p_to_li = 0
		
		h1_changed +=1

	else:
		
		line = line
				
	### Fjerner fed (<strong>) fra tags overordnede tags
		
	if "<strong>" in line:
		
		if keep_bold == 1:
			line = line
		
		else:
			if "<p" or "<tr" or "<th" or "<h1" or "<h2" or "<h3" or "<h4" or "<h5" or "<h6" in line:
				line = line.replace("<strong>","")
				line = line.replace("</strong>","")
				strong_removed +=1
	
	# Ændre p-elementer til li-elementer i indholdsfortegnelsen.
		
	if p_to_li == 1	:
		
		if "<p>" or "</p>" in line:
			if "<strong>" in line:
				line = line.replace("<p>",'<li style="list-style: none;font-size:{0}; margin-top:{1};margin-bottom:{2}">').format(TOC_level_1_size,TOC_level_1_margin_top,TOC_level_1_margin_bottom)
				line = line.replace("</p>","</li>")
			else:
				line = line.replace("<p>",'<li style="list-style: none;margin-left: {0}">').format(TOC_level_2_margin_left)
				line = line.replace("</p>","</li>")
		if "<a " in line:
			line = line.replace("<a ",'<a style="text-decoration: none;" ')
		
		# Fjerner sidetal i indholdsfortegnelsen
		
		print(line[-14:-10])
		
		while True:
			
			try:
				float(line[-11:-10]).is_integer()
				
				remove_char = 1
											
			except:
				
				remove_char = 0

			if remove_char == 1:
				
				print(line[-10:-11])
				
				line = line[:-11] + line[-10:]
				
			else:
				
				break
				

			
			


	if "<blockquote>" or "</blockquote>" in line:
		line = line.replace("<blockquote>","")
		line = line.replace("</blockquote>","")
		blockquote_removed +=1
			
	### Gør opmærksom på at der er billeder og illustrationer i filen
	
	if "<img" in line:
		image_fix +=1

	### Fjerner id fra tags
	
	if 'id="' in line:
		if "<li" in line:
			line = line
		if 'id="fn' in line:
			line = line
		else:
			start_tag = line.find('id="')
			end_tag = line[start_tag+len('id="'):].find('"')
			line = line.replace(line[start_tag:start_tag+end_tag+len('id="')+1],"")
			id_removed +=1

			
	if 'class="' in line:
		if "<li" in line:
			line = line
		else:
			start_tag = line.find('class="')
			end_tag = line[start_tag+len('class="'):].find('"')
			line = line.replace(line[start_tag:start_tag+end_tag+len('class="')+1],"")
			class_removed +=1

	if "<table>" in line:
		line = line.replace("<table>",'<table align="left" border="0" cellpadding="1" cellspacing="1" style="width:100%;">')
		table_head_changed +=1

	file_out.write(line)

file_out.write("<style>")
a_link = "li a:link {0} color: {1} {2}".format("{",TOC_level_1_color,"}")
file_out.write(a_link)
a_visited = "li a:visited {0}color: {1}{2}".format("{",TOC_level_2_color,"}")
file_out.write(a_visited)
file_out.write("a:hover {margin-left: 1px; margin-bottom: 1px}")
file_out.write("sup { font-size: .6em}")
file_out.write("</style>")
	
file_in.close()
file_out.close()

### Output af resultat

print(""" 

*******************************************************
***                                                 ***  
***    O U T P U T   F R A   P R O G R A M M E T    ***
***                                                 *** 
*******************************************************


filnavn på renset dokument: {7}

Antal tags ændret
<h1> -> <h2>: {0}
<h2> -> <h3>: {1}
<h3> -> <h4>: {2}
<h4> -> <h5>: {3}
<h5> -> <h6>: {4}

Elementer fjernet:
<strong>	: {5}
<blockquote>	: {11}
id 		: {9}
class 		: {10}

Tabelhoveder ændret: {8}



Billeder der skal fixes: {6}                         
""".format(h1_changed,h2_changed,h3_changed,h4_changed,h5_changed,strong_removed,image_fix,file_name_out,table_head_changed,id_removed,class_removed,blockquote_removed))
