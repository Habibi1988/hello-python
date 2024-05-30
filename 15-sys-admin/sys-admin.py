import os
import subprocess

# Exercise 1: Using os.system() to list directory contents
os.system("dir")

# Exercise 2: Using subprocess.run() to list directory contents
subprocess.run(["cmd", "/c", "dir"])

# Exercise 3: Using subprocess.run() with two arguments
subprocess.run(["cmd", "/c", "dir", "/w"])

# Exercise 4: Using subprocess.run() to display contents of README.md
subprocess.run(["cmd", "/c", "type", "README.md"])

# Exercise 5: Retrieving system information
command = "systeminfo"
print(f'Gathering system information with command: {command}')
subprocess.run(["cmd", "/c", command])

# Exercise 6: Retrieving information about active processes
command = "tasklist"
print(f'Gathering active process information with command: {command}')
subprocess.run(["cmd", "/c", command])
