from fpdf import FPDF
import datetime

# --- CONTENT CONFIGURATION ---
PROJECT_TITLE = "Academic Task Manager (ATM)"
STUDENT_NAME = "Your Name"  # <--- CHANGE THIS
REG_NUMBER = "Reg No: 123456" # <--- CHANGE THIS
COURSE_NAME = "Software Development Project"

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, PROJECT_TITLE, 0, 1, 'R')
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

    def add_section(self, title, body):
        self.chapter_title(title)
        self.chapter_body(body)

# Create PDF object
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()

# --- 1. COVER PAGE [cite: 112] ---
pdf.set_font('Arial', 'B', 24)
pdf.ln(60)
pdf.cell(0, 10, PROJECT_TITLE, 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Arial', '', 16)
pdf.cell(0, 10, "Project Report", 0, 1, 'C')
pdf.ln(10)
pdf.cell(0, 10, f"Submitted by: {STUDENT_NAME}", 0, 1, 'C')
pdf.cell(0, 10, f"{REG_NUMBER}", 0, 1, 'C')
pdf.ln(10)
pdf.cell(0, 10, f"Course: {COURSE_NAME}", 0, 1, 'C')
pdf.cell(0, 10, f"Date: {datetime.date.today()}", 0, 1, 'C')
pdf.add_page()

# --- 2. INTRODUCTION [cite: 113] ---
intro_text = (
    "The Academic Task Manager (ATM) is a Python-based Command Line Interface (CLI) application "
    "designed to help students manage their academic workload. In the modern educational environment, "
    "students face multiple deadlines, assignments, and projects. This system allows users to "
    "register, login, and track their tasks efficiently using a local persistent database. "
    "The project demonstrates core programming concepts including Object-Oriented Programming, "
    "File Handling (JSON), and Security (Hashing)."
)
pdf.add_section("1. Introduction", intro_text)

# --- 3. PROBLEM STATEMENT [cite: 114] ---
prob_text = (
    "Students often struggle to keep track of assignments and project deadlines because they are "
    "scattered across different portals or written in physical notebooks. Existing digital tools "
    "are often too complex, require paid subscriptions, or need constant internet access. "
    "There is a need for a lightweight, offline-capable, and secure tool to centralize academic "
    "tasks and monitor productivity efficiency."
)
pdf.add_section("2. Problem Statement", prob_text)

# --- 4. FUNCTIONAL REQUIREMENTS [cite: 115] ---
func_reqs = (
    "The system implements the following core functional modules:\n\n"
    "1. User Authentication Module:\n"
    "   - User Registration with username/password validation.\n"
    "   - Secure Login verification.\n"
    "   - Session management (Logout).\n\n"
    "2. Task Management Module (CRUD):\n"
    "   - Create: Add new tasks with Title, Description, and Priority.\n"
    "   - Read: View a list of all tasks filtered by the logged-in user.\n"
    "   - Update: Change task status (Pending -> Completed).\n"
    "   - Delete: Remove tasks permanently.\n\n"
    "3. Analytics Module:\n"
    "   - Calculate total tasks, completed tasks, and pending tasks.\n"
    "   - Display an efficiency percentage to the user."
)
pdf.add_section("3. Functional Requirements", func_reqs)

# --- 5. NON-FUNCTIONAL REQUIREMENTS [cite: 116] ---
non_func_reqs = (
    "1. Security: Passwords are not stored in plain text. SHA-256 hashing is used to encrypt "
    "credentials before storage.\n"
    "2. Persistence/Reliability: Data is saved to a local 'app_data.json' file immediately after "
    "every modification, ensuring no data loss upon exit.\n"
    "3. Error Handling: The system uses try-except blocks to handle invalid inputs (e.g. integers vs strings) "
    "and file access errors gracefully.\n"
    "4. Logging: Operational events (logins, errors, data updates) are written to 'app.log' for auditing."
)
pdf.add_section("4. Non-functional Requirements", non_func_reqs)

# --- 6. SYSTEM ARCHITECTURE [cite: 117] ---
arch_text = (
    "The project follows a Modular Monolithic Architecture suitable for a standalone Python application.\n"
    "- Presentation Layer: The 'Application' class handles the CLI loop and user inputs.\n"
    "- Logic Layer: 'UserManager', 'TaskManager', and 'AnalyticsEngine' classes contain business logic.\n"
    "- Data Layer: 'DataManager' class handles File I/O with the JSON storage.\n"
    "- Security Layer: 'SecurityService' class handles hashing algorithms."
)
pdf.add_section("5. System Architecture", arch_text)

# --- 7. DESIGN DIAGRAMS [cite: 118-123] ---
# Note: Since we are generating a PDF via script, we will describe the diagrams.
# In a real submission, you would paste images here.
diagrams_text = (
    "[NOTE: In a full manual submission, paste screenshots here. Descriptions provided below]\n\n"
    "A. Use Case Diagram:\n"
    "Actor: Student -> Uses Cases: Register, Login, Create Task, View Tasks, Update Status, Delete Task, View Report.\n\n"
    "B. Class Diagram:\n"
    "Classes defined: Application, UserManager, TaskManager, DataManager, SecurityService.\n"
    "Relationships: Application composes Manager classes. Managers use DataManager.\n\n"
    "C. Workflow Diagram:\n"
    "Start -> Auth Menu -> (Login/Register) -> Dashboard -> Select Action -> (CRUD/Analytics) -> Save Data -> Logout."
)
pdf.add_section("6. Design Diagrams", diagrams_text)

# --- 8. DESIGN DECISIONS & RATIONALE [cite: 124] ---
design_decisions = (
    "- Storage: JSON was chosen over SQL because it is lightweight, portable, and requires no "
    "external database server installation, making it perfect for a personal academic project.\n"
    "- Hashing: SHA-256 was chosen for password security as it is a standard industry algorithm "
    "available in Python's native libraries.\n"
    "- CLI Interface: Chosen to minimize resource usage and focus on logic implementation rather than UI design."
)
pdf.add_section("7. Design Decisions & Rationale", design_decisions)

# --- 9. IMPLEMENTATION DETAILS [cite: 125] ---
imp_details = (
    "The application is implemented in a single modular Python file 'project_main.py'.\n"
    "- Libraries used: 'json' (storage), 'os' (file checks), 'hashlib' (security), 'datetime' (timestamps), 'logging' (audit).\n"
    "- Data Structure: A dictionary containing two lists: {'users': [], 'tasks': []}.\n"
    "- The main loop runs continuously until the user selects 'Exit'."
)
pdf.add_section("8. Implementation Details", imp_details)

# --- 10. SCREENSHOTS / RESULTS [cite: 126] ---
screen_text = (
    "(Run the code and take screenshots of the console to insert here)\n\n"
    "1. Registration Success Message\n"
    "2. The Task Dashboard showing a list of tasks\n"
    "3. The Analytics Report output"
)
pdf.add_section("9. Screenshots / Results", screen_text)

# --- 11. TESTING APPROACH [cite: 127] ---
test_text = (
    "1. Unit Testing: Individual functions (hashing, file loading) were tested in isolation.\n"
    "2. Input Validation Testing: Verified that entering text into numeric fields does not crash the app.\n"
    "3. Integration Testing: Verified that a new user can register, login immediately, and see an empty task list unique to them."
)
pdf.add_section("10. Testing Approach", test_text)

# --- 12. CHALLENGES FACED [cite: 128] ---
challenge_text = (
    "- Data Persistence: Initially, the program overwrote data on every run. This was solved by creating a "
    "'load_data' method that checks if the file exists before initializing.\n"
    "- JSON Errors: If the file was empty, the JSON parser crashed. A try-except block was added to handle empty files."
)
pdf.add_section("11. Challenges Faced", challenge_text)

# --- 13. LEARNINGS & KEY TAKEAWAYS [cite: 129] ---
learnings = (
    "- Gained deep understanding of Python Classes and Objects.\n"
    "- Learned how to implement basic authentication and security practices.\n"
    "- Understood the importance of Modular Architecture for code maintenance.\n"
    "- Mastered file handling and JSON data serialization."
)
pdf.add_section("12. Learnings & Key Takeaways", learnings)

# --- 14. FUTURE ENHANCEMENTS [cite: 130] ---
future = (
    "- Graphical User Interface (GUI): Port the logic to Tkinter or PyQt.\n"
    "- Cloud Sync: Store data in Firebase or a remote SQL database.\n"
    "- Notifications: Add reminders for high-priority tasks near their deadline."
)
pdf.add_section("13. Future Enhancements", future)

# --- 15. REFERENCES [cite: 131] ---
refs = (
    "- Python 3 Documentation: https://docs.python.org/3/\n"
    "- Course Syllabus and Lecture Notes on Object Oriented Programming.\n"
    "- Tutorials on SHA-256 hashing implementation."
)
pdf.add_section("14. References", refs)

# Output the PDF
pdf.output("Project_Report.pdf")
print("PDF Generated Successfully: 'Project_Report.pdf'")