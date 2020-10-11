from PIL import Image



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
  
def mod_inverse(a, m): 
  for number in range(0, m) : 
    temp = (number * a) % m
    if temp == 1 :
      return number
  print("Error: No possible inverse")
  return -1
  
def determinant(a, b, c, d) : 
  det = (a * d) - (c * b)
  return det

def inverse_matrix(a, b, c, d, mod) : 
  det = determinant(a, b, c, d)
  inverseDet = mod_inverse(det, mod)
  
  if det == 0: 
    print("Matrix isn't invertible")
    return [[-1][-1], [-1][-1]]
  
  temp = [[(d * inverseDet) % mod, (b * -1 * inverseDet) % mod], [(c * -1 * inverseDet) % mod, (a * inverseDet) % mod]]
  return temp
  
def problem_1(imageName, integer) : 
  image = Image.open(imageName)
  length, width = image.size
  
  for i in range(length) : 
    for k in range(width) : 
      temp = image.getpixel((i, k))
      temp = (temp + integer) % 256
      image.putpixel((i, k), temp)
      
  image.save("DISCO.bmp")
  
def problem_2(imageName, matrix) : 
  image = Image.open(imageName)
  length, width = image.size 
  
  for k in range(width) : 
    for i in range(1, length, 2) : 
      a = image.getpixel((i - 1, k))
      b = image.getpixel((i, k))
      tempMat = [[a], [b]]
      temp = matrix_multiply2by1(matrix, tempMat, 256)
      image.putpixel((i - 1, k), temp[0][0])
      image.putpixel((i, k), temp[1][0])
  
  image.save("Problem2.bmp")
  
def problem_3(imageName, matrix) : 
  image = Image.open(imageName)
  length, width = image.size 
  
  inverseMat = inverse_matrix(matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1], 256)
  for k in range(width) : 
    for i in range(1, length, 2) : 
      a = image.getpixel((i - 1, k))
      b = image.getpixel((i, k))
      tempMat = [[a], [b]]
      temp = matrix_multiply2by1(inverseMat, tempMat, 256)
      image.putpixel((i - 1, k), temp[0][0])
      image.putpixel((i, k), temp[1][0])
  
  image.save("Problem3.bmp")
  
def problem_4(imageName, matrix, vectorA, vectorB, mod) : 
  image = Image.open(imageName)
  length, width = image.size
  
  count = 1
  
  for k in range(width) : 
    for i in range(1, length, 2) : 
      a = image.getpixel((i - 1, k))
      b = image.getpixel((i, k))
      tempMat = [[a], [b]]
      
      if (count % 2) != 0 : #use first row
        #print("A: " + str(matrix[0][0] * vectorA))
        #print("B: " + str(matrix[0][1] * vectorB))
        temp = matrix_multiply2by1(matrix, tempMat, mod)
        image.putpixel((i - 1, k), temp[0][0])
        image.putpixel((i, k), temp[1][0])
        
        newA = (matrix[0][0] * vectorA) % mod
        newB = (matrix[0][1] * vectorB) % mod
        newC = matrix[1][0]
        newD = matrix[1][1]
        matrix = [[newA, newB], [newC, newD]]
        #print("first row: " + str(matrix))
        
      else :
        temp = matrix_multiply2by1(matrix, tempMat, mod)
        image.putpixel((i - 1, k), temp[0][0])
        image.putpixel((i, k), temp[1][0])
        
        A = matrix[0][0]
        B = matrix[0][1]
        C = (matrix[1][0] * vectorA) % mod
        D = (matrix[1][1] * vectorB) % mod
        matrix = [[A, B], [C, D]]
        #print("second row: " + str(matrix))
        
      count = count + 1
      
  image.save("Problem4.bmp")
  
def problem_5(imageName, matrix, vectorA, vectorB, mod) : 
  image = Image.open(imageName)
  length, height = image.size
  
  count = 1
  
  #hardcode the first two pixels 
  inverseMat = inverse_matrix(matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1], mod)

  for k in range(height) : 
    for i in range(1, length, 2) : 
      a = image.getpixel((i - 1, k))
      b = image.getpixel((i, k))
      tempMat = [[a], [b]]
      
      if (count % 2) != 0 : #use first row 
        temp = matrix_multiply2by1(inverseMat, tempMat, mod)
        image.putpixel((i - 1, k), temp[0][0])
        image.putpixel((i, k), temp[1][0])

        newA = (matrix[0][0] * vectorA) % mod
        newB = (matrix[0][1] * vectorB) % mod
        newC = matrix[1][0]
        newD = matrix[1][1]
        
        matrix = [[newA, newB], [newC, newD]]
        inverseMat = inverse_matrix(newA, newB, newC, newD, mod)
        
      else: 
        temp = matrix_multiply2by1(inverseMat, tempMat, mod)
        image.putpixel((i - 1, k), temp[0][0])
        image.putpixel((i, k), temp[1][0])

        A = matrix[0][0]
        B = matrix[0][1]
        C = (matrix[1][0] * vectorA) % mod
        D = (matrix[1][1] * vectorB) % mod
        
        matrix = [[A, B], [C, D]]
        inverseMat = inverse_matrix(A, B, C, D, mod)

        
      count = count + 1
      #print(count)
  
  image.save("Problem5.bmp")
def problem_6(imageName, a, b) : 
  image = Image.open(imageName)
  length, height = image.size
  for i in range(length) : 
      for k in range(height) : 
        temp = image.getpixel((i, k))
        temp = ((a*temp) + b) % 256
        image.putpixel((i, k), temp)
      
  image.save("logoencoded.bmp")
def problem_6b(imageName, a, b) : 
  image = Image.open(imageName)
  inverse = mod_inverse(a, 256)
  length, height = image.size
  for i in range(length) : 
      for k in range(height) : 
        temp = image.getpixel((i, k))
        temp = (inverse*(temp - b)) % 256
        image.putpixel((i, k), temp)
      
  image.save("logodecoded.bmp")


      
        
        
  
      
  
problem_1("Disco.bmp", 53)
problem_2("SC.bmp", [[2, 5], [3, 20]])
problem_3("Mystery1.bmp", [[2, 3], [5, 20]])
problem_4("SC.bmp", [[2, 5], [3, 20]], 14, 5, 256)
problem_5("Mystery3.bmp", [[2, 5], [3, 20]], 5, 9, 256)
problem_6("logo1.bmp", 251, 101)
problem_6b("logoencoded.bmp", 251, 101)
