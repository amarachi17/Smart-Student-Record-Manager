from storage import load_students

def ai_search():
    students = load_students()

    if not students:
        print("No students available.")
        return
    
    query = input("Enter your search query: ").lower()

    results = []

    # Search by name 
    for student in students:
        if student["name"].lower() in query:
            results.append(student)

    # Score conditions
    if "above" in query:
        try:
            value = int(query.split("above")[1].strip())
            results = [s for s in students if s["score"] > value]
        except:
            print("❌ Could not understand score condition.")

    elif "below" in query:
        try:
            value = int(query.split("below")[1].strip())
            results = [s for s in students if s["score"] < value]
        except:
            print("❌ Could not understand score condition.")

    elif "equal" in query or "equals" in query:
        try: 
            value = int(query.split()[-1])
            results = [s for s in students if s["score"] == value]
        except:
            print("❌ Could not understand score condition.")

    # Show results
    if results:
        print("\n Results:")
        for s in results:
            print(f"{s['id']} | {s['name']} | Age: {s['age']} | Score: {s['score']}")

    else:
        print("❌ No matching students found.")