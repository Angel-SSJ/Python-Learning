import os


# Create a directory
# If Directory exists already then it will raise an error
os.mkdir('new_directory')
os.mkdir('new_directory_testing')
# Rename a file
# If File does not exist then it will raise an error
os.rename('old_directory', 'new_directory')


# Delete a file
# If File does not exist then it will raise an error
os.remove('new_directory_testing')

# Get the current working directory
cwd = os.getcwd()
