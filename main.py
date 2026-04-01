from student_manager import(
    add_student,
    view_students, 
    search_student,
    update_student,
    delete_student,
    export_to_csv
)

def display_menu():
    print("\n" + "-" * 40)
    print("Student Record Manager")
    print("-" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Export Student to CSV")
    print("7. Exit")
    print("-" * 40)


def main():
    while True: 
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
            
        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            export_to_csv(7)

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select from 1-6.")


if __name__ == "__main__":
    main() 