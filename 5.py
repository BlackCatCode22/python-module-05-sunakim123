#Counting Word Frequency
from idlelib.run import handle_tk_events

fname = input('Enter File: ')
if len(fname) <1 : fname = 'clown.txt'
fhand = open(fname)

di = dict()
for lin in fhand:
    lin = lin.rstrip()
    wds = lin.split()
    for w  in wds:
            di[w] = di.get(w,0) + 1

print(di)

largest = - 1
theword = None
for k, v in di.items() :
    if v > largest:
        largest = v
        theword = k

print (theword, largest)


#Sorting a Dictionary Using Tuples
fname = input('Enter File: ')
if len(fname) <1 : fname = 'clown.txt'

fhand = open(fname)
many =dict()

for line in fhand :
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w,0) + 1

tmp = dict()
newlist = list()
for k, v in many.items():
    tup = (v, k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)

for v, k in cool[:5]:
    print(k,v)


#Regular Expressions
import re
hand = open('clown.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))