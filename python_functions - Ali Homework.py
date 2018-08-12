
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# ## Practise Python Functions
# 
# ---

# ### Resources: potentially helpful functions
# 
# * [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
# * [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate)
# * [`len`](https://docs.python.org/3/library/functions.html#len)
# * [`int`](https://docs.python.org/3/library/functions.html#int)
# * [`list`](https://docs.python.org/3/library/functions.html#func-list)
# * [`reversed`](https://docs.python.org/3/library/functions.html#reversed)

# ---
# 
# ### 1) Write a function that takes the length of a side of a square as an argument and returns the area of the square.

# In[4]:


# A:
side=5
areaofsquare=side**2
print(areaofsquare)


##Solution2

# Python Program - Calculate Area of Square

print("Enter 'x' for exit.");
side = input("Enter side length of Square: ");
if side == 'x':
    exit();
else:
    side_length = int(side);
    area_square = side_length*side_length;
    print("\nArea of Square =",area_square);


# ---
# 
# ### 2) Write a function that takes the height and width of a triangle and returns the area.

# In[19]:


# A:

def area_rectangle (height, width):
    area = height * width
    print("Area of a Rectangle is: ", area)
area_rectangle(5, 10)


# ---
# 
# ### 3) Write a function that takes a string as an argument and returns a tuple consisting of two elements:
# - **A list of all of the characters in the string.** 
# - **A count of the number of characters in the string.**

# In[34]:


# A:
string="thisisastring"

print(list(string), len(string))

##solution 2

def stringargument (string):
    stringargument=list(string)
    return(stringargument, len(stringargument))
stringargument('thisisastring')


# ---
# 
# ### 4) Write a function that takes two integers, passed as strings, and returns the sum, difference, and product as a tuple (with all values as integers).

# In[39]:


# A:
def function(x,y):
    x=int(x)
    y=int(y)
    sum=(x+y)
    difference=(x-y)
    product=x*y
    return(sum, difference, product)
tuple=function(2,3)
print(tuple)


# ---
# 
# ### 5) Write a function that takes a list as the argument and returns a tuple consisting of two elements:
# - **A list with the items in reverse order.**  
# - **A list of the items in the original list that have an odd index.**

# In[62]:


# A:
def listargument (list_a):
    reverse=list(reversed(list_a))
    oddlist=list_a[1::2]
    
    return(reverse, oddlist)
listargument([1,2,3,4,5,6,7,8,9,10,12,14,16])


    


# In[63]:


##Q5 Solution 2

##solution2:

def listargument (list_a):
    reverse=list(reversed(list_a))
    oddlist=[]
    
    for count, i in enumerate(list_a):
        if count % 2==1:
            oddlist.append(i)
            
    return(reverse, oddlist)
listargument([1,2,3,4,5,6,7,8,9,10,12,14,16])


# ---
# 
# ### Challenge: Write a function that returns the score for a word. A word's score is the sum of the scores of its letters. Each letter's score is equal to its position in the alphabet.
# 
# So, for example:
# 
# * A = 1, B = 2, C = 3, D = 4, E = 5
# * abe = 8 = (1 + 2 + 5)
# 
# 
# ***Hint 1:*** *The string library has a property, `ascii_lowercase`, that can save some typing here.*
# 
# Nowadays, most of the `string` module's components are already built into Python. However, it still has several [constant values](https://docs.python.org/3/library/string.html#string-constants) that can be useful, including:
# ```python
# string.ascii_uppercase
# ```
# 
# ***Hint 2:*** *you may want to use a `list`'s [`index` method](https://www.tutorialspoint.com/python3/list_index.htm)*

# In[1]:


import string

string.ascii_uppercase


# In[76]:


# A:
import string
letters_score=[]*len(string.ascii_lowercase)
score=letters.index(string.ascii_lowercase)
def word_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        total += score[letters]
    return total
word = 'ali'
word_score('ali')

