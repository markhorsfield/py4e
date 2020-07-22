#!/usr/bin/python3

text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(':')
#print("ipos",ipos)
text2 = text[ipos+1:]
#print("text2",text2)
text3 = float(text2.strip())
#print(type(text3))
print(text3)
