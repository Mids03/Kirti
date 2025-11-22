# Academic Task Manager (ATM)

## Overview
The Academic Task Manager (ATM) is a command-line interface (CLI) application designed to help students manage their academic workload efficiently. [cite_start]It allows users to register, manage tasks with priorities, and view productivity analytics to track their progress[cite: 90].

## Features
* [cite_start]**User Authentication:** Secure registration and login with password hashing.
* [cite_start]**Task Management:** Full Create, Read, Update, and Delete (CRUD) capabilities for academic tasks[cite: 29].
* [cite_start]**Productivity Analytics:** Generates a statistical report of completed vs. pending tasks[cite: 28].
* [cite_start]**Data Persistence:** Automatically saves all data to a local JSON file, ensuring no data loss.

## Technologies Used
* **Language:** Python 3.x
* **Data Storage:** JSON (Flat file storage)
* **Security:** Hashlib (SHA-256 encryption)
* **Logging:** Python Logging Module

## Installation & Execution
1.  Ensure Python 3.x is installed on your system.
2.  Download `project_main.py` to a local directory.
3.  Open a terminal/command prompt in that directory.
4.  Run the application:
    ```bash
    python project_main.py
    ```

## Instructions for Testing
1.  **Register:** Select option 1 and create a user. Try creating a password shorter than 4 characters to test validation.
2.  **Login:** Use your new credentials to log in.
3.  **Add Tasks:** Add 2-3 tasks with different priorities.
4.  **Analytics:** Select "View Analytics Report" to see your efficiency score.
5.  **Persistence:** Close the app and restart it. Log in again to verify your tasks are still there.