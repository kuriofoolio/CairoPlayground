
#!/bin/bash

# Navigate to the directory containing your local Git repository
cd "$(dirname "$0")"

#variables
$branch='main'

#start up web server
# xdg-open "http://localhost:5500"

#run script for committing to git
# ./myscript.sh

# Run file for extracting words
# node js/extract_words.js


# Add all changes to the Git staging area
git add .

#check status of files to be committed
git status

# Commit the changes with a descriptive message
git commit -m "added all files"

# Push the changes to your GitHub repository
git push origin $branch
