'''
generate one time password, random,time
#Lets try to generate random number
#linking the OTP with time
#range will give a sequence
#help() all the help documentation
'''

import random
help('random') 
print(dir(random))

import random
import time

a = random.randint(55,105)

for i in range(1,10):
    print(random.randint(1000,9999))
    time.sleep(5)
    print(i)


