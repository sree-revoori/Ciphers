from math import gcd
 
def c2i(c, alphabet):
    return alphabet.index(c) 

def i2c(i, alphabet):
    return alphabet[i]

def prepare_string(s, alphabet):
  temp = s 
  alphaList = list(alphabet)
  sList = list(temp)
  for index in range(len(sList)) : 
    for index2 in range(len(alphaList)) : 
      if temp[index] == alphaList[index2] :
        break
      if index2 + 1 == len(alphaList) :
        sList.remove(temp[index])
    
  final = ''.join(sList)
  return final
  
def mod_inverse(a, m): 
  for number in range(2, m) : 
    temp = number * a 
    while (temp > m) : 
      temp = temp - m
    if (temp == 1) :
      return number
  print("Error: No possible inverse")
  return -1

def affine_encode(plaintext, alphabet, a, b) : 
  #plaintext = prepare_string(plaintext, alphabet)
  m = len(alphabet) 
  cipherText = ''
  for character in plaintext : 
    plainIndex = c2i(character, alphabet)
    temp = a * plainIndex
    temp = (temp + b) % m
    cipherText += i2c(temp, alphabet)
  return cipherText
  
def affine_decode(ciphertext, alphabet, a, b) : 
  m = len(alphabet)
  plainText = ''
  for character in ciphertext : 
    cipherIndex = c2i(character, alphabet)
    inverse = mod_inverse(a, m)
    temp = cipherIndex - b
    temp = (temp * inverse) % m
    plainText += i2c(temp, alphabet)
  return plainText
  
def transformation_table(alphabetSize) : 
  bVal = alphabetSize
  aVal = 0
  for number in range(alphabetSize) : 
    if gcd(number, alphabetSize) == 1 : 
      aVal = aVal + 1
  
  totalTrans = aVal * bVal 
  print("   " + str(alphabetSize) + "                        " + str(aVal) + "                        " + str(bVal) + "                           " + str(totalTrans))
  
def d2i(d, alphabet) : 
  dList = list(d)
  a = c2i(dList[0], alphabet)
  b = c2i(dList[1], alphabet)
  digraphVal = (a * len(alphabet)) + b
  return digraphVal

def i2d(i, alphabet) : 
  alphaLength = len(alphabet)
  alphaList = list(alphabet)
  digraph = ''
  for a in range(len(alphaList)) : 
    for b in range(len(alphaList)) : 
      if ((a * alphaLength) + b) == i :
        digraph = i2c(a, alphabet) + i2c(b, alphabet)
        return digraph

def affine_encode_digraph(plaintext,alphabet, a, b) : 
  encoded=""
  alpha=[]
  if len(plaintext)%2==1:
      plaintext+="X"
  for i in range(0,len(alphabet)*len(alphabet)):
      alpha.append((a*i+b)%(len(alphabet)*len(alphabet)))
  for i in range(int(len(plaintext)/2)):
      num = d2i(plaintext[2*i]+plaintext[2*i+1],alphabet)
      encoded += i2d(alpha[num], alphabet)
  return encoded
  
def affine_decode_digraph(ciphertext, alphabet, a, b) : 
  m = len(alphabet)
  plainText = ''
  if (len(ciphertext) % 2) != 0 : 
    ciphertext = ciphertext + "Z"
    
  for i in range(0, len(ciphertext), 2):
    string = ciphertext[i:i + 2]
    inverse = mod_inverse(a, m *m)
    temp = d2i(string, alphabet) - b
    temp = (temp * inverse) % (m * m)
    plainText += i2d(temp, alphabet)
  return plainText
def test_formula(a,b,ciphertext,plaintext,alphabet):
  for i in range(len(plaintext)):
    if (c2i(plaintext[i],alphabet)*a+b)%len(alphabet)!=c2i(ciphertext[i],alphabet):
      return False
  return True
  
  
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(affine_decode_digraph("nNjd oJzrXndiqn:EMiMrXPTcEbdAkai,omA", alphabet, 137, 241))
  
print(mod_inverse(19, 26))
print(d2i("HI", alpha))
print(i2d(190, alpha))

print(affine_encode_digraph("BOMBOGENESIS", alpha, 375, 114))
print(affine_decode_digraph("PVAIUJKSYRSR", alpha, 343, 31))
print(affine_encode_digraph("THISISANOTHERTESTX", alpha, 81, 119))     

alphabet1 = "CVJQ3GIDX1WEOKM2RTBL0SNAFYZHUP"
print(affine_encode("ANEWALPHABETWITHDIGITS12", alphabet1, 13, 29))
print(affine_decode("U2N1UIR0UANW1TW0CT3TWJZM", alphabet1, 13, 29))
print(mod_inverse(13, 30))
print("Alphabet Size    # of A Values Possible     # of B Values Possible      Total # of Transformations")
for number in range(17576, 17578) :
  transformation_table(number)
alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.?0123456789-*"
plaintext="IPHONE4IS"
ciphertext="U?NVO42UIPN4M4IPIHFBP?NVO4404B3Z1YHUAAUH4P4BI37UPNFOFAAO47!4IUGOFO!MWUA!6WFAUPJAU54OVHVMUA4!40UT41"

for a in range(len(alphabet1)):##FOR CRIB QUESTION
  for b in range(len(alphabet1)):
    if(test_formula(a,b,ciphertext,plaintext,alphabet1)==True):
      print(a,b)
      
for i in range(576):
  for j in range(576):
    if(affine_encode_digraph("EARLYDECISIONX",alpha,i,j)=="RFDYNWCZHDJPIO"):
      print(i,j)
