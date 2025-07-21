"""
print pattern
*
* *
* * *
* * * *
"""
for i in range(1,5):
    for j in range (1,i+1):
        print("*",end=" ")
    print()

print("end of this pattern")
"""
print pattern
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(1,5):
    for j in range (1,5):
        print("*",end=" ")
    print()
print("end of this pattern")

'''
print this pattern
* * 
* * * * * 
* * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * * *
'''


for i in range(1,6):
    for j in range (1,i*3):
        print("*",end=" ")
    print()
print("end of this pattern")
