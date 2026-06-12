# Student Management System

A robust, Object-Oriented Python application for managing student records. This mini-project demonstrates core OOP principles (Inheritance, Encapsulation, Polymorphism) and essential File I/O operations.

## Features

* **Add Students**: Add new student profiles to the system with automatic GPA validation (must be between 0 and 4.0).
* **View Students**: Display the list of all students. Supports multi-criteria sorting:
  * Increasing order (by GPA -> Name -> Age)
  * Decreasing order (by GPA -> Name -> Age)
* **Search & Delete**: Easily find or remove specific students from the system by their name.
* **File I/O Integration**: 
  * Load student records from a formatted text file (CSV style). Includes error handling to skip invalid data formats.
  * Save and export the current list of students to a text file.

## System Architecture

The project is built around three main classes:

1. `Person` (Base Class): Represents a generic person with `name` and `age` attributes.
2. `Student` (Derived Class): Inherits from `Person` and introduces student-specific attributes like `gpa` and a class-level attribute `school`. Includes static methods for data validation.
3. `Manager` (Controller Class): Acts as the main engine to store the list of students (`self.students`) and handles all business logic, including CRUD operations and File I/O.

## Data Format

When loading from or saving to a text file, the system expects and generates data in the following format:
`"Name", Age, GPA`

*Example (`input.txt`):*
```text
"Long", 19, 4.0
"Vinh", 18, 3.6
"Lam", 18, 3.2

