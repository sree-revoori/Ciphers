from collections import Counter 
#Helper Methods
def c2i(c, alphabet) : 
  return alphabet.index(c) 
  
def i2c(i, alphabet) :
  return alphabet[i]
  
def prepare_string(s, alphabet) :
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
  
  #encoding
  def caesar_shift_encode(plaintext, shift, alphabet) :
  plaintext = plaintext.upper()
  temp = prepare_string(plaintext, alphabet) 
  string = ""
  newChar = ""
  for character in temp : 
    aIndex = c2i(character, alphabet) 
    newIndex = c2i(character, alphabet) + shift 
    if newIndex >= 25 : 
      tempIndex = 25 - aIndex 
      newIndex = shift - tempIndex - 1 
      newChar = i2c(newIndex, alphabet)
    else :
      newChar = i2c(newIndex, alphabet) 
    string += newChar
  return string
  
  # decoding
  def caesar_shift_decode(ciphertext, shift, alphabet) : 
  temp = ciphertext
  string = "" 
  newChar = ""
  for character in temp : 
    newIndex = c2i(character, alphabet) - shift
    newChar = i2c(newIndex, alphabet)
    string += newChar
  return string
  def subst_validate(alpha1, alpha2) : 
  alpha1 = list(alpha1)
  alpha2 = list(alpha2)
  for index in range(len(alpha1)) : 
    for index2 in range(len(alpha2)) : 
      if alpha1[index] == alpha2[index2] :
        break
      
    return False 
  return True 
  # encodes sub cipher using helper method from above
  def substitution_cipher_encode(plaintext, alpha1, alpha2) : 
  temp = prepare_string(plaintext, alpha1)
  subst_validate(alpha1, alpha2)
  ciphertext = ""
  for character in temp : 
    alpha1Index = c2i(character, alpha1)
    shift = alpha1Index
    alpha2Character = i2c(shift, alpha2)
    ciphertext += alpha2Character
  return ciphertext
def substitution_cipher_decode(ciphertext, alpha1, alpha2) : 
  temp = prepare_string(ciphertext, alpha2)
  subst_validate(alpha1, alpha2)
  plaintext = "" 
  for character in temp : 
    alpha2Index = c2i(character, alpha2)
    shift = alpha2Index
    alpha1Character = i2c(shift, alpha1)
    plaintext += alpha1Character
  return plaintext
  #Practically an inverse to the sub cipher encode method
  
    
def make_cipher_alphabet(alphabet, keyword) : 
  keywordList = list(keyword)
  alphbetList = list(alphabet)
  replicate = ""
  cipherAlphabet = ""
  for index in range(len(keywordList)) : 
    if keywordList[index] not in cipherAlphabet : 
      cipherAlphabet += keywordList[index]
  
  for index2 in range(len(alphbetList)) : 
    if alphbetList[index2] not in cipherAlphabet : 
      cipherAlphabet += alphbetList[index2]
      
  return cipherAlphabet
  # This method creates a substitution alphabet to replace the normal english alphabet in the substitution cipher
  def keyword_substitution_cipher_encode(plaintext, keyword, alphabet_source) : 
  plaintext = prepare_string(plaintext.upper(), alphabet_source)
  cipherAlphabet = make_cipher_alphabet(alphabet_source, keyword)
  cipherText = ""
  for character in plaintext : 
    alpha1Index = c2i(character, alphabet_source)
    alpha2Character = i2c(alpha1Index, cipherAlphabet)
    cipherText += alpha2Character
  return cipherText
  
  def keyword_substitution_cipher_decode(ciphertext, keyword, alphabet_source) : 
  # Inverts the encoding method
  cipherAlphabet = make_cipher_alphabet(alphabet_source, keyword)
  #temp = prepare_string(ciphertext, cipherAlphabet)
  plaintext = "" 
  for character in ciphertext : 
    alpha2Index = c2i(character, cipherAlphabet)
    shift = alpha2Index
    alpha1Character = i2c(shift, alphabet_source)
    plaintext += alpha1Character
  return plaintext
  
  def frequent_letters(text, alphabet) : 
    text = prepare_string(text, alphabet)
    c = Counter(text)
    return c.most_common(4)
    
  def frequent_bigraphs(text, alphabet) : 
    bigraphs = []
    for index in range(len(text) - 1) : 
      bigraphs.append(text[index:index + 2])
    c = Counter(bigraphs)
    return c.most_common(4)
   
 def frequent_trigraphs(text, alphabet) : 
  bigraphs = []
  for index in range(len(text) - 1) : 
    bigraphs.append(text[index:index + 3])
  c = Counter(bigraphs)
  return c.most_common(4)
  
  def frequent_double_letters(text, alphabet) :
  double = []
  for index in range(len(text) - 1) : 
    if text[index] == text[index + 1] :
      double.append(text[index] + text[index + 1])
  c = Counter(double)
  return c.most_common(4)
  
  def vigenere_encode(plaintext, key, alphabet) : 
  plaintext = prepare_string(plaintext, alphabet)
  plainList = list(plaintext)
  keyList = list(key)
  alphaList = list(alphabet)
  encodeText = ""
  
  for index in range(len(plainList)) : 
    plainIndex = c2i(plainList[index], alphabet)
    keyIndex = c2i(((keyList[index % len(key)])), alphabet)
    encodeTextIndex = (plainIndex + keyIndex) % (26)
    encodeText += i2c(encodeTextIndex, alphabet)
    
  return encodeText
  
  def vigenere_decode(ciphertext, key, alphabet) : 
  ciphertext = prepare_string(ciphertext, alphabet)
  cipherList = list(ciphertext)
  keyList = list(key)
  alphaList = list(alphabet)
  decodeText = ""
  
  for index in range(len(ciphertext)) : 
    cipherIndex = c2i(cipherList[index], alphabet)
    keyIndex = c2i(((keyList[index % len(key)])), alphabet)
    decodeTextIndex = (cipherIndex - keyIndex) % (26)
    decodeText += i2c(decodeTextIndex, alphabet)
    
  return decodeText
  
  def main1() :  
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  plaintext = "my coffee tastes like covfefe"
  codebet = "QWERTYUIOPLKJHGFDSAZXCVBNM"
  plaintext = plaintext.upper()
  shift = 10
  print("\n---Testing substitution-------")
  ciphertext = substitution_cipher_encode(plaintext, alphabet, codebet)
  recovered_text = substitution_cipher_decode(ciphertext, alphabet, codebet)
  print("Plaintext = %s" % plaintext)
  print("Ciphertext = %s" % ciphertext)
  print("Recovered text = %s" % recovered_text)
  print("\n---Testing Caesar-------")
  ciphertext = caesar_shift_encode(plaintext, shift, alphabet)
  recovered_text = caesar_shift_decode(ciphertext, shift, alphabet)
  print("Plaintext = %s" % plaintext)
  print("Ciphertext = %s" % ciphertext)
  print("Recovered text = %s" % recovered_text)
  
  def main2() : 
  print("\n---Testing Keyword Substitution-------")
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  plaintext = "To be or not to be, that is the question"
  keyword = "SHAKESPEARE"
  print("Cipher alphabet is " + make_cipher_alphabet(alphabet, keyword))
  ciphertext = keyword_substitution_cipher_encode(plaintext, keyword, alphabet)
  recovered_text = keyword_substitution_cipher_decode(ciphertext, keyword, alphabet)
  print("Plaintext = %s" % plaintext)
  print("Ciphertext = %s" % ciphertext)
  print("Recovered text = %s" % recovered_text)
  
  def main3() : 
  print("\n---Testing Keyword Graphs-------")
  text3 = "LTQCXT LRJJ HJRDECD, EZT CDJP SXTFRYTDE EC ZNKT LTTD RASTNHZTY VNF NDYXTV WCZDFCD. ZT VNF NHUBREETY LP N FRDGJT KCET VZTD N LXNKT FTDNECX QXCA ONDFNF XTQBFTY EC PRTJY QXCA SXTFFBXT EC HCDKRHE EZT SXTFRYTDE. ZNY WCZDFCD LTTD HCDKRHETY, EZT FSTNOTX CQ EZT ZCBFT VCBJY ZNKT LTHCAT SXTFRYTDE FRDHT WCZDFCD ZNY DC KRHTSXTFRYTDE. RDHXTYRLJP, RE VNF EZRF FNAT FSTNOTX VZC JTY EZT RASTNHZATDE RD EZT ZCBFT CQ XTSXTFTDENERKTF. EZBF, ZNY EZT FTDNET HCDKRHETY EZT SXTFRYTDE, EZRF VCBJY ZNKT NACBDETY EC N SCJRERHNJ HCBS."
  
  
  text3 = text3.lower()
  print("Problem 3 Original Message : " + text3)

    text3 = text3.replace('n', 'A')
  text3 = text3.replace('e', 'T')
  text3 = text3.replace('z', 'H')
  text3 = text3.replace('t', 'E')
  text3 = text3.replace('k', 'V')
  text3 = text3.replace('c', 'O')
  text3 = text3.replace('v', 'W')
  text3 = text3.replace('f', 'S')
  text3 = text3.replace('d', 'N')
  text3 = text3.replace('x', 'R')
  text3 = text3.replace('l', 'B')
  text3 = text3.replace('q', 'F')
  text3 = text3.replace('y', 'D')
  text3 = text3.replace('w', 'J')
  text3 = text3.replace('s', 'P')
  text3 = text3.replace('o', 'K')
  text3 = text3.replace('b', 'U')
  text3 = text3.replace('r', 'I')
  text3 = text3.replace('j', 'L')
  text3 = text3.replace('h', 'C')
  text3 = text3.replace('p', 'Y')
  text3 = text3.replace('a', 'M')
  text3 = text3.replace('u', 'Q')
  text3 = text3.replace('g', 'G')
  
  print("Problem 3 Decoded Message : " + text3)
  
  # text7 = "ZFNNANWJWYBZLKEHBZTNSKDDGJWYLWSBFNS SJWYFNKBGLKOCNKSJEBDWZFNGKLJKJNQFJP FJBXHBZTNRDKNZFNPDEJWYDRPDEGCNZNWJY FZZFLZTCNBBNBZFNNLKZFSLKONWBLCCKJAN KBPHGBZFNGNLOBLWSRDCSBZFNRJWLCBFDKN JWLWSWDTDSUWDTDSUOWDQBQFLZBYDJWYZDF LGGNWZDLWUTDSUTNBJSNBZFNRDKCDKWKLYB DRYKDQJWYDCSJZFJWODRSNLWEDKJLKZUJNA NWZFJWODRDCSSNLWEDKJLKZUZFNRLZFNKQN WNANKRDHWSJZFJWODRSNLWEDKJLKZU"
  # text7 = text7.lower()
  # print("Problem 7 Original Message: " + text7)
  
  # text7 = text7.replace(' ', '')
  # text7 = text7.replace('z', 'T')
  # text7 = text7.replace('f', 'H')
  # text7 = text7.replace('n', 'E')
  # text7 = text7.replace('l', 'A')
  # text7 = text7.replace('r', 'F')
  # text7 = text7.replace('k', 'R')
  # text7 = text7.replace('u', 'Y')
  # text7 = text7.replace('y', 'G')
  # text7 = text7.replace('j', 'I')
  # text7 = text7.replace('g', 'P')
  # text7 = text7.replace('w', 'N')
  # text7 = text7.replace('a', 'V')
  # text7 = text7.replace('b', 'S')
  # text7 = text7.replace('t', 'B')
  # text7 = text7.replace('c', 'L')
  # text7 = text7.replace('e', 'M')
  # text7 = text7.replace('h', 'U')
  # text7 = text7.replace('d', 'O')
  # text7 = text7.replace('o', 'K')
  # text7 = text7.replace('p', 'C')
  # text7 = text7.replace('s', 'D')
  # text7 = text7.replace('q', 'W')
  # text7 = text7.replace('x', 'J')  

  
  # print("Problem 7 Decoded Message: " + text7)
  
  text1 = "XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI."
  text1 = text1.lower()
  text1 = text1.replace('g', 'I')
  text1 = text1.replace('q', 'S')
  text1 = text1.replace('r', 'T')
  text1 = text1.replace('e', 'A')
  text1 = text1.replace('l', 'N')
  text1 = text1.replace('f', 'H')
  text1 = text1.replace('i', 'K')
  text1 = text1.replace('b', 'E')
  text1 = text1.replace('x', 'Y')
  text1 = text1.replace('p', 'R')
  text1 = text1.replace('c', 'F')
  text1 = text1.replace('w', 'X')
  text1 = text1.replace('k', 'M')
  text1 = text1.replace('n', 'P')
  text1 = text1.replace('j', 'L')
  text1 = text1.replace('o', 'Q')
  text1 = text1.replace('t', 'U')
  text1 = text1.replace('m', 'O')
  print("Problem 1 = %s" % text1)
  
  text2 = "AJM PQMCIY QVJ, XJR HCYBQ TNGG QBCP N OCQ BNMS. NP CQ QRMIP JRQ, C TNI YJ N GJIY VNX VCQBJRQ RPCIY NIX JA QBNQ QBCIY KJPQ-S AMJH JRM RPRNG GNXJRQ NQ NGG."
  text2 = text2.lower()
  text2 = text2.replace('n', 'A')
  text2 = text2.replace('c', 'I')
  text2 = text2.replace('g', 'L')
  text2 = text2.replace('t', 'C')
  text2 = text2.replace('i', 'N')
  text2 = text2.replace('p', 'S')
  text2 = text2.replace('y', 'G')
  text2 = text2.replace('j', 'O')
  text2 = text2.replace('v', 'W')
  text2 = text2.replace('x', 'Y')
  text2 = text2.replace('b', 'H')
  text2 = text2.replace('r', 'U')
  text2 = text2.replace('q', 'T')
  text2 = text2.replace('a', 'F')
  text2 = text2.replace('m', 'R')
  text2 = text2.replace('h', 'M')
  text2 = text2.replace('o', 'B')
  text2 = text2.replace('s', 'D')
  text2 = text2.replace('k', 'P')
  print("Problem 2 = %s" % text2)
  
  def main4() : 
  print("\n---Testing Vigenere Cipher Encode-------")
  plaintext = "SECRETMESSAGE"
  keyword = "WORD"
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print("Plaintext = " + plaintext)
  print("Keyword = " + keyword)
  
  encodedMessage =  vigenere_encode(plaintext, keyword, alphabet)
  print("Encoded Message: " + encodedMessage) 
  
  print("\n---Testing Vigenere Cipher Decode-------")
  ciphertext = "OSTUAHDHOGRJA"
  keyword = "WORD"
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print("Ciphertext = " + ciphertext)
  print("Keyword = " + keyword)
  
  decodedMessage = vigenere_decode(ciphertext, keyword, alphabet)
  print("Decoded Message: " + decodedMessage) 
  
  main4()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   
  
