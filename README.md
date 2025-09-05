# Welcome to the class exercises

Find All Duplicates
Write a function (in python) or method (in Java) that accepts a list of integers and returns a list of only those integers that appear more than once.

Describe the two different ways to figure out all of the duplicate values of a list of integers in english. 

A: You can try to solve the Find All Duplicates with nested loops or with a map

1) The first solution is the nested loop solution. 
In this method we can take two numbers from the list and compare. If they're the same and we haven't already logged that number then it can be stored as a duplicate. 

2) The second solution is to use a dictionary or a map (similar to the containsPair method we wrote in class). 
In this method the map works as a constant and is much faster. It doesn't have to loop through each number and instead uses a tracker. 

Head should always point to the newest commit: On both one-set and main

