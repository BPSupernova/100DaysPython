first_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(first_dictionary["Bug"]) # Prints the value associated with the key "Bug"

# Adding a new item to a dictionary
first_dictionary["Awesomeness"] = "A feeling that is just pure awesome."

# Redefining an item in a dictionary
first_dictionary["Bug"] = "A moth in your computer" # Redefines the "Bug" item

# Loop through a dictionary to get the keys
for key in first_dictionary:
    print(key) # Prints key
    print(first_dictionary[key]) # Prints the value

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
}

# Nesting a List in a List
wierd_alphabet = ["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary
travel_log_deluxe = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]}
}

# Nesting a Dictionary in a List
travel_log_super_deluxe = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 2
    },
    {
        "country": "India", 
        "cities_visited": ["Mumbai", "New Delhi"], 
        "total_visits": 3
    },
]