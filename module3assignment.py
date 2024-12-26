import os
def list_directory_contents(path):
    with open(path, 'r') as file:
        for line in file:
            print(line)


list_directory_contents("tools.txt")