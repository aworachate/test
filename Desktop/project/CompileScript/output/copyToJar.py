import os
import subprocess
path = "org/apache/hadoop/mapreduce/v2/app/speculate/"
flie_list = ""
for file in os.listdir(path):
    if file.endswith(".class"):
        temp = file.replace("$", "\\$")
        flie_list = flie_list+(path+temp+" ")
print(flie_list)
out = "$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-app-2.7.1.jar"
str_command="jar -uf "+out+" "+flie_list
#str_command = "javac -cp `hadoop classpath` -d "+out+" "+src

command = str_command  # the shell command

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
output = process.communicate()

print output[0]
