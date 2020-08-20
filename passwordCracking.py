import math 
from random import randint 

def c2i(c, alphabet):
    return alphabet.index(c) 

def i2c(i, alphabet):
    return alphabet[i]

def rsa_password_cracking(): 
  alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;:-, !'0123456789"

commonPasswordList = list()
  usernameList = ["meckel", "Meckel", "mEckel", "MEckel","mceckel", "Mceckel", "mCeckel", "mcEckel", "MCeckel", "McEckel", "mCEckel", "MCEckel", "malcolm.eckel", "Malcolm.eckel", "malcolm.Eckel", "Malcolm.Eckel"]

#### open a text file. read it line by line. strip the "\n" off each line then split the line into three strings separated by whitespace. 
file = open("common-passwords.txt", "r")

for line in file.readlines() :
    line = line.strip()
    if line.isalpha() == True and len(line) > 5:
      commonPasswordList.append(line)
file.close()

mod = 90487058565911344860746920532714345107344888706603388689414973118770115868824428038927974148369533060365472446789821522968583861289788613738073758712025234963231865997137994675667715748727317358600691229070201161969867856640249424928418473804035245009947964183514868695116591835621822263433693274598400210107
