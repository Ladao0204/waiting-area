import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

# 1. Create Patient Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
''')

# 2. Create Doctor Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT
)
''')

# 3. Create Appointment Table (Links Patients and Doctors)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    app_date TEXT,
    status TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors (doctor_id)
)
''')

conn.commit()
conn.close()
print("Database and tables created successfully!")