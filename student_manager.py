import csv
from storage import load_students, save_students

# Add Student

def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ").strip()

    # Check for duplicate ID 
    for student in students:
        if student["id"] == student_id:
            print("❌ Student ID already exists.")
            return
        
    name = input("Enter Student Name: ").strip()

    try:
        age = int(input("Enter Student Age: "))
        score = float(input("Enter Student Score: "))
    except ValueError:
        print("❌ Invalid input. Age must be a number, score must be numeric.")
        return
    
    new_student = {
        "id": student_id,
        "name": name, 
        "age": age,
        "score": score
    }
    
    students.append(new_student)
    save_students(students)

    print("✅ Student added successfully.")

# View All Students

def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return
    
    print("\n Student List:")
    for student in students:
        print(f"{student['id']} | {student['name']} | Age: {student['age']} | Score: {student['score']} ")


# Search Student by ID 

def search_student():
    students = load_students()

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\n ✅ Student Found: ")
            print(student)
            return
    
    print("❌ Student not found.")


# Update Student

def update_student(): 
    students = load_students()

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Leave blank to keep current value.")

            name = input(f"Name ({student['name']}): ").strip()
            age = input(f"Age ({student['age']}): ").strip()
            score = input(f"Score ({student['score']}): ").strip()

            if name:
                student["name"] = name

            if age:
                try:
                    student["age"] = int(age)
                except ValueError:
                    print("❌ Invalid age input.")
                    return
            
            if score: 
                try:
                    student["score"] = float(score)
                except ValueError:
                    print("❌ Invalid score input.")
                    return
            
            save_students(students)
            print("✅ Student updated successfully.")
            return
    
    print("❌ Student not found.")


# Delete Student

def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")

    print("❌ Student not found.")


# Export Students to CSV

def export_to_csv():
    students = load_students()

    if not students:
        print("No students to export.")
        return

    file_name = "students_export.csv"

    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow(["ID", "Name", "Age", "Score"])

            # Write student data 
            for student in students:
                writer.writerow([
                    student["id"],
                    student["name"],
                    student["age"],
                    student["score"]
                ]) 
        print(f"Students exported successfully to {file_name}")

    except Exception as e:
        print(f"❌ Error exporting file: {e}")