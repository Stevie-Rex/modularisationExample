from person import Person

def main():
    # Create a list of Person objects
    people = [Person("Alice", 25, 'F'), Person("Bob", 30, 'M'), Person("Charlie", 35, 'M')]

    # Use a loop to print out the details of each person
    for p in people:
        print(p.getName() + " is " + str(p.getAge()) + " years old and " + p.getGender())

# Call the main function
if __name__ == "__main__":
    main()
