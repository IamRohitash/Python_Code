##command line arguments
## Apython prigram to display command line arguments

import sys
n=len(sys.argv)
args=sys.argv
print('no of command line arguments:',n)
print('the args are:',args)
print('the args one by one:')
for i in args:
    print(i)