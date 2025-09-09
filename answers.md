# Lab 3 Answers

## Part 1: Git

### 1.1. List the contents of the lab03-exercises repo immediately after initialization
```
# paste code here
mariahaddon@Marias-MacBook-Pro lab03-exercises % ls -a
.               ..              .git            README.md
mariahaddon@Marias-MacBook-Pro lab03-exercises % cd .git
mariahaddon@Marias-MacBook-Pro .git % ls
branches        config          description     HEAD            hooks           info            objects         refs

```

### 1.2. Paste the output of your `git status` command
```
# paste code here
mariahaddon@Marias-MacBook-Pro lab03-exercises % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md

nothing added to commit but untracked files present (use "git add" to track)

```

### 1.3. Paste the output of the state of your repository after committing your README.md file
```
# paste code here
mariahaddon@Marias-MacBook-Pro lab03-exercises % git commit -m "add README.md to the repository"
[master (root-commit) e1bb5f6] add README.md to the repository
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
mariahaddon@Marias-MacBook-Pro lab03-exercises % 

```

### 1.4. Copy your `git log` output
```
# paste code here
mariahaddon@Marias-MacBook-Pro lab03-exercises % git log
commit e1bb5f6360ad1bacd098ee8113f2f0417f28f651 (HEAD -> master)
Author: Maria <mariabhaddon@gmail.com>
Date:   Wed Sep 3 13:08:50 2025 -0400

    add README.md to the repository

```

### 1.5. Copy your `git diff` output
```
# paste code here
mariahaddon@Marias-MacBook-Pro lab03-exercises % git diff
diff --git a/README.md b/README.md
index 2a41c9d..205cfd3 100644
--- a/README.md
:...skipping...
diff --git a/README.md b/README.md
index 2a41c9d..205cfd3 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,4 @@
 # Welcome to the class exercises
 
+Find All Duplicates
+Write a function (in python) or method (in Java) that accepts a list of integers and returns a list of only those integers that appear more than once.
~

```


### 1.6. Reflection

We've learned 6 git subcommands now. Describe each of them in your own words in the section below:

* git init - Creates a brand new repository
* git status - Shows the progress and what's been done
* git add - Adds what you want before commiting, writing a commit message, and then pushing. "Stages" the changes that you made. 
* git commit - Makes a message of what you did to log it for the future. You can track your history. 
* git log - Shows the history of commits. Can tell who made the changes on what date/time. 
* git diff - Shows the differences of what's been changed


### 1.7. Practice: Find All Duplicates (Java)
Make sure you implement the `FindDuplicates.java` class as specified in the instructions (with the nested loops implementation).

## Part 2: GitHub

### 2.1. Practice: Find All Duplicates (Python)
Make sure you implement the `find_duplicates.py` file as specified in the instructions (with the nested loops implementation).


## Part 3: Branching

### 3.1. Implement the More Efficient Version of the "Find Duplicates" problem
Implement the more efficient Version of the "Find Duplicates" problem using a dictionary (or hashmap) data structure instead of nested loops. You may do this in either your Python file or in the Java file that you’ve already made. Do this by adding a second function/method to your Java/Python file with a slightly different name.


### 3.2. Link to Repo
Please make sure that the new repo that you made today on GitHub is public, and paste a link to it below.

```bash
# paste your new repo link here...
https://github.com/Tangerinedream13/lab03-exercises.git
```

### 3.3. What do the three "Merge pull request" options mean? 
Describe each of them in your own words.
1) Merge Commit: Merge commit is a way to complete version control that allows multiple people to make changes to the code. Unfortunately, it can become messy and cause merge conflicts if different people are making changes. To avoid this, you need to go in and resolve the merge conflict. It does show a history of all the different collaborators, edits that were made and times the changes were made. 

2) Rebase: Rebase is a way to move and combine commits from one branch to another. It keeps commits linear and avoids messy merge commits. Rebasing replays the commits on top of the branch that you're rebasing to. 

3) Squash and merge: Squashing allows you to combine multiple commit messages into one. It helps keep the commit history clear. 
