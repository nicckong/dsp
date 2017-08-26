# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>>

Code | Description
---- | ----
pwd | show current working directory path
mkdir | creating a directory
rmdir | deleting a directory
touch | creating a file using `touch` command
rm | deleting a file
mv | renaming a file
ls -a | listing hidden files
cp | copying a file from one directory to another
cd .. | go up one folder
man | show manual

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

Code | Description
---- | ----
ls | list directory
ls -a | list all files and folders
ls -l | list with long format (show permissions)
ls -lh | list long format with readable file size
ls -lah | list long format with readable file size including hidden files
ls -t | sort by modification time & date
ls -Glp | list long format but exclude ownername and display directories with "/"

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-a	Displays all files  
-l	Displays the long format listing
-R	Displays subdirectories as well
-t	Displays newest files first (based on timestamp)
-1	Displays each entry on a line

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> xargs reads data from standard input and executes the command one or more times based on the input read. 
An example of using xargs is to search for files containing a specific text/string. For example, to find .txt files containing text 'abc':

`
find -name "*.txt" | xargs grep "abc"
`


 

