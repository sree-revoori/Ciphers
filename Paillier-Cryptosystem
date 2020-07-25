#This cipher is the Paillier Cipher, a homomorphic additive cryptosystem. One especially useful application of this cipher is in electronic voting. Some of the downsides of this cipher are that the numbers that you can choose for p and q are very limited. There are many conditions that will prevent the program from working. For this particular program, you can pick any of the following numbers for the two initial primes that the program prompts the user for- 43,47,53,59,61,67,73,79,83,89,97. If given more time, I would have made sure to implement the program so that almost any two prime numbers work. 
from random import randint#Needed to generate random numbers. 
import sys#This is needed to do sys.exit(), so that I can exit the code run-through if there is an error
def mod_inverse(a, m): #This method finds the modular inverse of a mod m. If no inverse exists, it returns an error. 
  for number in range(0, m) : 
    temp = (number * a) % m
    if temp == 1 :
      return number
  print("Error: No possible inverse")
  sys.exit()
def gcd (a, b): #This method finds the greatest common divisor of two numbers using recursion. 
  if (a == 0):
    return b;  
  return gcd(b % a, a); 
def lcm(a, b): #This method finds the lowest common multiple of two numbers using the gcd method. 
  return int(a*b / gcd(a,b)) 
def L(x,n): #This method implements a mathematical function which is necessary to encrypt a number in the Paillier Cipher. 
	return ((x-1)//n)
def inMultGroupsquared(p, q, g): #This method checks if the random integer g is in the multiplicative group of n^2. This is a necessary condition for some aspects of the cryptosystem. 
  n = p*q
  if(gcd(n*n, g)!=1):
    return False
  return True
def inMultGroup(p, q, g): #This method checks if the random integer g is in the multiplicative group of n^2. This is a necessary condition for some aspects of the cryptosystem. 
  n = p*q
  if(gcd(n, g)!=1):
    return False
  return True
def errorChecks(p, q, g): 
  #This method runs through numerous cases of bad values entered by the user. The conditions are as follow: p and q cannot be the same. g must be rel prime to n^2. p and q must be prime. gcd(pq, (p-1)(q-1)) = 1
  n = p*q
  if(p==q):
    print("p and q cannot be the same")
    sys.exit()
  if(gcd(p*q, (p-1)*(q-1)) != 1):
    print("Make sure p and q are two large, prime, and chosen randomly and independently of each other")
    sys.exit()
  if(gcd(g,n*n)!=1):
    print("Make sure g is relatively prime to n^2")
    sys.exit()
def keyGen(p, q, g): #This method generates the public and private key for the Paillier Cipher. The only way to crack this cipher is through knowing the private key. The public key can be given to anyone. 
  n= p*q
  lamb = lcm(p-1, q-1)
  while inMultGroupsquared(p, q, g) == False: #Since the inMultGroup is a function that returns a boolean, I need to check if the condition is not met so that I can generate another random number which meets the condition. Lines 39 and 40 accomplish this task. 
    g = randint(0,100) 
  mu = mod_inverse(L(pow(g, lamb, n*n), n), n) #This is a mathematical formula to calculate the greek symbol mu, which is used in the private key. 
  errorChecks(p, q, g)#This line runs the errorChecks method and makes sure nothing goes wrong and that the user input is correct. 
  print("Public Key(n, g) : " + str(n) + ", " + str(g))
  print("Private Key(lambda, mu) : " + str(lamb) + ", " + str(mu))
  #Lines 43 and 44 convert the integers to strings, format the keys, and prints them out nicely. 
def paillierEncrypt(m, p, q, g):
  n = p*q
  if(m>=n):#This if-statement is another error check to see if the user entered a value of the message that is larger than the product of p and q. If it is, the user must enter larger values for p and q or a smaller value for the message. 
    print("Make sure the number you want to have encrypted is less than than the product of p and q")
    sys.exit()
  if(m<0):#This if-statement makes sure that the user does not enter a negative number because it is not allowed by the cipher. 
    print("Make sure the number you want to have encrypted is a positive number")
    sys.exit()
  r = randint(0, n) #In lines 54-56, I create a random integer, r, which must be between 0 and the value of n, the product of p and q. It must also be in the multiplicative group of n. 
  while inMultGroup(p, q, r) == False:
    r = randint(0, n) 
  m1 = pow(g, m, n*n) #In lines 57 through 60, I calculate the ciphertext using the private key and the encoding formula for the Paillier cryptosystem.
  m2 = pow(r, n, n*n)
  c = (m1 * m2) % (n*n)
  return c
def paillierDecrypt(c, p, q, g):
  n = p*q#In lines 62-64, I recalculate the necessary variables to decrypt the ciphertext. 
  lamb = lcm(p-1, q-1)
  mu = mod_inverse(L(pow(g, lamb, n*n), n), n)
  m = (L(pow(c, lamb, n*n), n) * mu) % n #This line decodes the ciphertext.
  print("Decrypted Value: " +str(m))

#Lines 69 - 75 ask the user for input and run the code. Line 69 creates a global variable, g, which is passed as an argument to almost all of my other methods. Lines 70 and 71 prompt the user to give values for p and q. Line 72 runs the keyGen method with the information collected in the previous lines and generates the public and private key for the Paillier cipher. 73 prompts the user to enter the number that he/she wants to encode. Line 74 prints out the encrypted value while line 75 decrypts that encrypted value to show that the cipher actually works.   
g = randint(0, 100)
p = int(input("Please enter a prime number from the list of numbers provided in a comment at the top: "))
q = int(input("Please enter another prime number from the list of given numbers at the top which is chosen randomly and independently of the first number: "))
keyGen(p, q, g)
m = int(input("Please enter a number which you want to be enciphered using the Paillier cryptosystem: "))
print("Encrypted Value: " + str(paillierEncrypt(m, p, q, g)))
paillierDecrypt(paillierEncrypt(m, p, q, g), p, q, g)




