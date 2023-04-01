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

""" travel_log = [
    {
        "country": "France",
        "country": "France",
        "cities": ["paris", 'little', 'dijon'],
        "total_visits":12
    },
    {
        "country": "France",
        "country": "France",
        "cities": ["paris", 'little', 'dijon'],
        "total_visits":12
    }
] """


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities

    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
