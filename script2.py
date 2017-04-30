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