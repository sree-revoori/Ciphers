from primefac import *
import math 
from random import randint 
from timeit import default_timer as timer 

#print(factorint(13049725))
#factorList = list(factorint(13049725))
#print(factorList)
#print(factorint(13049723))

def friedman_test(ciphertext, alpha):
    """Calls index_of_coincidence, then returns the predicted value for keyword length from the friedman test
    using that value"""
    ioc = index_of_coincidence(ciphertext, alpha)
    n = float(len(ciphertext))
    return (0.027 * n)/(((n-1)*ioc)+0.0655-(0.0385*n))

def kasiski_test(ciphertext):  #Code partially provided
    """Finds gcd of most common distances between repeated trigraphs
    Recommended strategy: loop through the ciphertext, keeping a list of trigraphs and a list of distances in this way:
    1) When encountering a new trigraph add it to the trigraph list
    2) When encountering a repeat add the distance from current index to first index of that trigraph to the list of distances"""
    # Here, write code to create the array of distances:
    trigraphList = []
    distanceList = []
    for index in range(len(ciphertext) - 1) : 
      currentTrigraph = ciphertext[index:index + 3]
      if currentTrigraph not in trigraphList :
        trigraphList.append(currentTrigraph)
      else : 
        previousIndex = ciphertext.find(currentTrigraph)
        distance = index - previousIndex
        distanceList.append(distance)

def index_of_coincidence(ciphertext, alpha):
   
  cipher_flat = "".join(
  [x.upper() for x in ciphertext.split()
  if x.isalpha() ]
  )

  N = len(cipher_flat)
  freqs = collections.Counter( cipher_flat )
  alphabet = map(chr, range( ord('A'), ord('Z')+1))
  freqsum = 0.0

  for letter in alphabet:
    freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

  IC = freqsum / ( N*(N-1) )
  return IC

def miller_rabin_test(p): 
  if (p % 2) == 0: 
    #print("Number is composite")
    return False 
  #finding d such that p-1 = 2**r * d and d is odd 
  r, d = 0, p - 1 
  while(d%2 == 0) : 
    d = d/2 
    r = r + 1
  
  for index in range(1, 10) : 
    #x *= 2 
    #x %= p 
    x = pow(randint(2, p-1), d, p)
    if (x == p - 1 or x == 1): 
      continue
    for r in range(1, r) : 
      x = (x * x) % p
      if(x == p) : 
        return False 
      if(x == p - 1) : 
        break 
    else : 
      return False 
  return True 
  
  
def isPerfectSquare(num) : 
  temp = math.sqrt(num)
  if (temp.is_integer()) :
     return True
  return False
  
def efficient_factor(num) : 
  keepTrying = True
  x = math.ceil(math.sqrt(num))
  temp = (x * x) - num
  while(isPerfectSquare(temp) == False) : 
    x = x + 1
    temp = (x * x) - num
    
  return (x) - math.sqrt(temp), (x) + math.sqrt(temp)
      
def run_trial(e) : 
  startPrime = timer() 
  randomPrime1 = randint(pow(2, e-1), pow(2, e))
  randomPrime2 = randint(pow(2, e-1), pow(2, e))
  
  while(miller_rabin_test(randomPrime1)) == False : 
    randomPrime1 = randint(pow(2, e-1), pow(2, e))
  while(miller_rabin_test(randomPrime2)) == False : 
    randomPrime2 = randint(pow(2, e-1), pow(2, e))
    
  stopPrime = timer()
  primeDifference = stopPrime - startPrime
  product = randomPrime1 * randomPrime2 
  startFactor = timer()
  factor = efficient_factor(product)
  stopFactor = timer()
  factorDifference = stopFactor - startFactor
  
  print("Between 2 to the " + str(e -1) + "th and 2 to the " + str(e) + "th")
  print("Found primes " + str(randomPrime1) + " and " + str(randomPrime2))
  print("Product: " + str(product))
  print("Factored to " + str(factor))
  print("Finding primes took " + str(primeDifference) + " seconds")
  print("Factoring products took " + str(factorDifference) + " seconds")
  
def run_multiple_trials(e) : 
  primeList = list()
  factorList = list()
  
  for index in range(1, 10) : 
    startPrime = timer() 
    randomPrime1 = randint(pow(2, e-1), pow(2, e))
    randomPrime2 = randint(pow(2, e-1), pow(2, e))
  
    while(miller_rabin_test(randomPrime1)) == False : 
      randomPrime1 = randint(pow(2, e-1), pow(2, e))
    while(miller_rabin_test(randomPrime2)) == False : 
      randomPrime2 = randint(pow(2, e-1), pow(2, e))
    
    stopPrime = timer()
    primeDifference = stopPrime - startPrime
    primeList.append(primeDifference)
    product = randomPrime1 * randomPrime2 
    startFactor = timer()
    factor = efficient_factor(product)
    stopFactor = timer()
    factorDifference = stopFactor - startFactor
    factorList.append(factorDifference)
    
  primeDiffAverage = 0
  for index in range(len(primeList)) : 
    primeDiffAverage += primeList[index]
  primeDiffAverage = primeDiffAverage/10 
  
  factorDiffAverage = 0
  for index2 in range(len(factorList)) : 
    factorDiffAverage += factorList[index2]
  factorDiffAverage = factorDiffAverage/10
  
  print("Average time to find two primes: " + str(primeDiffAverage))
  print("Average time to factor product: " + str(factorDiffAverage))
  
def run_trial_new(e) : 
  startPrime = timer() 
  #randomPrime1 = randint(pow(2, e-1), pow(2, e))
  #randomPrime2 = randint(pow(2, e-1), pow(2, e))
  
  y1 = randint(2**(e-1), 2**e)
  x1 = nextprime(y1)
  
  y2 = randint(2**(e-1), 2**e)
  x2 = nextprime(y2)

  stopPrime = timer()
  primeDifference = stopPrime - startPrime
  
  product = x1 * x2 
  
  startFactor = timer()
  factor = factorint(product)
  stopFactor = timer()
  factorDifference = stopFactor - startFactor
  
  print("Between 2 to the " + str(e -1) + "th and 2 to the " + str(e) + "th")
  print("Found primes " + str(x1) + " and " + str(x2))
  print("Product: " + str(product))
  print("Factored to " + str(factor))
  print("Finding primes took " + str(primeDifference) + " seconds")
  print("Factoring products took " + str(factorDifference) + " seconds")
  
def run_multiple_trials_new(e) :
  primeList = list()
  factorList = list()
  
  for index in range(1, 10) : 
    startPrime = timer() 
    y1 = randint(2**(e-1), 2**e)
    x1 = nextprime(y1)
  
    y2 = randint(2**(e-1), 2**e)
    x2 = nextprime(y2)
    stopPrime = timer()
    primeDifference = stopPrime - startPrime
    primeList.append(primeDifference)
    
    product = x1 * x2 
    
    startFactor = timer()
    factor = factorint(product)
    stopFactor = timer()
    factorDifference = stopFactor - startFactor
    factorList.append(factorDifference)
    
  primeDiffAverage = 0
  for index in range(len(primeList)) : 
    primeDiffAverage += primeList[index]
  primeDiffAverage = primeDiffAverage/10 
  
  factorDiffAverage = 0
  for index2 in range(len(factorList)) : 
    factorDiffAverage += factorList[index2]
  factorDiffAverage = factorDiffAverage/10
  
  print("Average time to find two primes: " + str(primeDiffAverage))
  print("Average time to factor product: " + str(factorDiffAverage))
  


print(efficient_factor(30))
#print(miller_rabin_test(45))
#print(run_trial(37))
#print(run_multiple_trials(39))
#print(run_trial_new(39))
#print(run_multiple_trials_new(57))
