# Week 1, Day 2: Advanced Python Challenge
## Introduction : 
This file contains about list comprehension and lambda function as a part of my week1_day2 of "Python_for_ML_Roadmap.

##Challege overview:
it consists of 2 parts 
# part 1 : list comprehension
**Problem**:Create a new list containing the squares of only the even numbers from a given list of numbers from 1 to 20.
**Solution:** I used a list comprehension with a conditional filter to achieve this. The code efficiently iterates through the list and calculates the square for each number that meets the specified criteria (being an even number).

# Part 2 : lambda function with 'map()' 
**Problem:** From a list of product dictionaries, extract only the prices and put them into a new list.
**Solution:** I used a combination of Python's built-in `map()` function and an anonymous `lambda` function. The lambda function was used to define a simple, single-use operation that extracts the 'price' value from each dictionary in the list. The `map()` function then applied this operation to every item in the list.


## How to Run the Code

To run the code, simply execute the `week_1_day_2.py` file in a Python environment. No external libraries are required.

```bash
python week_1_day_2.py

