## File handeling in python
# Write mode - make a file and overwrite a file
f = open("test.txt","w")
f.write("Hello, Hassan")
f.close()

# Open a file in read mode
f = open("test.txt","r")
content = f.read()
print(content)
f.close()

# Append mode - add something in existing file
f = open("test.txt","a")
f.write("\nNew line added.")
f.close()

# Again open a file in read mode to check appending is done or not
f = open("test.txt","r")
content = f.read()
print(content)
f.close()

## New Professional way to do this because this is old and boring way
# with statement close the file automatically 
with open("test.txt","w") as f:
    f.write("Hello, Hassan file\n")
    f.write("AI Automation Engineer\n")

with open("test.txt","r") as f:
    content = f.read()
    print(content)

with open("test.txt","a") as f:
    f.write("This is the append case.61-81")

with open("test.txt","r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("test.txt","r") as f:
    for line in f:
        print(line.strip())

## Lets discuss about JSON file
import json
# Python Dictionary ---> JSON file
student_data = {
    "name":"Hassan",
    "roll_no":"CS-01",
    "marks":{
        "Math":85,
        "OOP":91,
        "Physics":72
    },
    "grade":"B"
}
# SAVE the file
with open("student.json","w") as f:
    json.dump(student_data,f,indent=4)
print("JSON file is saved.")

# Again load the file
with open("student.json","r") as f:
    loaded_data = json.load(f)
print(loaded_data['name'])
print(loaded_data['marks']['OOP'])