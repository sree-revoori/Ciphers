from cryptoLibrary import RSA
from cryptoLibrary import cryptoTests
from cryptoLibrary import enigma
from cryptoLibrary import Basic_Ciphers
from cryptoLibrary import Vigenere_Cipher
from cryptoLibrary import passwordCracking
from cryptoLibrary import Paillier_Cryptosystem
from cryptoLibrary import Affine_Cipher
from cryptoLibrary import Image_Encoding
from cryptoLibrary import ADFGVX_Cipher
from cryptoLibrary import Index_of_Coincidence
from cryptoLibrary import hillCipher
import decimal
import math

def almostEqual(x, y):
    return abs(x - y) < 10**-9
def roundHalfUp(d):
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def test_hillCipher():
    mat1 = [[7, 6], [4, 13]]
    mat2 = [[4, 3], [5, 6]]
    mat3 = [[6, 1], [17, 3]]
    mat4 = [[27, 13], [5, 14]]
    mat5 = hillCipher.determine_encoding_matrix("TYIL", "RHRM", alphabet, 26)
    mat6 = hillCipher.determine_encoding_matrix("TYIL", "RHRM", alpha, 59)
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet1= "ALPHBETYQWERUIOPJHGN"
    alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"
    
    assert hillCipher.hill_decode("tTtp?cIretbpAw,:YKEvcdsWgsydbpcxqmxlz!jfRlxlUM", mat4, alpha, 59) == "I WILL GO IN THIS WAY, AND FIND MY WAY OUT"
    assert hillCipher.hill_decode("CnzHbKasnOnbeznbhtmHAcv,Xlnbro?M", mat4, alpha, 59) == "All at once the ghosts come back"
    assert hillCipher.hill_encode("ALPHABET", mat1, alphabet1, 20) == "TIUYBURG"
    assert hillCipher.hill_decode("TIUYBURG", mat1, alphabet1, 20) == "ALPHABET"
    assert hillCipher.hill_encode("INFINITYWARX", mat3, alphabet, 26) == "JTMFILIFCKVU"
    assert hillCipher.hill_decode("JTMFILIFCKXA", mat3, alphabet, 26) == "INFINITYWARX"
    assert hillCipher.determine_encoding_matrix("TYIL", "RHRM", alphabet, 26) == [[13, 11], [9, 4]]
    assert hillCipher.hill_decode("RMYAAMRHMYRSDPSAMRRCXCBIFBFNMRBYQAFLJSNUAC", mat5, alphabet, 26) == "ILOOKATYOUALLSEETHELOVETHERETHATSLEEPINGA"

def test_cryptoTests():
    assert cryptoTests.isPerfectSquare(47) == False
    assert cryptoTests.isPerfectSquare(49) == True

def test_Affine_Cipher():
    assert Affine_Cipher.affine_encode_digraph("BOMBOGENESIS", alpha, 375, 114) == "JIUVKYBXWAOA"
    assert Affine_Cipher.affine_decode_digraph("PVAIUJKSYRSR", alpha, 343, 31) == "CYCLOGENESIS"
    assert Affine_Cipher.affine_encode_digraph("THISISANOTHERTESTX", alpha, 81, 119) == "FKGRGRTCBUMBKUURDG"
    assert Affine_Cipher.affine_encode("ANEWALPHABETWITHDIGITS12", alphabet1, 13, 29) == "U2N1UIR0UANW1TW0CT3TWJZM"
    assert Affine_Cipher.affine_decode("U2N1UIR0UANW1TW0CT3TWJZM", alphabet1, 13, 29) == "ANEWALPHABETWITHDIGITS12"

def test_Index_of_Coincidence():
    assert almostEqual(Index_of_Coincidence.ioc("YTSPOQCONOVOTNOTBTDIDIQCOHDLLGOJRQCOIDBCQVOLTIYOTNJSILQCOFDQYCOIDIQCONORNDBONTQJNGDBCQLJVIQCOPQTDNPDVTPQCONODNOHOHAONDQTGGQJJVOGGXOTC"), 0.07666894508999772)

def test_Basic_Ciphers():

def test_RSA():
    assert RSA.rsa(512, "RSA ENCRYPTION IS NAMED AFTER RON RIVEST ADI SHAMIR AND LEONARD ADLEMAN", alphabet) == "DXMWXQZSUHAWVVSSKBPPKKJZZLUEVWXYGQPTMUDNMCPLLSWOVHWNAEMMF"
