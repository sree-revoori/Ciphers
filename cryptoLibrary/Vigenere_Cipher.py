import collections
from math import gcd
from collections import Counter

def c2i(c, alphabet):
    """Returns the index of c in the string alphabet, starting at 0"""
    return alphabet.find(c)
    # Copy your method from subcipher.py here

def i2c(i, alphabet):
    """Returns the character at index i in alphabet"""
    return alphabet[i]
    # Copy your method from subcipher.py here

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    for x in s:
      if(alphabet.find(x)==-1):
        s = s.replace(x, "")
    # Copy your method from subcipher.py here
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("".join(key)) 

def vigenere_encode(plaintext, key, alphabet):
  keyword = generateKey(plaintext, key)
  cipher_text = [] 
  for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(keyword[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
  return("".join(cipher_text))

def vigenere_decode(ciphertext, key, alphabet):
  keyword = generateKey(ciphertext, key)
  orig_text = [] 
  for i in range(len(ciphertext)): 
        x = (ord(ciphertext[i]) - 
             ord(keyword[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
  return("".join(orig_text)) 

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

    # Code is provided to find the gcd of any common distances appearing at least twice, just add your array:
    dCount = Counter(distanceList)
    topCount = dCount.most_common(6)
    my_gcd = topCount[0][0]
    for index in range(1, len(topCount)):
        if topCount[index][1] > 1:
            my_gcd = gcd(my_gcd, topCount[index][0])
    return my_gcd

def run_key_tests(ciphertext, alphabet): #Code provided
    """Runs Friedman and Kasiski tests and formats the output nicely"""
    friedman = friedman_test(ciphertext, alphabet)
    kasiski = kasiski_test(ciphertext)
    out = "Friedman test gives: " + str(friedman) + " and Kasiski gives this as the most likely: " + str(kasiski);
    return out

def make_cosets(text, n):
    """Makes cosets out of a ciphertext given a key length; should return an array of strings"""
    coset = [None]*n
    lis = list(text) 
    for x in range(0, n) : 
      i = x
      stri = ""
      while (i)<len(lis)-1: 
        stri += lis[i]
        i += n
      coset[x] = stri  
    return coset

def rotate_list(old_list):  #Code provided
    """Takes the given list, removes the first element, and appends it to the end of the list, then returns the
    new list"""
    new_list = old_list[:]
    new_list.append(old_list[0])
    del new_list[0]
    return new_list

def find_total_difference(list1, list2):
    """Takes two lists of equal length containing numbers, finds the difference between each pair of matching
    numbers, sums those differences, and returns that sum"""
    sum = 0
    for index in range(len(list1)): 
      sum += abs(list1[index] - list2[index])
    return sum

def find_likely_letters(coset, alpha, eng_freq):
    """Finds the most likely shifts for each coset and prints them
    Recommended strategy: make a list of the frequencies of each letter in the coset, in order, A to Z.
    Then, alternate using the find total difference method (on your frequencies list and the standard english
    frequencies list) and the rotate list method to fill out a new list of differences.  This makes a list of
    the total difference for each possible encryption letter, A to Z, in order.
    Then, find the indices of the smallest values in the new list, and i2c them for the most likely letters."""
    alphaList = list(alpha)
    cosetFreqList = [] 
    for index in range(len(alphaList)) : 
      cosetFreqList.append((coset.count(alpha[index])))
    differenceList = []
    for index in range(len(alphaList)) :
      differenceList.append(find_total_difference(cosetFreqList, eng_freq))
      cosetFreqList = rotate_list(cosetFreqList)
    letter1 = differenceList.index(min(differenceList))
    letter1 = i2c(letter1, alpha)
    secondSmallestIndex = sorted(differenceList) [1]
    letter2 = i2c(differenceList.index(secondSmallestIndex), alpha)

   
    return "the most likely letter is: " + letter1 + " followed by: " + letter2

def crack(ciphertext, alpha, eng_freq):  #Code provided
    """User-friendly walkthrough of decoding methods"""
    print("Your cipher text is: " + ciphertext)
    out = run_key_tests(ciphertext, alpha)
    print(out)
    x = int(input("Choose the key length you'd like to try: "))
    cosets = make_cosets(ciphertext, x)
    for index in range(len(cosets)):
        print("For coset " + str(index + 1) + ", " + find_likely_letters(cosets[index], alpha, eng_freq) + ".")
    s = input("Type the key you would like to use to decipher: ")
    print(vigenere_decode(ciphertext, s, alpha))
    print()




alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
            .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]

example = "YTSPOQCONOVOTNOTBTDIDIQCOHDLLGOJRQCOIDBCQVOLTIYOTNJSILQCOFDQYCOIDIQCONORNDBONTQJNGDBCQLJVIQCOPQTDNPDVTPQCONODNOHOHAONDQTGGQJJVOGGXOTC"




# For the example, the key is "PLANET" and the plaintext is:
# "For many years the known planets of our solar system were mercury, venus, earth, mars, jupiter, saturn, uranus, neputne, and pluto.  However, it is now true that many people think pluto should no longer be considered a named planet.  New planets are currently being discovered, and it is very likely that many more will be in the near future."

#Try this:
crack(example, alpha, eng_freq)

#Once everything works, uncomment the following twelve lines and crack some ciphertexts!
c1 = "KBTCSPDTIPHTVITZTTKGAMCGWGOWUWQDTZXRGGIMUADETJWHGHCGIYROHRPYGNATSPZDULMOISIQEAEFEFKXRWSAQHWBSPTDVTNMATKTSHKEROGCPLDGUMSHYCDOXARCCQUOJMHGUGCPTKIAOKPPXFQHUEOCADNLTIPHWCPMGNNVCUQEAEBHCJTWDUOBLNPTEGAFMEFKXRWSHXCKOANDWWKSPCIMCLQMHCHQSIYGNWKZAFPVWTLCUVWPSLKUEYAYETGIYQIZLDWZHWNIRINYGNATSBWAAHMORFJLHALLIZVJLSRWWSKLIWUPKTNFWILTVWKLCUHMGIKLLQKNMJLMVKAGDLDFSZUPMDSLIDEPCMIFTPJBCGPNKTGAOIPUNMJADBNMKWGRHKAANZRMCTSBNCRDUCLGTDYVXAWWAELYWECPLDROWFBCBOJROHTIFTFSVEQTIFXSMGIXSGQTAFWOXSGUGILXIVKXRWMQHWPGDDIWSKEOSBCHOXMLQQZCGTOHPQWCRDHGAOJCWMWOZIOKBIMW"
c2 = "ZSIEVVOZGHYEEFCBQDRSGDGAMFNIGKIDZCEELDBPQIIHNQUUFUFUGZSZLVVPURBQJWXNFXOZKSIIGQHTWJZOPHWEOIKRHGCUFUNIGPMPSIXHGHFGLSCLHUUUJZESUHGMQAPDNGWEVSUTUHBIZCNAFSVAFSYEEHWESBFTUHFOGDPPNVHMZOJAABCZWFVAYOMNWSEFNUSHWBRSQHQUVSUTBXGQWJVNTRKMFHKOQRZAGYDOEHZUCSYIRYSDQCEEVPBQOAPNNPSUKYRTLEIFMQRNPDZXESKEUSSZYIZNBIRAGACOYDGGUOESRHWYNSIYEDBPGAKHNWGIZMZCNPSTWFVTBRAQWHIAAGCYHDCLVNSYWWCIXHHAOOKCULBHSRVRFLAULGDYSDJAJWKEGYGTGKSCHCWFKGFOBRFMFRFMAHKMQGZHBSSFGARKRDZALCWFEHWZVGYEEHGAYWMEZHZALGFFPRAYWBKSRVRAGCFOBPAYEADMRESUFFRNQRAMYOZNUHVQLCFDYHG"
c3 = "PHXWBQDQAHGKSNVHZZYOEHISPVLELEJRDSICZAEPKJHKTKFMLVJPOWPWTCNASTQABESKLLLDQTRSLOPTAXETPCSSWCAAGHJLPTAUONAZDSPPREMSXGVVIDEKINASTQAGASJLZQCPHXHRJRICZVHMTWZQCPHXEZJKQHCULXZFNXGKPAITALARKMBRXLYCTEWHYCVUBLKNWIISULPXSXRKXHKTOPKIJWUBDJEOIIQZQSAALXYWTICOABHRFKAIELECFMDQAHHTZVLVODKNMLVDHAIXRBHXWDQAHFTPCTLPXJDRSLSULIDEEEJLSQVDTLAZDSODKUMJFDSWLADUCKZLAJJTAIDGVVPJDMLVKAIGOAGHJLPTAUONAZDSPPREMSXGVVNKUPMCDJWBATHVVYPWCOMHVVVLADHAMIRFKEGATVLVVAPPJYHYVNLZSNETQVVJWJHDXBZKAXAWCXWFXZWGNOPGIWHBTZEGXZJLTNXYMLRLTMPJSNTVJZBXPIHRNZPKWUONCFMYATHFAEMWWCIWBHYKXVZHKLHRXTBBHPIEPPGBEXHLAEMWAWVKOG"
c4="YRDOIQCGDEJEHWWYUSTOGSPZYEETMWSGDOWEMVSIENRPYDRUNEXSBLQKAKVEJKMJMBEOLPECXYCALJIEASVOOWSWATYELSIFBLVSVXWZZEJSGUTIANXSUJVVQSNINKQIYOFNSDRUIOLLXOMBQTFAXGXYMTGRIIIJEOISHDTVUSRNOJPPSIKMLSEUROFTQRYCPLZKYWSIQGZSNHVYUSRSNRRZEHDEHWXYMTRNCGMFFLZKYWLRFEMELEITMMVAJUSWQSJOLPVNARDTULPSUDJPLRJVESFRMQEGQGFOXGEPMNUAXYMJQSYIGWSNMSYHCVLRURKHYVPZYESAFO"
c5="VBLTRYTHHHIPEXTGJSZMGEDSTASZMAAZLGCIEGKKDSVWLVTSLNHJFYCBMEKFQDLNAGHMKKZXRLSYMSOLPLBLXBGPMIFAMHMGHPXFWVBFAPHXBZEGCSUWIPQILNXKUZBTYGSSTFEALYGBGPZGVWYLZMVVFVWKKZHJFEALQHQWQCIEBLTSLJLQBZEENJKTQBZEEOMTWSFMMGDNGYCCPMENKQWLLPELBGPZXVBYMDVVOIGZYXUAVHPTMVFNMVVJJPMVGLJLIABMKDHNHRGPELZDYHCFOVHVFKUHRMHMNMPKIEAXTMVJVAGPITAKVYYFMWMLWVHTUGWBBSNHWFMVMHGPZSSITAHDQZSCPIKGSXLFRMRTQJKCIQIXBSAUHPJICLVWNSEALABRWVVJVZWMZKMVRRAIEEOJHXZWVTKAVFHBBLXXGTKSRALXZAOHX"
c6= "SIKSZDISXFCFGABPJGVDYJPRKRNPCEZMGJIZVCHHOFMMLUQQAOELRGJIZHGRAVIWILDHVYQEDWTJXULCMQKHOXCJRPQBOCOFQYOHGTBWREEUOLVSMIRMBWAJRZIGKRFZCFEGEMPWVNFEESSPGUXBRBWAIMOXFSYKKIXMTLQYSLYZBKKPXKMNPKFPLCJKXTPGYRKZFFCSACABOCBRFIWIPMEWPFMFOQASVFPSNMMUMRGGJISMQYGJEUMKHNMMOKGOVPXOITSEISORYGUWXZSSCHVIWIPMJJISIGAYQSLMLUAQAJQQIETSVRBSQDCZSSFROFSEASOCFZMAOAUIFCMIEJEMSWCHMRPAWCHTINCQOIKRHKPOPGCPYPSRXISCRVVPKJRCSQCREQMFRKXTAPWGVIOEJZBXISCMIEHEDIZOOAMDELTRGPZSSFUCPPTPOLKXXSLHSCHFEUOLKGBRDSRNCPYPVNNSIEJCUCPPMAOAUIFCMIEJEMSFOYQLBPMWPCRGICZLQYSLYZBJEMSFOYQMDELGRGCPYPVNNSIEJCUCPP"
crack(c1, alpha, eng_freq)
crack(c2, alpha, eng_freq)
crack(c3, alpha, eng_freq)
crack(c4, alpha, eng_freq)
crack(c5, alpha, eng_freq)
crack(c6, alpha, eng_freq)
