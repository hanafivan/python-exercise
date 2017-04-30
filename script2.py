#usr/bin/python

def verbing(s):
    if (len(s) >= 3 and s[-3:len(s)] == 'ing'):
        print (s+'ly')
    elif (len(s) >= 3 and s[-3:len(s)] != 'ing'):
        print (s+'ing')
    else:
        print (s)

verbing('flyover')
verbing('swimming')
verbing('ju')

#Not_bad replace

#front back
def front_back(a):
    if (len(a)%2==0):
        print (a[0:len(a)/2]+','+a[len(a)/2:len(a)])
    elif (len(a)%2!=0):
        print (a[0:len(a)/2+1]+','+a[len(a)/2+1:len(a)])

front_back()