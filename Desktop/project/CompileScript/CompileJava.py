import os
import subprocess
path = "src/"
src = ""
for file in os.listdir(path):
    if file.endswith(".java"):
        src = src+(path+file+" ")
print(src)
out = "output/"
str_command = "javac -cp `hadoop classpath` -d "+out+" "+src

command = str_command  # the shell command

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

print output[0]
