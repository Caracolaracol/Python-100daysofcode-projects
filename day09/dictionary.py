programming_dictionary = {
    "bug": "an error in a program",
    "anotherword" :"another definition",
    "asd": "asdsad"
}

programming_dictionary["bug"] # gives the value of bug
programming_dictionary["Loop"] = "The action of doing something over and over again" # adding new items to dictionary

#wipe an existing dictionary
# programming_dictionary = {}

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key]) 
