#Write a python script to print first N odd natural numbers in reverse order

for x in range(int(input('Enter N Value : ')),0,-1):
    print(x*2-1,end=' ')