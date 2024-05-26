from helpers import retrieve_students, add_student, delete_student

def main():
    while True:
        print("\nStudent Management CLI")
        print("1. Retrieve all students")
        print("2. Add a new student")
        print("3. Delete a student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            retrieve_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()