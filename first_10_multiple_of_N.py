#Write a python script to print first 10 multiples of N

n=int(input('Enter N Value : '))
for x in range(1,11):
    print(n,'*',x,':',x*n)