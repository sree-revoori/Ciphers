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


