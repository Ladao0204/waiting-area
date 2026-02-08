import sqlite3

def add_patient(name, phone, email):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Patients (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print(f"Patient {name} added!")

# Example usage:
add_patient("John Doe", "555-0199", "john@example.com")