#List comprehension
numbers = [i for i in range(1,21)] #creating a list containing numbers from 1-20
print(numbers)
even_square_number = [i*i for i in numbers if i%2 == 0  ] #list comprehension and only contains squares of even numbers 
print(even_square_number)
