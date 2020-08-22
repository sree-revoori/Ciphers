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

e = 65537 

l = len(alphabet)
largestPower = 0 

while pow(l, largestPower) < mod: 
    largestPower += 1 

largestPower = largestPower - 1

print("Alphabet length is: " + str(l) + " and the highest power is " + str(largestPower))

actualNum = 89897807505048742568624266076183099622868191865791675665199726198073166863517809194896619121285164863721775826174711988683028633449762554684260071137667277939952878337117007006682648484027616481552917086710938427047904293454110730563208669424803871616352517233729085665806037146392445377160226330123954583864

for password in commonPasswordList : 
    for username in usernameList : 
      plaintext = "userid:" + username + ", password:" + password
      #print(plaintext)
      substringList = list()
      if(len(plaintext)%largestPower == 0): 
        numObjects = len(plaintext)/largestPower
      else: 
        numObjects = (len(plaintext)/largestPower) + 1
        numOfZ = largestPower - (len(plaintext)%largestPower)
        count = 0
      while (count < numOfZ) : 
        plaintext = plaintext + "Z"
        count = count + 1
      
      numObjects = int(numObjects)

      for index in range(numObjects) : 
        string = plaintext[:largestPower]
        plaintext = plaintext[largestPower:]
        substringList.append(string)
        
      numList = list()
      for i in range(len(substringList)) : 
        numFinal = 0
        for index in range(largestPower): 
          string = substringList[i]
          string = string[::-1]
          num = c2i(string[index], alphabet)
          temp = pow(l, index) * num 
          numFinal = numFinal + temp
        
      numList.append(numFinal)
        temp = (pow(numFinal, e, mod))
        if temp ==  actualNum: 
          yes = "Mr. Eckel used " + password + " and username " + username
          return yes
  
