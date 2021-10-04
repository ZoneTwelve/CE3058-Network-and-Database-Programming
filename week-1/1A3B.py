#/usr/bin/env python3
import random
# 如何不重複取數
num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
mem = num[:]
answer = [ ] # random input
limit  = 5
length = 4
for i in range(0, length):
  r = random.randint( 0, len(mem)-1 ) 
  r = mem[ r ]
  answer.append( r )
  #answer = answer + str( r )
  mem.remove( r )
print( "Real answer:", answer )
guess = "0000"
while guess != answer:
  print( "%d time remaining" % ( limit ) )
  guess = input("Input: ")
  A, B = 0, 0
  for i in range( 4 ):
    s = int(guess[ i ])
    if s == answer[ i ]:
      A = A + 1
    elif s in answer:
      B = B + 1
  print( "%dA%dB" % ( A, B ) )
  limit = limit - 1