
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# ## Python Review With Movie Data
# 
# ---
# 
# In this lab, you'll be using the [IMDb](http://www.imdb.com/) `movies` list below as your data set. 
# 
# This lab is designed to help you practice iteration and functions in particular. The normal questions are more gentle, and the challenge questions are suitable for advanced/expert Python students or those with programming experience. 
# 
# All of the questions require writing functions and using iteration to solve. You should print out a test of each function you write.
# 
# 
# ### 1) Load the provided list of `movies` dictionaries.

# In[1]:


# List of movies dictionaries:

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# ---
# 
# ### 2) Filtering data by IMDb score.
# 
# #### 2.1)
# 
# Write a function that:
# 
# 1) Accepts a single movie dictionary from the `movies` list as an argument.
# <br>2) Returns `True` if the IMDb score is greater than 5.5.

# In[27]:


# Your code here
# List of movies dictionaries:


def imdb_score(name_of_movie):
    for m in movies:
        if m["name"]==name_of_movie and m["imdb"]>5.5:
            rating = True
        elif m["name"] == name_of_movie and m["imdb"]<5.5:
            rating = "Score has to be over 5.5"
            return rating

imdb_score("we two")


# #### 2.2 Challenge)
# 
# Write a function that:
# 
# 1) Accepts the `movies` list and a specified category.
# <br>2) Returns `True` if the average score of the category is higher than the average score of all movies.

# In[2]:


# Your code here


# ---
# 
# ### 3) Creating subsets by numeric condition.
# 
# #### 3.1)
# 
# Write a function that:
# 
# 1) Accepts the list of movies and a specified IMDb score.
# <br>2) Returns the sublist of movies that have scores greater than the one specified.

# In[36]:


# Your code here
def selected_movies(movies):
    selected_movies=[]
    for m in movies:
        if m["imdb"]>8: ##i am strugglig with this one, it is only pickig one movieand addinone the empt list. where am i goin wrong?
            selected_movies.append(m["name"])
            return selected_movies
        

all_movies = selected_movies(movies)
print(all_movies)


# #### 3.2 Challenge)
# 
# Write a function that:
# 
# 1) Accepts the `movies` list as an argument.
# <br>2) Returns the `movies` list sorted first by category and then by movie according to category average score and individual IMDb score, respectively.

# In[3]:


# Your code here.


# ---
# 
# ### 4) Creating subsets by string condition.
# 
# #### 4.1)
# 
# Write a function that:
# 
# 1) Accepts the `movies` list and a category name.
# <br>2) Returns the movie names within that category (case-insensitive!).
# <br>3) If the category is not in the data, prints a message that says it does not exist and returns `None`.
# 
# Recall that, to convert a string to lowercase, you can use:
# 
# ```python
# mystring = 'Dumb and Dumber'
# lowercase_mystring = mystring.lower()
# print lowercase_mystring
# 'dumb and dumber'
# ```

# In[48]:


# Your code here
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def movie_list_and_category(category):
    movie_list_and_categories =[]
    
    for m in movies:
        if m["category"] == category.lower():
            movie_list_and_category.append(m["name"])
            return movie_list_and_category
        
romance_movies = movie_list_and_category("Romance")
print (romance_movies)
movie_list_and_category("thriller")


# #### 4.2 Challenge)
# 
# Write a function that:
# 
# 1) Accepts the `movies` list and a "search string."
# <br>2) Returns a dictionary with the keys `'category'` and `'title'` whose values are lists of categories that contain the search string and titles that contain the search string, respectively (case-insensitive!).

# In[4]:


# Your code here


# ---
# 
# ### 5) Multiple conditions.
# 
# #### 5.1)
# 
# Write a function that:
# 
# 1) Accepts the `movies` list and a "search criteria" variable.
# <br>2) If the criteria variable is numeric, return a list of movie titles with a score greater than or equal to the criteria.
# <br>3) If the criteria variable is a string, return a list of movie titles that match that category (case-insensitive!). If there is no match, return an empty list and print an informative message.

# In[ ]:


# Your code here

