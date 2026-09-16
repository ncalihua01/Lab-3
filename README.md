# Lab-3
In this lab, we use the full suite of data structures as well as file and error handling.

# Directions for submission
Create a github repo called "Lab-3." Invite me as a collaborator to your repo.  Download the repo files here as a zip file.  Unzip the files and add them to your repo.  Modify the files as appropriate according to the instructions.  Do not change names.  Commit and push changes to your repo.

# Directions for solutions
Do not change any of the code given to you (other than the comments which should absolutely be removed).  I will run your code with the expected structure.  You are welcome to add any additional lines of code or functions you find necessary.  If you make changes in which your solutions do not run, you will receive no credit for that problem.  All solutions should include a docstring with doctests.  Unless otherwise specified, all functions should end with a return of the appropriate type and not a print statement.

# Problem 1
Design the function flatten that takes a (possibly deep) list and "flattens" it.  That is, removes any internal nesting so that it is just a single list.

# Problem 2
Consider the class of lists which are sorted in ascending order (duplicates are allowed).  Design the function merge which takes in two sorted lists and returns a new list that contains all of the elements in the two lists in sorted order.

# Problem 3
Write a one-line function, count_vowels, that counts the number of vowels in a given character string.

# Problem 4
Write a program that outputs all possible strings formed by using the characters "c", "a", "t", "d", "o" and "g" exactly once.  Then, generalize to design a function word_scramble, that takes in a sequence of characters (allowing inputs to be either lists, strings or tuples) and returns a list of all possible strings formed by using whose characters exactly once.  If the initial sequence included to "c"s, for example, the possible strings would also still include those two "c"s.

# Problem 5
Design a function make_change that takes in two numbers as input amount_paid and amount_owed as in Lab 1.  The function should now return a dictionary with the number of each kind of bill and coin to give back as change in as few bills and coins as possible.  If the difference is negative (i.e. if the customer still owes money), the function should return the message "After this payment, your total due is $[balance]." where balance is given by the inputs.

# Problem 6
Design functions merge_sets and word_scramble_sets which have the same functionality of merge and word_scramble but where the input(s) and output is now a set.

# Problem 7
Take a list of 3000 randomly generated data points.  Write this data to a file called "random.txt" formatted so that the file has commas separating values, 3 values are printed per line, and the first line of the file reads "col1, col2, col3".
