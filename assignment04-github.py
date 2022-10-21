# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.
# I do not need to see your keys
# (see lab2, to follow)
# Handup: Save the program as assignment04-github.py to the same repository you uploaded the xml to
# Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.

from github import Github 
from config import config
import requests

gitHubKey = config['gitHubKey']
g = Github(gitHubKey)

repo = g.get_repo("ShaneOG2/data-representation-coursework")

fileContent = repo.get_contents("assignment04-file.txt")

print(fileContent.decoded_content.decode())
