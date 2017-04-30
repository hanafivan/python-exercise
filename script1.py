#!usr/bin/env python -tt

def donuts(count):
    if (count<10):
        print (count)
    else:
        print ('many')


#B

def both_end(s):
    if(len(s)<=2):
        print ('')
    else:
        print (s[0]+s[1]+s[-2]+s[-1])

both_end('spring')
both_end('ak')

def fix_start(s):
    print(s.replace(s[1:len(s)] , '*'*len(s)))

fix_start('babel')
fix_start('testing')