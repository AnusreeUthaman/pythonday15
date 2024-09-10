
#regular function
def greet():
    return "hello world"
print(greet())#hello world


#Anonymous function(lambda)

#lambda function in programming is a small anonymous function defined with the lambda keyword
#it can have any number of arguments but only have one expression.
#the expression is evaluated and returned


#syntax
   #lambda parameters: expression
greet= lambda :"hello world"
print(greet())#hello world

add=lambda x,y: x+y
print(add(5,4))#9




#map()
#syntax
    #map(function,iterable)
#map functions :Apply a function to all items in an iterable.
numbers=[1,2,3,4,5]
square=list(map(lambda x: x**2,numbers))
print(square)#[1, 4, 9, 16, 25]



#filter()
#syntax
    #filter(function,iterable)
#condition based
numbers=[1,2,3,4,5,6,7]
even=list(filter(lambda x:x%2==0,numbers))
print(even)#[2, 4, 6]


#Q-vowels
chars=['a','b','c','d','e','f']
vowels=list(filter(lambda x:x in "aeiou" ,chars))
print(vowels)#['a', 'e']



#Reduce()
#syntax
   #reduce(function,iterable)

from functools import reduce
numbers=[1,2,3,4,5]
#x=accumulator
#y=next
product=reduce(lambda x,y:x*y,numbers)
print(product)#120

#initialisation:initialise x takes the first element of the iterable and y takes the second element
#each time,x accumulates the result of the lambda function applied to x and y.



#LIST COMPREHENSION
#[expression for item in iterable]
#[expression for item in iterable if condition]
#[(expression-true)if condition else (expression-false)for item in iterable]

numbers=[1,2,3,4,5]
for i in numbers:
    squares.append(i**2)
print(squares)
    
#using list comprehension using for loop
numbers=[1,2,3,4,5]
squares=[i**2 for i in numbers]
print(squares)


numbers=[1,2,3,4,5,6,7]
even_doubles=[]
for i in numbers:
    if i%2==0:
        even_doubles.append(i*2)
print(even_doubles)

#using list comprehension
numbers=[1,2,3,4,5,6,7]
even_doubles=[i*2 for i in numbers if i%2==0]
print(even_doubles)#[4, 8, 12]


#Q-initials
names=['Alice','Bob','charlie','David']
initials=[]
for n in names:
    initials.append(n[0])
print(initials)
    
#using list comprehension
names=['Alice','Bob','charlie','David']
initials=[i[0] for i in names]
print(initials)


#Q-words with a
words=['apple','banana','cherry','dates','blueberry','kiwi']
words_with_a=[]
for i in words:
    if 'a' in i:
        words_with_a.append(i)
print(words_with_a)#['apple', 'banana', 'dates']

#using list comprehension
words=['apple','banana','cherry','dates','blueberry','kiwi']
words_with_a=[i for i in words if 'a'in i]
print(words_with_a)#['apple', 'banana', 'dates']



#Q-even num-squares or cubes
numbers=[1,2,3,4,5]
squares_or_cubes=[]
for i in numbers:
    if i%2==0:
        squares_or_cubes.append(i**2)
    else :
        squares_or_cubes.append(i**3)
print(squares_or_cubes)#[1, 4, 27, 16, 125]


#using list comprehension
numbers=[1,2,3,4,5]
#[expression-true if condition else expression-false for item in iterable]
squares_or_cubes=[x**2 if x%2==0 else x**3 for x in numbers]
print(squares_or_cubes)#[1, 4, 27, 16, 125]     
        







