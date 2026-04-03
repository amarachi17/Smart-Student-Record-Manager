# Smart Student Record Manager (CLI)

A command-line application for managing student records with support for CRUD operations, CSV export, and AI-powered natural language search.

## Features

# Core Features
- Add, update, delete student records
- View all students
- Search students by ID
- Persistant data storage using JSON

# Advanced Features
- Export student data to CSV
- AI-powered natural language search:
    - "students above 70"
    - "find blessing"
    - "students below 50"


## Project Structure
student_record_manager/

-- ai_assistant.py
-- main.py
-- student_manager.py
-- storage.py
-- students.json
-- students_export.csv
-- README.md
-- requirements.txt


## Technologies Used
- Python
- JSON (Data storage)
- CSV (Data export)
- CLI (Command-line interface)

## Why This Project?

This project was built to simulate a real-world backend system where data is stored, processed, and retrieved efficiently. It demonstrates modular programming, data handling, and user interaction through CLI.


## Core Architecture

- `main.py` → CLI interface and user interaction  
- `student_manager.py` → CRUD operations  
- `storage.py` → JSON data handling  
- `ai_assistant.py` → intelligent search logic  


## AI Feature

The application includes a smart search assistant that allows users to query student data using natural language.

Example queries:

"students above 70"
"find Alice"
"students below 50"


## Learning Outcomes
- Modular programming
- File handling (JSON & CSV)
- CLI application design
- Data filtering and processing
- Basic AI-like query handling

## Application Status

The application is fully functional and supports user input, data processing, and output generation through a command-line interface.

## Data Handling

- Student data is stored in a JSON file (`students.json`)
- Data is read and written using custom storage functions
- Exported data is saved as CSV (`students_export.csv`)
- The system ensures structured and consistent data storage

## Core Logic Explanation

The application separates concerns for better scalability and maintainability.

## Submission Links

- GitHub Repository: https://github.com/amarachi17/Smart-Student-Record-Manager
- Presentation Slides (PDF): [Included in repository]

## How to Run

```bash
python main.py
```

## Future Improvements
- Convert to Django REST API
- Add authentication
- Deploy as a web app


## Author
Confidence Amarachi Nkeonye