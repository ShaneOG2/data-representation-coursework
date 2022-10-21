# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.

from github import Github 
from config import config

# Get github key from config
gitHubKey = config['gitHubKey']
g = Github(gitHubKey)

# Get my repo
repo = g.get_repo("ShaneOG2/data-representation-coursework")

# Get the contents of assignment04-file.txt
fileContent = repo.get_contents("assignment04-file.txt")

# Decode the contents
fileContentDecoded = fileContent.decoded_content.decode() # https://stackoverflow.com/a/64739176

# Convert text to lower and replace andrew with Shane
fileContentDecoded = fileContentDecoded.lower()
fileContentDecoded = fileContentDecoded.replace("andrew", "Shane")

# Update and commit to github 
gitHubResponse = repo.update_file(fileContent.path, "Updated by programme", fileContentDecoded, fileContent.sha)