# Coding Challenge for GB

This repository contains my submission for the coding challenge at GB.  I have included comments in the files themselves, but I will include some additional commentary about my thought processes here. 

## 1. Database Design

![DB Visual Schema](https://raw.githubusercontent.com/baldegg/gb-homework/master/schema.png)

This exercise is presented in [schema.sql](https://github.com/baldegg/gb-homework/blob/master/schema.sql), a schema file which can be imported into a new or existing database (as long as table names do not conflict).  Each table contains auto-incrementing primary id columns so we can easily address each row by a unique id.  Since all of the information in these columns is important, every column has been flagged with the "NOT NULL" constraint.  

Based on the article provided, I created 3 tables in a MySQL database:
1. An '*articles*' table which contains the article id, title, content, published date, author, thumbnail, and category.
2. A '*categories*' table which simply contains the category id and its associated name.
3. A '*users*' table which contains the user's id, username, email, full (display) name, role, and password hash.

The *articles* table contains the article itself and important data about it.  Its article_content is assumed to be HTML or some sort of markdown language processed outside of the database.  This field is of MEDIUMTEXT type; a regular TEXT field would probably suffice, but it's possible that articles may exceed 64KB at some point. We have a thumbnail field where we can specify an image url to be displayed as the thumbnail on lists of articles.  article_category_id column is linked to the foreign key category_id in the categories table, meaning that MySQL will only allow article_category_id's to be chosen from those that exist as category_id's.

The *categories* table may seem redundant since it only contains an id and an associated name, but it's probably a good idea to compartmentalize it.  For example, having a simple linear list of categories in one page makes it easier to create an index page or nav bar of all categories. Because we have not specified an "ON DELETE" policy in the foreign key constraints, MySQL will default to "RESTRICT", which will not allow us to delete a category until all articles under that category are deleted or recategorized.  We could also tell MySQL to "CASCADE" on deleting a category, meaning it would delete all associated articles, or we could set a "DEFAULT" category to which orphaned categories would revert when their parents are deleted.  For now, though, "RESTRICT" seems safest to reduce unintentional deletion of articles and lazy categorization.

The *users* table would most likely actually be handled by the web framework (ie Django) or the CMS, not a "roll your own" implementation such as this.  A very simple users table is included here for illustrative purposes.  The table contains basic information that allows users to login and access permitted activities.  The user_role field is probably beyond the scope of this exercise, but in a real-life situation, it would be linked to a permissions table, which would determine what each user group is allowed to do (post, edit, delete, etc.) As with the categories, the article_author_id is linked to the user_id via a foreign key constraint that restricts deletion of authors who have articles published. 


## 2. API Interaction

This exercise is found at [jsonplaceholder.py](https://github.com/baldegg/gb-homework/blob/master/jsonplaceholder.py).  

1. **GET** - Simply performing a get request on the url (https://jsonplaceholder.typicode.com/todos/) returns a list of 200 TODOs.  As discussed in the comments, we assume this to be a list of the newest 200 TODOs, even though id numbers aren't usually reverse-chronological.  If we assumed otherwise, we would need some way of finding the most recent todo, hopefully through an API endpoint, but in the worst case we could brute force it by iterating to the end of the list and counting backwards by 200.

2. **POST** - We send a request of method POST to the API containing a header specifying our content type and a body of JSON.  We know that the server accepts the POST because we get a response back containing the information we posted along with the id number of the new TODO.

3. **DELETE** - We send a DELETE request to the API of the TODO specified by parameter.  Depending on whether the TODO was found our not, we present the user with an appopriate message.


## 3. Algorithms

This exercise is found at [permutations.py](https://github.com/baldegg/gb-homework/blob/master/permutations.py).  A sample infile is found at [permies.txt](https://github.com/baldegg/gb-homework/blob/master/permies.txt).  Command line usage is " python permutations.py filename.txt ".

The program loads a given text file line by line into a list of strings to be permuted.  The permutation function is called on each of the strings and iterates letter by letter, swapping letters and calling itself recursively until the end of the string is reached.  This process is explained in detail in the comments in the python file.

In permutations, the order of letters is considered important, even if they are the same letter, so the program will always return n! permutations where n is the length of the string.  Because of this, I believe the theoritical complexity is somewhere on the order of O(n! * n log n ) since we are also presorting the string using python's sorted method, which runs in O(n log n).  Since we are making a lot of recursive calls in a language not especially performance-oriented, actual runtime performance is a lot worse than theoretical.  From rough tests, this implementation seems to complete in around the same timeframe as itertool's.  On my system, both have trouble once inputs exceed 10 characters.  If we needed to increase performance or process larger strings, I would consider porting the permute function to higher performance a language like C or trying to figure out a purely iterative way to produce the permutations.






