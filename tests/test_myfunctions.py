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


def test_RSA():
  assert RSA.rsa(512, "RSA ENCRYPTION IS NAMED AFTER RON RIVEST ADI SHAMIR AND LEONARD ADLEMAN", alphabet) == DXMWXQZSUHAWVVSSKBPPKKJZZLUEVWXYGQPTMUDNMCPLLSWOVHWNAEMMF
