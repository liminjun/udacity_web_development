def escape_html(s):
	for(i,o) in (("&","&amp;"),
		(">","&gt;"),
		("<","&lt;"),
		('"',"&quot;")):
	    s=s.replace(i,o)
	return s

print escape_html("test")