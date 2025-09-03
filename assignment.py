# 1. Hospital Management System

# Problem Statement: Design a program that allows hospital staff to manage patients and doctors.

# Requirements:

# Patient Class (encapsulated): name, age, ailment.

# Doctor Class: name, specialty.

# Hospital Class:

# Private lists: __patients, __doctors, __appointments.

# Methods: add_patient(), add_doctor(), schedule_appointment(), display_patients(), display_doctors(), display_appointments().
# User Actions:

# Add a patient/doctor.

# Schedule an appointment.

# View records.

# Exit system.
# .
class Patient:
    def __init__(self, name, age, ailment):
        self._name = name
        self._age = age
        self._diagnosis = ailment

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_ailment(self):
        return self._ailment
    def set_name(self, name):
        self._name = name
    def set_age(self, age):
        if age > 0:  
            self._age = age
    def set_ailment(self, ailment):
        self._ailment = ailment
    def __str__(self):
        return f"Patient: {self._name}, Age: {self._age}, Ailment: {self._ailment}"

class Doctor:
    def __init__(self, doctor_name, specialty):
        self._doctor_name = doctor_name
        self._specialty = specialty

    def get_doctor_name(self):
        return self._doctor_name
    def specialty(self):
        return self._specialty
    def set_doctor_name(self):
        return self._doctor_name
    def specialty(self):
        return self.specialty

class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment: {self.patient.get_name()} with Dr. {self.doctor.name} on {self.date_time}"
    
class Hospital:
    def __init__(self):
        self.__patients = []
        self.__doctors = []
        self.__appointments = []

#SOLUTION
class Patient:
    def _init_(self, name, age, ailment):
        self.__name = name          # Encapsulated attributes
        self.__age = age
        self.__ailment = ailment

    def get_info(self):
        return f"Name: {self._name}, Age: {self.age}, Ailment: {self._ailment}"


class Doctor:
    def _init_(self, name, specialty):
        self.__name = name
        self.__specialty = specialty

    def get_info(self):
        return f"Name: {self._name}, Specialty: {self._specialty}"


class Hospital:
    def _init_(self):
        self.__patients = []        # Private lists
        self.__doctors = []
        self.__appointments = []

    def add_patient(self, name, age, ailment):
        patient = Patient(name, age, ailment)
        self.__patients.append(patient)
        print(f"✅ Patient '{name}' added successfully!")

    def add_doctor(self, name, specialty):
        doctor = Doctor(name, specialty)
        self.__doctors.append(doctor)
        print(f"✅ Doctor '{name}' added successfully!")

    def schedule_appointment(self, patient_name, doctor_name, date):
        # Ensure both patient and doctor exist
        patient_exists = any(p.get_info().startswith(f"Name: {patient_name}") for p in self.__patients)
        doctor_exists = any(d.get_info().startswith(f"Name: {doctor_name}") for d in self.__doctors)

        if patient_exists and doctor_exists:
            self.__appointments.append((patient_name, doctor_name, date))
            print(f"✅ Appointment scheduled: {patient_name} with Dr. {doctor_name} on {date}")
        else:
            print("❌ Either patient or doctor not found!")

    def display_patients(self):
        print("\n--- Patients ---")
        if not self.__patients:
            print("No patients found.")
        for p in self.__patients:
            print(p.get_info())

    def display_doctors(self):
        print("\n--- Doctors ---")
        if not self.__doctors:
            print("No doctors found.")
        for d in self.__doctors:
            print(d.get_info())

    def display_appointments(self):
        print("\n--- Appointments ---")
        if not self.__appointments:
            print("No appointments found.")
        for a in self.__appointments:
            print(f"Patient: {a[0]}, Doctor: {a[1]}, Date: {a[2]}")


# ------------------ Main Program ------------------
hospital = Hospital()

while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. View Patients")
    print("5. View Doctors")
    print("6. View Appointments")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        ailment = input("Enter patient ailment: ")
        hospital.add_patient(name, age, ailment)

    elif choice == '2':
        name = input("Enter doctor name: ")
        specialty = input("Enter doctor specialty: ")
        hospital.add_doctor(name, specialty)

    elif choice == '3':
        patient_name = input("Enter patient name: ")
        doctor_name = input("Enter doctor name: ")
        date = input("Enter appointment date: ")
        hospital.schedule_appointment(patient_name, doctor_name, date)

    elif choice == '4':
        hospital.display_patients()

    elif choice == '5':
        hospital.display_doctors()

    elif choice == '6':
        hospital.display_appointments()

    elif choice == '7':
        print("Exiting system. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")