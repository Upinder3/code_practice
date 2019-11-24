def max_time(t):
	mt = ""
	if t[0] == "?":
		if t[1] == "?" or t[1] < "4":
			mt += "2"
		else:
			mt += "1"
	else:
		mt += t[0]
	
	
	if t[1] == "?":
		if mt[0] == "2":
			mt += "3"
		else:
			mt += "9"
	else:
		mt += t[1]
	
	mt += ":"
	
	if t[3] == "?":
		mt += "5"
	else:
		mt += t[3]
	
	
	if t[4] == "?":
		mt += "9"
	else:
		mt += t[4]
	
	return mt


t = "??:??"
print(max_time(t))
