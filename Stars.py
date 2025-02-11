'''
   *
  **
 ***
****
'''

n = int(input("Enter the row number: "))

for i in range(n+1):
    print((n-i)*" ", end='')
    print(i*"*")
