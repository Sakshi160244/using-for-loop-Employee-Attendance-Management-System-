# using-for-loop-Employee-Attendance-Management-System-
Employee Attendance Management System is a Python project that records employees' check-in and check-out times to determine attendance status such as Present, Absent, Overtime, Half Day, or Short Day. It processes multiple records, counts each attendance type, and displays a summary report using loops and conditional statements.
# Employee Attendance Management System

## Introduction

The Employee Attendance Management System is a Python application designed to automate attendance tracking based on employee check-in and check-out times. The system evaluates attendance records using predefined business rules and classifies each employee into one of the following categories: **Present**, **Overtime**, **Half Day**, **Short Day**, or **Absent**.

This project demonstrates core Python programming concepts by implementing a rule-based attendance evaluation system with automated summary reporting.

---

## Key Features

* Automated attendance classification
* Check-in and check-out time validation
* Overtime detection
* Half-day and short-day identification
* Attendance summary generation
* Support for processing multiple employee records
* Clean and modular program flow

---

## Technology Stack

* **Language:** Python 3
* **Concepts Used:**

  * Variables
  * User Input
  * Conditional Statements (`if`, `elif`, `else`)
  * Loops (`for`)
  * Counters
  * Logical Operators

---

## Project Structure

```text
employee-attendance-management/
├── attendance.py
└── README.md
```

---

## Attendance Classification Rules

| Check-In                         | Check-Out | Status   |
| -------------------------------- | --------- | -------- |
| ≤ 08:00                          | 18:00     | Present  |
| ≤ 08:00                          | > 18:00   | Overtime |
| ≤ 08:00 & 13:00 or 13:00 & 18:00 | Half Day  |          |
| Late arrival or early departure  | Short Day |          |
| Invalid attendance record        | Absent    |          |

---

## Getting Started

### Prerequisites

* Python 3.x installed on your system

### Installation

```bash
git clone https://github.com/your-username/employee-attendance-management.git
cd employee-attendance-management
```

### Run the Application

```bash
python attendance.py
```

---

## Sample Output

```text
Employee 1

Enter Morning Time: 8
Enter Evening Time: 18

Present

Attendance Summary

Total Present   : 1
Total Overtime  : 0
Total Half Day  : 0
Total Short Day : 0
Total Absent    : 0
```

---

## Learning Objectives

This project demonstrates practical implementation of:

* Rule-based decision making
* Control flow using conditional statements
* Iterative processing with loops
* Counter-based data aggregation
* Console-based application development
* Basic business logic implementation

---

## Future Improvements

* Employee ID and Name Management
* CSV/Excel File Support
* Attendance History
* Monthly Report Generation
* Salary Calculation Based on Attendance
* Database Integration (SQLite/MySQL)
* Graphical User Interface (Tkinter/PyQt)
* Object-Oriented Architecture

---

## License

This project is intended for educational and learning purposes.

---

## Author

**Sakshi Panchal**

Aspiring Data Analyst skilled in Python, SQL, Excel, Power BI, and Data Analytics.

