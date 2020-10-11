
import collections

def ioc(cipher_text):
  

  cipher_flat = "".join(
  [x.upper() for x in cipher_text.split()
  if x.isalpha() ]
  )

  N = len(cipher_flat)
  freqs = collections.Counter( cipher_flat )
  alphabet = map(chr, range( ord('A'), ord('Z')+1))
  freqsum = 0.0

  for letter in alphabet:
    freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

  IC = freqsum / ( N*(N-1) )
  print(IC)
ioc("YTSPOQCONOVOTNOTBTDIDIQCOHDLLGOJRQCOIDBCQVOLTIYOTNJSILQCOFDQYCOIDIQCONORNDBONTQJNGDBCQLJVIQCOPQTDNPDVTPQCONODNOHOHAONDQTGGQJJVOGGXOTC")


