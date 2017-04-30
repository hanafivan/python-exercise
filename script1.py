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

#C

def fix_start(s):
    print(s.replace(s[1:len(s)] , '*'*len(s)))

fix_start('babel')
fix_start('testing')

#D mix up

def mix_up(a,b):
    print (a.replace(a[1:2],b[1:2])+','+b.replace(b[1:2],a[1:2]))

mix_up('dog','dinner')

