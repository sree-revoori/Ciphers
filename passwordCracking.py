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
