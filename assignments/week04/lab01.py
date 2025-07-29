"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
def personal_info_manager():
    # Create initial person tuple
    person = ("Ashif", 19, "chonburi", "Thailand")  # name, age, city, country
    hobbies = ["Badminton"]

    while True:

        print("--- Option ---\n")
        print("1.Display all information\n")
        print("2.Add new hobbies\n")
        print("3.Remove hobbies\n")
        print("4.Update age\n")
        print("5.Exit\n")
        choice = input("Choose option: ")

        if choice == "1":
            print("----- Personal Info -----\n")
            print("Name: ", person[0])
            print("Age: ", person[1])
            print("City: ", person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)

        if choice == "2":
            hobby = input("What is your hobby?: ")
            hobbies.append(hobby)

        if choice == "3":
            del hobbies[0]

        if choice == "4":
            person_list = list(person)
            age = int(input("How old are you?: "))
            person_list[1] = age
            person = tuple(person_list)
        if choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()