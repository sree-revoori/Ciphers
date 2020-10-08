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

def almostEqual(x, y):
    return abs(x - y) < 10**-9

def test_hillCipher():
    assert hillCipher.hill_decode("tTtp?cIretbpAw,:YKEvcdsWgsydbpcxqmxlz!jfRlxlUM", mat4, alpha, 59) == "I WILL GO IN THIS WAY, AND FIND MY WAY OUT"
    
def test_Affine_Cipher():
    assert Affine_Cipher.affine_encode_digraph("BOMBOGENESIS", alpha, 375, 114) == "JIUVKYBXWAOA"
    assert Affine_Cipher.affine_decode_digraph("PVAIUJKSYRSR", alpha, 343, 31) == "CYCLOGENESIS"
    assert Affine_Cipher.affine_encode_digraph("THISISANOTHERTESTX", alpha, 81, 119) == "FKGRGRTCBUMBKUURDG"
    assert Affine_Cipher.affine_encode("ANEWALPHABETWITHDIGITS12", alphabet1, 13, 29) == "U2N1UIR0UANW1TW0CT3TWJZM"
    assert Affine_Cipher.affine_decode("U2N1UIR0UANW1TW0CT3TWJZM", alphabet1, 13, 29) == "ANEWALPHABETWITHDIGITS12"

def test_Index_of_Coincidence():
    assert almostEqual(Index_of_Coincidence.ioc("YTSPOQCONOVOTNOTBTDIDIQCOHDLLGOJRQCOIDBCQVOLTIYOTNJSILQCOFDQYCOIDIQCONORNDBONTQJNGDBCQLJVIQCOPQTDNPDVTPQCONODNOHOHAONDQTGGQJJVOGGXOTC"), 0.07666894508999772)

def test_Basic_Ciphers():
    assert Basic_Ciphers.

def test_RSA():
    assert RSA.rsa(512, "RSA ENCRYPTION IS NAMED AFTER RON RIVEST ADI SHAMIR AND LEONARD ADLEMAN", alphabet) == "DXMWXQZSUHAWVVSSKBPPKKJZZLUEVWXYGQPTMUDNMCPLLSWOVHWNAEMMF"
