'''Python_Section'''
# 1. Whatis decorator , write a decorator?
    Decorator is a way to chande or enhance the behaviour of a function/ class without changing the original it self.
     It's a function which take another function as an argument.
for example: creat a calculator using deorator?

def decore(calculator):
    def substraction(a,b):
        sub=a-b
        return sub, calculator(a,b)
    return substraction

@decore
def calculator(a,b):
    add=a+b
    return add
print(calculator(45,60))


# 2. Whatis lambda expression, write a lambda expression?
   It is a single line statement.
    syntax:
    lambda parameter:logics/statements
   A lambda expression is a quick way to create a small, one-time-use function in programming.
   For example, as a shortcut it is for defining a function without giving it a name.

lambda x, y: x + y


# 4. WAF,Reverse a string words.
#   > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function
s = input('hello world')
def reverse_str(s):
    reversed_str = ''
    for i in s:
        reverse_str = i + reverse_str
        return reverse_str




# 6. Sort a list integer element without using inbuilt function?
def sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
numbers = [48, 60, 49, 54, 34]
sort(numbers)
print(numbers)

# 7. Li = [1,2,3,4], Li2 = [10,20,30]
 Result = {1:10,2:20,3:30}
 Take a two list a parameter, return dictionary, look like above result.

def lists_to_dict(keys, values):
    result_dict = {}
    for key, value in zip(keys, values):
        result_dict[key] = value
    return result_dict
Li = [1, 2, 3, 4]
Li2 = [10, 20, 30, 40]
result = lists_to_dict(Li, Li2)
print(result)

# 8. Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
 the csv and print in console bar
import csv
data = [
    ["first_name", "email", "phn_no"],
    ["abhilash panigrahi", "abhilash.panigrahi.02@gmail.com", "6370818133"],
    ["swagatika pradhan", "swagatikap624@gmail.com", "6372513766"],
    ["sibasrita pradhan", "sibasrita265@gmail.com", "9438626183"],
    ["Abhilipsa", "abhilipsa65@gmail.com","63702513766"],
    ["Gitanjali sethi", "gita_njali02@gmail.com", "637548606"],
]
print(data)


# 9. What is exception handling , how handel the exception in python , explain with each block?
Exception_handling in python is a mechanism for managing errors and unusual conditions that occur during a program execution using try, except, else and finally blocks.
    try :
    The code inside try(result = a/b) tries to prform division.

    else:
      if there are no errors, it prints the result of the division.

    finally:
       this block always runs.


# 10. Difference between Moudle and Packages (3 diff)

module:-
* A single file containing
* It can define functions, classes, and variables, and can include runnable code.
* A module is just a single .py file,
 for example= swag.py

pakage:-
* it containing one or more Python
* It allows for a hierarchical structure of modules.
* A package is a directory with a special _init_.py file.

#11. Difference between List vs tuple vs set vs dictionary?
list
1. list is encloses by a [].
2. list allows duplicate elements.
3. list is a mutable data type.
4. It is a heterogenous data type.

tuple
1. Tuple is written inside a ().
2. It allows duplicate elements.
3. It is an immutable data type.
4. It is a heterogenous data type.

set
1.set is written inside a {}.
2. it does not allow duplicate elements.
3. It is a immutable data type.

Dictionary
1. It encloses with a {}.
2.It represents in a key:value pair.
3.keys are immutable but value can be same.

# 15. Explain break, continue, pass with code?

1.break:-it is used to terminate the loop or statement in which it is present.
example;
for i in range(5):
    if i<=3:
        break
2.continue:-Continue is also a loop control statement just like the break statement.

 for i in range(0,10):
     if i==5:
         continue

3.pass:-The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

for i in range(20):
    pass

'''SQL'''
1.Explain about the DML,DDL,TCL,DQL commands?
DDL=DDL commands manage database structure,
DML=DML commands handle data manipulation.
TCL=TCL commands manage transactional changes.
DQL=used for fetching data from a relational database.

