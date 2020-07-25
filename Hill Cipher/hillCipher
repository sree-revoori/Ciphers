def c2i(c, alphabet):
    return alphabet.index(c)  

def i2c(i, alphabet):
    return alphabet[i]

def mod_inverse(a, m): 
  for number in range(0, m) : 
    temp = (number * a) % m
    if temp == 1 :
      return number
  print("Error: No possible inverse")
  return -1
  
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
  
def determinant(a, b, c, d) : 
  det = (a * d) - (c * b)
  return det

def inverse_matrix(a, b, c, d, mod) : 
  det = determinant(a, b, c, d)
  inverseDet = mod_inverse(det, mod)
  
  if det == 0: 
    print("Not Invertible")
    return [[-1][-1], [-1][-1]]
   
  temp = [[(d * inverseDet) % mod, (b * -1 * inverseDet) % mod], [(c * -1 * inverseDet) % mod, (a * inverseDet) % mod]]
  return temp
  
def matrix_multiply2by2(matrix1, matrix2, mod) : 
  multA = ((matrix1[0][0] * matrix2[0][0]) + (matrix1[0][1] * matrix2[1][0])) % mod
  multB = ((matrix1[0][0] * matrix2[0][1]) + (matrix1[0][1] * matrix2[1][1])) % mod
  multC = ((matrix1[1][0] * matrix2[0][0]) + (matrix1[1][1] * matrix2[1][0])) % mod
  multD = ((matrix1[1][0] * matrix2[0][1]) + (matrix1[1][1] * matrix2[1][1])) % mod
  
  multMat = [[multA, multB], [multC, multD]]
  return multMat
  
def matrix_multiply2by1(matrix1, matrix2, mod) : 
  multA = ((matrix1[0][0] * matrix2[0][0]) + (matrix1[0][1] * matrix2[1][0])) % mod
  multB = ((matrix1[1][0] * matrix2[0][0]) + (matrix1[1][1] * matrix2[1][0])) % mod
  
  multMat = [[multA], [multB]]
  return multMat
  
def hill_encode(plaintext, matrix, alphabet, mod) : 
  plaintext = plaintext.upper()
  plaintext = prepare_string(plaintext, alphabet)
  if (len(plaintext) % 2) != 0 : 
    plaintext = plaintext + "Z"
  plainList = list(plaintext)
  cipherText = ""
  
  for index in range(len(plainList)) : 
    if (index % 2) != 0: 
      a = c2i(plainList[index - 1], alphabet)
      b = c2i(plainList[index], alphabet)
      tempMat = [[a], [b]]
      temp = matrix_multiply2by1(matrix, tempMat, mod)
      cipherText += i2c(temp[0][0], alphabet) + i2c(temp[1][0], alphabet)
      
  return cipherText
  
def hill_decode(ciphertext, matrix, alphabet4, mod) : 
  cipherList = list(ciphertext)
  inverseMat = inverse_matrix(matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1], mod)
  plainText = ""
  for index in range(len(cipherList)) : 
    if (index % 2) != 0: 
      a = c2i(cipherList[index - 1], alphabet4)
      b = c2i(cipherList[index], alphabet4)
      tempMat = [[a], [b]]
      temp = matrix_multiply2by1(inverseMat, tempMat, mod)
      plainText += i2c(temp[0][0], alphabet4) + i2c(temp[1][0], alphabet4)
      
  return plainText
  
def problem_3(alphabet) :
  digraphList = list()
  for character in alphabet: 
    for character2 in alphabet: 
      temp = ""
      temp += character + character2
      encode = hill_encode(temp, mat1, alphabet, 26)
      if temp == encode : 
        digraphList.append(temp)
  return digraphList
  
def find_number_inverses(mod) : 
  count = 0
  
  for a in range(mod) : 
    for b in range(mod) : 
      for c in range(mod) : 
        for d in range(mod) : 
          if (determinant(a, b, c, d) % mod) != 0 : 
            count += 1
            
  return count

def determine_encoding_matrix(plainDigraph, cipherDigraph, alphabet, mod) : 
  plainM = [[c2i(plainDigraph[0], alphabet), c2i(plainDigraph[2], alphabet)], [c2i(plainDigraph[1], alphabet), c2i(plainDigraph[3], alphabet)]]
  cipherM = [[c2i(cipherDigraph[0], alphabet), c2i(cipherDigraph[2], alphabet)], [c2i(cipherDigraph[1], alphabet), c2i(cipherDigraph[3], alphabet)]]
  
  inverseM = inverse_matrix(plainM[0][0], plainM[0][1], plainM[1][0], plainM[1][1], mod)
  
  if(-1  in inverseM) : 
    return ["NO"]
  encodingM = matrix_multiply2by2(cipherM, inverseM, mod)
  
  return encodingM
  
 
mat1 = [[7, 6], [4, 13]]
mat2 = [[4, 3], [5, 6]]
mat3 = [[6, 1], [17, 3]]
mat4 = [[27, 13], [5, 14]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet1= "ALPHBETYQWERUIOPJHGN"
alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"
mat6 = determine_encoding_matrix("TYIL", "RHRM", alpha, 59)
print(determine_encoding_matrix("TYIL", "RHRM", alpha, 59))

print(hill_decode("tTtp?cIretbpAw,:YKEvcdsWgsydbpcxqmxlz!jfRlxlUM", mat4, alpha, 59))
print(hill_decode("CnzHbKasnOnbeznbhtmHAcv,Xlnbro?M", mat4, alpha, 59))
print(hill_encode("ALPHABET", mat1, alphabet1, 20))
print(hill_decode("TIUYBURG", mat1, alphabet1, 20))
print(hill_encode("INFINITYWARX", mat3, alphabet, 26))
print(hill_decode("SKCVSCKLURRZWWYBWX", mat3, alphabet, 26))
print(hill_decode("JTMFILIFCKXA", mat3, alphabet, 26))
print(inverse_matrix(4, 3, 5, 6, 26))
print(hill_encode("Lester S. Hill had a brilliant idea for a cipher", mat2, alphabet, 26))
print(hill_decode("MVTHVEQHWAIKZRBIPGQTQBVEODDATWKFSVYR", mat2, alphabet, 26))



mat5 = determine_encoding_matrix("TYIL", "RHRM", alphabet, 26)
print(determine_encoding_matrix("TYIL", "RHRM", alphabet, 26))
print(hill_decode("RMYAAMRHMYRSDPSAMRRCXCBIFBFNMRBYQAFLJSNUAC", mat5, alphabet, 26))
