import datetime
import random

class Doctor:
    def __init__(self, doc_id, name, specialization):
        self.doc_id = doc_id
        self.name = name
        self.specialization = specialization
        # Dictionary to store appointments: { "date": ["10:00", "11:00"] }
        self.booked_slots = {} 

    def is_available(self, date, time):
        """Check if a specific slot is free."""
        if date in self.booked_slots:
            if time in self.booked_slots[date]:
                return False
        return True

    def book_slot(self, date, time):
        """Reserve a slot."""
        if date not in self.booked_slots:
            self.booked_slots[date] = []
        self.booked_slots[date].append(time)

class Patient:
    def __init__(self, p_id, name, age, contact):
        self.p_id = p_id
        self.name = name
        self.age = age
        self.contact = contact

class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.id = random.randint(1000, 9999)
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

class HospitalSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []
        # Seeding some dummy data
        self._seed_data()

    def _seed_data(self):
        self.doctors.append(Doctor(1, "Dr. Sarah Smith", "Cardiology"))
        self.doctors.append(Doctor(2, "Dr. John Doe", "Dermatology"))
        self.doctors.append(Doctor(3, "Dr. Emily Chen", "Pediatrics"))

    def find_doctor(self, doc_id):
        for doc in self.doctors:
            if doc.doc_id == doc_id:
                return doc
        return None

    def register_patient(self):
        print("\n--- Patient Registration ---")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        contact = input("Enter Contact Number: ")
        p_id = len(self.patients) + 1
        new_patient = Patient(p_id, name, age, contact)
        self.patients.append(new_patient)
        print(f"Patient Registered Successfully! ID: {p_id}")
        return new_patient

    def show_doctors(self):
        print("\n--- Available Doctors ---")
        print(f"{'ID':<5} {'Name':<20} {'Specialization'}")
        print("-" * 40)
        for doc in self.doctors:
            print(f"{doc.doc_id:<5} {doc.name:<20} {doc.specialization}")

    def book_appointment(self):
        print("\n--- Book Appointment ---")
        # 1. Identify Patient
        # For simplicity, we register a new patient every time in this demo, 
        # but in a real app, you would search for an existing ID.
        patient = self.register_patient()

        # 2. Select Doctor
        self.show_doctors()
        try:
            doc_id = int(input("\nEnter Doctor ID to book: "))
        except ValueError:
            print("Invalid ID format.")
            return

        doctor = self.find_doctor(doc_id)
        if not doctor:
            print("Doctor not found.")
            return

        # 3. Select Time
        date = input("Enter Date (YYYY-MM-DD): ")
        time = input("Enter Time (e.g., 10:00 AM): ")

        # 4. Check Availability
        if doctor.is_available(date, time):
            doctor.book_slot(date, time)
            appt = Appointment(doctor, patient, date, time)
            self.appointments.append(appt)
            print(f"\nSuccess! Appointment confirmed with {doctor.name} on {date} at {time}.")
            print(f"Appointment ID: {appt.id}")
        else:
            print(f"\nError: {doctor.name} is already booked at that time.")

    def view_appointments(self):
        print("\n--- All Scheduled Appointments ---")
        if not self.appointments:
            print("No appointments scheduled yet.")
        else:
            for appt in self.appointments:
                print(f"ID: {appt.id} | Dr. {appt.doctor.name} <-> {appt.patient.name} | {appt.date} @ {appt.time}")

    def run(self):
        while True:
            print("\n" + "="*30)
            print(" HOSPITAL MANAGEMENT SYSTEM")
            print("="*30)
            print("1. View Doctors")
            print("2. Book Appointment")
            print("3. View All Appointments")
            print("4. Exit")
            
            choice = input("Enter choice: ")

            if choice == '1':
                self.show_doctors()
            elif choice == '2':
                self.book_appointment()
            elif choice == '3':
                self.view_appointments()
            elif choice == '4':
                print("System Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = HospitalSystem()
    system.run()
