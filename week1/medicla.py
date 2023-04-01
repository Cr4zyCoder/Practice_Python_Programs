# care hospital wants to know the medical speciability visited the pateient is stored in a list. The details of
# the medical speciabilities are stored in a dictionary as follows:
# {"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
# write a function to find the medical speciality visited by the maximum number of pateints and return the name of the
# speciality.
# Note: 1. Assume that there is always only one medical specilaity which is visited by maximum number of pateints.
# 2. Perform case sensitive string comparision wherever necessary
def find_max_specialty(specialties):
    
    specialty_dict = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}

    #  dictionary to store the counts 
    count_dict = {"Pediatrics": 0, "Orthopedics": 0, "ENT": 0}

    # Iterate and update over the specialties 
    for specialty in specialties:
        count_dict[specialty_dict[specialty]] += 1

    # maximum count speciality
    max_count = max(count_dict.values())
    max_specialty = [key for key, value in count_dict.items() if value == max_count][0]
    print(max_specialty)


specialties = ["P", "O", "O", "E", "P", "P", "O", "P", "E", "P", "O", "O", "O", "E", "P"]
#specialties=[101,'P',102,'O',302,'P',305,'P']
max_specialty = find_max_specialty(specialties)
