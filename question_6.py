# Dictionaries
cutoffs_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "MnC", 318),
    ("Pilani", "ECE", 314),
    ("Pilani", "EEE", 292),
    ("Pilani", "EnI", 282),
    ("Pilani", "Mech", 266),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Civil", 238),
    ("Pilani", "Manufacturing", 243),
    ("Pilani", "Pharma", 165),
    ("Pilani", "Eco", 271),
    ("Pilani", "BioSci", 236),
    ("Pilani", "Math", 256),
    ("Pilani", "Phy", 254),
    ("Pilani", "Chem", 241),
    ("Goa", "Chemical", 239),
    ("Goa", "EEE", 278),
    ("Goa", "Mech", 254),
    ("Goa", "CS", 301),
    ("Goa", "EnI", 270),
    ("Goa", "ECE", 287),
    ("Goa", "MnC", 295),
    ("Goa", "BioSci", 234),
    ("Goa", "Chem", 236),
    ("Goa", "Eco", 263),
    ("Goa", "Math", 249),
    ("Goa", "Phy", 248),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Bio", 234),
    ("Hyderabad", "ECE", 284),
    ("Hyderabad", "EEE", 275),
    ("Hyderabad", "EnI", 270),
    ("Hyderabad", "Mech", 251),
    ("Hyderabad", "Civil", 235),
    ("Hyderabad", "MnC", 293),
    ("Hyderabad", "Pharma", 161),
    ("Hyderabad", "Chem", 235),
    ("Hyderabad", "Math", 247),
    ("Hyderabad", "Phy", 245)
]   # Creating a list of tuples containing data of BITSAT'24 cutoffs

cutoffs_dict = {} # Creating an empty dictionary to store the data in

for campus, course, marks in cutoffs_list: # Checks through elements in list
    if campus not in cutoffs_dict: # If new campus is found in list
        cutoffs_dict[campus] = {}   # Creates an inner/nested dictionary for courses of that campus
    cutoffs_dict[campus][course] = marks # Associates cutoff marks of the course key (in nested dictionary) within the campus key of the original dictionary

for campus, courses in cutoffs_dict.items(): #Checks through elements in the dictionary
    print(f'"{campus}": {courses},') #P
    print("")
