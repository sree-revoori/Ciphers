rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
ringPositions = "DEF" 
plugboard = "AT BS DE FM IR KN LZ OW PV XY"

def caesarShift(str, amount):
	output = ""

	for i in range(0,len(str)):
		c = str[i]
		code = ord(c)
		if ((code >= 65) and (code <= 90)):
			c = chr(((code - 65 + amount) % 26) + 65)
		output = output + c
	
	return output

