#!/usr/bin/env python3
import csv

data = list()
def USE( db ):
  try:
    with open(db+".csv", newline='') as csvfile:
      buf = csv.DictReader(csvfile) 
      mem = list()
      for row in buf:
        mem.append( row )
      return { 'data': mem }
  except:
    return { 'error':"failed to open: '" + db + "'" }

def SELECT( cmd, data ):
  col    = cmd[ 1 ]
  schema = cmd[ 3 ]
  buf = USE( schema )
  if 'error' in buf:
    return {'error':(buf['error'])}
  elif 'data' in buf:
    data = buf['data']
  else:
    return {'error':("not except error")}
  
  sel = list()
  keys = list(data[0].keys())
  #if col == "*":
  #  for i in range( len( data[0].keys() ) ):
  #    print( keys[i] )
  for i in range( len( data[0].keys() ) ):
    if col == '*':
      sel.append( keys[i] )
    elif keys[i] in col:
      sel.append( keys[i] )
    
  print( "SELECT columns: ", sel )
  head = ( "| %s |" % "\t|\t".join(sel) )
  print()
  print( head )
  #for i in range( len(head) ):
  #  print( '-', end='' )
  print(end="\n")
  for row in data:
    mem = sel.copy()
    printable = not ( 'WHERE' in cmd )
    for i in range(len( sel )):
      mem[i] = row[ sel[i] ] #data[][ sel[i] ] 
    
    andgate = True
    if not printable:
      condi = cmd[5].split(",")
      for con in condi:
        greater  = '>' in con
        lessthen = '<' in con
        equal    = '=' in con
        if greater:
          c = con.split(">")
          if int(row[ c[0] ]) <= int(c[1]):
            andgate = False
        elif lessthen:
          c = con.split("<")
          if int(row[ c[0] ]) >= int(c[1]):
            andgate = False
        elif equal:
          c = con.split("=")
          if row[ c[0] ] != c[1]:
            andgate = False
    if andgate:
      print( "| %s |"  % "\t|\t".join( mem ) )
  print("OK, 200")
  return { 'result': "OK" }

while True:
  cmd = input("MiniSQL> ").split(" ")
  
  if cmd[0].lower() == 'use':
    buf = USE( cmd[1] )
    if 'error' in buf:
      print(buf['error'])
    elif 'data' in buf:
      data = buf['data']
      print( 'Ready to use: %s"' % cmd[1] )
    else:
      print("not except error")
  elif cmd[0].lower() == "print":
    print( data )
    for row in data:
      print( row )
  elif cmd[0].lower() == "select":
    res = SELECT( cmd, data )
    if 'error' in res:
      print( res['error'] )
  else:
    print("Unknow command '%s'" % cmd[0])