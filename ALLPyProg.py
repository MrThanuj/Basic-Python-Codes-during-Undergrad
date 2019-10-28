#convert farenheit to celsius
f=int(input("enter temperature in farenheit"))
c=(f-32)*5/9
print("temperature in celsius is",c)

#area if triangle
import math
a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle by sides is",area)

#read a binary digits and prints its decimal value(units,tens,hunds,th)
units=int(input("enter units digit:"))
tens=int(input("enter tens digit:"))
hunds=int(input("enter hunds digit:"))
th=int(input("enter thousands digit:"))
#sum=units*(2**0)
#sum=sum+tens*(2**1)
#sum=sum+hunds*(2**2)
#sum=sum+th*(2**3)
#print("sum=",sum) 
sum=units*(2**0)+tens*(2**1)+hunds*(2**2)+th*(2**3)
print("sum=",sum)

#find the roots of quadratic equation(ax**2+bx+c)
import math
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
x=(-b-math.sqrt(b**2-4*a*c))/2
y=(-b+math.sqrt(b**2-4*a*c))/2
print("Roots of quadratic equation is",x,y)

#largest of three numbers
n1=int(input('enter number 1:'))
n2=int(input('enter number 2:'))
n3=int(input('enter number 3:'))
if(n1>n2 and n1>n3):
    print("{0} is largest of {1} and {2}".format(n1,n2,n3))
elif(n2>n1 and n2>n3):
     print("{0} is largest of {1} and {2}".format(n2,n1,n3))
else:
     print("{0} is largest of {1} and {2}".format(n3,n1,n2))
     
#find factorial of given number
n=int(input('enter the number'))
fact=1
if n==0 or n==1:
    fact=1
else:
    for i in range(1,n+1):
        fact=fact*i
    print('factorial =',fact)
    
 #prepation for CA1 on 17/09/2019
 
 #conversion of temp from F to C 
 f=int(input("Enter the Temp in F"))
 c=(f-32)*(5/9)
 print("Temp in C is",c)
 
#conversion of temp from C to F   
 c=float(input("Enter the Temp in C"))
 f1=32+(9/5)*c
 print("Temp in F is",f1)  

# area of a triangle from its sides
 import math
 a=int(input("enter side1"))
 b=int(input("enter side2"))
 c=int(input("enter side3"))
 s= float (a+b+c)/2 
 area=math.sqrt(s*(s-a)*(s-b)*(s-c))
 print('area=',area)
 
# read a four digit binary number one digit at a time starting 
#from the rightmost digit and print its decimal value 
 ones=int(input("enter ones digit"))
 tens=int(input("enter tens digit"))
 hunds=int(input("enter hunds digit"))
 th=int(input("enter th digit"))
 s=(ones*(2**0)+tens*(2**1)+hunds*(2**2)+th*(2**3))
 print('decimal digit is:',s)
 
# find x to the power y for some x and y
x=int(input("Enter x(base) value:"))
y=int(input("Enter y(exponent) value:"))
Result=x**y
print("Result=",Result)
 
# roots of a quadratic equation ax**2 + bx + c = 0 given a,b and c
import math
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
root1=(-b+math.sqrt(b**2-(4*a*c)))/2*a
root2=(-b-math.sqrt(b**2-(4*a*c)))/2*a
print(root1,"root1")
print(root2,"root2")

#swap two given values
a = int(input('Enter a'))
b = int(input('Enter b'))

print('The value of a before swapping is {0}'.format(a))
print('The value of b before swapping is {0}'.format(b))

t = a
a = b
b = t
 
print('The value of a after swapping is {0}'.format(a))
print('The value of b after swapping is {0}'.format(b))

# generate a random number between 0 and 9
 import random
 print(random.randint(0,999))
 
#convert a decimal number to binary, octal and #hexa
dec=int(input("enter decimal number:"))
print("decimal equivalent binary number:",bin(dec))
print("decimal equivalent octal number:",oct(dec))
print("decimal equivalent hexa number:",hex(dec))

#read the radius of a circle and find its area
import math
r=int(input("enter the radius:"))
area=math.pi*(r**2)
print("area of circle is",area)

#Write a python program to determine a number is even or odd.
number=int(input("enter a number:"))
if(number%2==0):
    {
     print("{0} is Even".format(number))
    }
else:
    {
     print("{0} is Odd".format(number))
    }
    

#Write a python program to know whether a number is positive or negative.
n=int(input('enter the number:'))
if(n<0):
    print('{0} is negative',n)
elif(n>0):
    print('{0} is positive',n)
else:
    print('{0} is zero',n)

#Read a character A or B or C. 
#If the character input is A, program should print ‘Apple’; 
#if character entered is B, program should print ‘Banana’;
#if character entered is C, program should print ‘Coconut
a=input('enter a character')
if(a=='A' or a=='a'):
        print('APPLE')
elif(a=='B' or a=='b'):
    print('Banana')
elif(a=='C' or a=='c'):
    print('Coconut')
else:
    print('Enter A or B or C character only')

#Read three numbers and find the largest of three.
n1=int(input('enter num1'))
n2=int(input('enter num2'))
n3=int(input('enter num3'))
if(n1>n2) and (n1>n3):
    print('{0} is largest'.format(n1))
elif(n2>n1) and (n2>n3):
    print('{0} is largest'.format(n2))
elif(n3>n1) and (n3>n2):
    print('{0} is largest'.format(n3))
else:
    print('all are equal')

#Write a Python script to read the length and breadth of a rectangular garden in centimeters. The program should also find the cost of fencing the garden, if the cost of fencing per cm Rs.168. 
l=int(input('Enter the length:'))
b=int(input('Enter the breadth:'))
p=2*(l+b)
cost=p*168
print('perimeter of rectangular is:{0}'.format(p))
print('total cost:{0}'.format(cost))

#Write a Python script to read the name and age of two persons x and y. 
#The program should also print the younger of the two.
 
#Sample Input :
#Name : David   Age : 67
#Name: Jennifer  Age : 32
#Output:
#Jennifer is the youngest

x1=input('Enter Name of Person 1')
x2=int(input("Enter {0}'s Age".format(x1)))
y1=input('Enter Name of Person 2')
y2=int(input("Enter {0}'s Age".format(y1)))
if(x2<y2):
    print('{0} is the Youngest'.format(x1))
else:
    print('{0} is the Youngest'.format(y1))

c1=int(input('enter the total no of number to print:'))
a,b,c=0,1,1
print(a,'\n',b,'\n',c,'\n')
for i in range(0,c1):
    d=a+b+c
    print(d,'\n')
    a=b
    b=c
    c=d

#find 1+2+3+.n for given n
sum=0
i=1
n=int(input('enter number:'))

while i<=n:
    sum=sum+i
    i+i+1
    print('sum=',sum)

#Program to read ‘n’ numbers and count positive,
# negatives and zeros among them
nn=0
np=0
nz=0
i=1
n=int(input('enter the range:'))

while i<=n:
    i=i+1
    num=int(input('enter the numbers'))
   
    if(num<0):
        nn=nn+1
    elif(num>0):
        np=np+1
    else:
        nz=nz+1
print('postive count is{0}\n negative count is{1}\n zeros are{2}'.format(np,nn,nz))
    
#Find the factorial of a given number n using for loop

fact=1
n=int(input('enter the range'))
if(n==0) or (n==1):
    print('fact is 1')
else:
    for i in range(1,n+1):
        fact=fact*i
    print('fact=',fact)


#sample test
nn=0
np=0
nz=0
counter=1
n=int(input('enter the range:'))
while counter<=n:
    counter=counter+1
    num=int(input('enter the number:'))
    if(num<0):
        nn=nn+1
    elif(num>0):
        np=np+1
    else:
        nn=nn+1
print('Positive count is {0}\n Negative count is {1}\n Zeros are{2}'.format(np,nn,nz))



fact=1
n=int(input('enter the number'))
if(n==0) or (n==1):
    fact=1
    print('factorial=',fact)
else:
    for i in range(1,n+1):
        fact=fact*i
print('factorial=',fact)

n=9
sum=0
print(sum)
for i in range(0,n):
    if(i%2==0):
        sum=sum+2
        print(sum)
    else:
        sum=sum+1
        print(sum)
        
#LIST
#find the sum of all numbers stored in a list
l1=[1,2,3,4,5,9]
sum=0
for i in range(0,len(l1)):
    sum=sum+l1[i]
print('Sum of all numbers in list is',sum)        
        
#find the sum and average of all n numbers stored in a list given by the user
l=[]
sum=0
while(1):
    n=int(input('ENTER THE NUMBERS:'))
    if(n==000):
        break
    else:
        l.append(n)
print(l)
for i in range(0,len(l)):
            sum=sum+l[i]
print('SUM=',sum)
print('AVG=',sum/float (len(l)))

#Read a list of integers. From the input list, store only integers # between 1 and 100 in another list
l1=[]
l2=[]
size=int(input('Enter the size of list'))
for i in range(0,size):
    a=int(input('Enter the numbers'))
    l1.append(a)
print('The input list is:',l1)

for i in l1:   
    if i>=1 and i<=100:
        l2.append(i)
print('The new list is:',l2)

# Read the ages of a list of people into a list. For all ages between 40 to 50, # the string ‘middle age’ should be stored instead. Print the resulting list.
l=[]
while(1):
    age=int(input('Enter the any ages b/n 1-100:'))
    if(age==101):
        break
    else:
        l.append(age)
print('The input list is\n',l)
for i in range(len(l)):
    if l[i]>=40 and l[i]<=50:
        l[i]=['MIDDLE AGE']
    
print('The modified list is\n',l)

        
# Read two lists of integers. Display whether both lists are of same length, whether the elements in each list sum up to the same value and whether there are any values that occur in both the lists.

l1=[]
l2=[]
sum1=0
sum2=0
size=int(input('Enter the size of the list:'))
for i in range(size):
    a=int(input('Enter the numbers to list 1:'))
    l1.append(a)
print('The List1 elements are:',l1)

for i in range(size):
    b=int(input('Enter the numbers to list 1:'))
    l2.append(b)
print('The List2 elements are:',l2)

for i in l1:
    sum1=sum1+i
print('sum of list1',sum1)

for j in l2:
    sum2=sum2+j
print('sum of list2',sum2)



if(len(l1)==len(l2)):
    print("Both List1 & List2 have same length")
else:
    print("Both Lists length is not same")
    
if(sum1==sum2):
    print("Both List sum up to same value!")
else:
    print("Both lists sum is different")


for i in l1:
    for j in l2:
        if(i==j):
            print(i,"value has occured in both lists")

# Read a list of names. Find how many times the letter 'a' appears in the list
names=[]
count=0
size=int(input("enter the total numbers of names"))
for i in range(size):
    n=input('enter the names:')
    names.append(n)
print('names are',names)
 
for i in names:
    for j in i:
        if j=='a':
            count=count+1
print(count)

# to search for an element ‘x’ in a given list of n #integers
l1=[]
while(1):
    n=int(input('Enter the integers'))
    if(n==000):
        break
    else:
        l1.append(n)
x=int(input('enter the integer to be searched'))

print('input list is',l1)
flag=1
for i in l1:
    if(i==x):
        flag=0
        break
   
if flag==0:
    print(x,'Found')
else:
    print(x,'Not found')
    

 #Read a list of integers from the user till the user inputs 000. Using list comprehension create new lists namely
#Square, where each element is a square of the corresponding element in the input list
#Positive, with only positive numbers in the input list
l=[]
l1=[]
l2=[]
while(1):
    n=int(input('Enter the number:'))
    if(n==000):
        break
    else:
        l.append(n)
    
l2=[i*i for i in l]
print('square of numbers',l2)
for i in l:
    if(i>0):
       l1.append(i)
print('postive numbers are',l1)
print('input list is',l)

#Using list comprehension create two lists
#Odd -  list of odd integers from 1 to 10.
#Even – list of even integers from 1 to 10.
odd=[]
even=[]
l=[]
while(1):
    n=int(input('Enter the numbers:'))
    if(n==000):
        break
    else:
        l.append(n)
for i in l:
    if(i%2!=0):
        odd.append(i)

    elif(i%2==0):
        even.append(i)
     
    else:
         break
print('odd numbers are',odd)
print('even numbers are',even)      
            #OR#
odd=[]
even=[]
odd=[i for i in range(1,11) if i%2!=0]
even=[i for i in range(1,11) if i%2==0]
print('odd numbers:',odd)
print('even number:',even)

# Calculate the class average of the first course
grades=[[98,99,93],[78,65,87]]
course_index=0
sum=0
for k in range(0,len(grades)):
    sum=sum+grades[k][course_index]
    
print('sum:',sum)
print('Avg of 1st course of 2 student is',sum/float(len(grades)))

#Average of each course
grades=[[98,99,93],[78,65,87]]
sum=0

for k in range(0,len(grades)):
        
   for course_index in range(0,3):
        sum=sum+grades[k][course_index]
        
print('sum',sum)
print('avg',sum/float(len(grades)))














A=[]
n=int(input("Enter N for N x N matrix : "))        #3 here
#use list for storing 2D array
#get the user input and store it in list (here IN : 1 to 9)
print("Enter the element ::>")
for i in range(n): 
   row=[]                                        #temporary list to store the row
   for j in range(n): 
      row.append(int(input()))             #add the input to row list
   A.append(row)                            #add the row to the list
print(A)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Display the 2D array
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")
   print() 
   
B=[]
n=int(input("Enter N for N x N matrix : "))        #3 here
#use list for storing 2D array
#get the user input and store it in list (here IN : 1 to 9)
print("Enter the element ::>")
for i in range(n): 
   row=[]                                        #temporary list to store the row
   for j in range(n): 
      row.append(int(input()))             #add the input to row list
   B.append(row)                            #add the row to the list
print(B)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Display the 2D array
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(B[i][j], end=" ")
   print() 

                                           #new line
result = [[0,0,0], [0,0,0], [0,0,0]] 

# iterate through rows 
for i in range(n):    
# iterate through columns 
    for j in range(len(A[0])): 
        
       result[i][j] = A[i][j] + B[i][j] 
   
    print("Resultant Matrix is ::>")
    for r in result: 
       print("Resultant Matrix is ::>",r) 
       
       
      
        
                   #*********Tuples*********#
                  
#Read the marks of ‘n’ students in a course as a tuple and find the sum, average, highest and lowest.
marks=eval(input('Enter the marks in ()'))
sum=0
n=len(marks)
for i in range(n):
    sum=sum+marks[i]
print('Sum of all marks',sum)
print('Avg of all marks',sum/n)
print('Maximum marks',max(marks))
print('Minimum marks',min(marks))

#Write a Python script that prompts the user to enter types of fruits and their corresponding weight in pounds. The program should then print the information in the form of fruit, weight first 
#a) sorted using alphabetical order of fruit names and then 
#b) in ascending order of fruit weights and 
#c)in descending order of fruit weights
#Using a list of tuples
import operator
fruit=[]
fruit_1=[]
fruit_2=[]
fruit_3=[]
num=int(input('Enter the no of fruits:'))

for i in range(num):
    f=eval(input('Enter fruit name & weight in ()'))
    fruit.append(f)
print(fruit)

fruit_1=sorted(fruit)
fruit_2=sorted(fruit,key=operator.itemgetter(1))
fruit_3=sorted(fruit,key=operator.itemgetter(1),reverse=1)

print(fruit_1)
print(fruit_2)
print(fruit_3)

########
t=()
while(1):
    n=int(input('Enter ages:'))
    if(n==000):
        break
    else:
        t=t +(n,)
        
print('Ages are',t)


###########
t=()
while(1):
    n=input('Enter the names:')
    if(n=='AAA'):
        break
    else:
        t=t +(n,)
unique=[]
for i in t:
    if i not in unique:
        unique.append(i)
        print('The name {0} occurs {1} times'.format(i,t.count(i)))
        
##############
import statistics
from statistics import mode
t=()
while(1):
    a=input('ENTER NAMES')
    if a=='AAA':
        break
    else:
        t=t +(a,)
print(t)
print('The most frequent name is:',mode(t))


#############
t=()
while(1):
    a=input('Enter the name:')
    if(a=='AAA'):
        break
    else:
        t=t +(a,)
print(t)
r=input('Enter the removing name:')
for i in range(len(t)):
    if t[i]==r:
        t=t[:i]+t[i+1:]
        break
print('The list after removing {0} is {1}'.format(r,t))

sl=[]
while(1):
    a=eval(input('enter the shopping list with item name & weight in ()'))
    if(a==()):
        break
    else:
        sl.append(a)
#########################################
A=[]
n=int(input('Enter N for NxN matrix:'))
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input('Enter the Numbers')))
        
    A.append(row)
print(A)

for i in range(n):
    for j in range(n):
       print(A[i][j], end=" ")
    print()

B=[]
n=int(input('Enter M for MxM matrix:'))
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input('Enter numbers')))
B.append(row)
print(B)
for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
for r in result:
        print('Resultant MAtrix is:',r)














                

       
    

    



















 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    