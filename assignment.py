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
    def __init__(self, ward_name):
        self._ward_name = ward_name

def __init__(self, hospital_name):
    self.__patients = []  
