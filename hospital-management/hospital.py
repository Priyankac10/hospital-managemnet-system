class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

    def details(self):
        return f"Patient: {self.name}, Age: {self.age}, Ailment: {self.ailment}"

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def details(self):
        return f"Doctor: {self.name}, Specialty: {self.specialty}"

def main():
    # Sample patient
    patient = Patient("John Doe", 30, "Flu")
    print(patient.details())

    # Sample doctor
    doctor = Doctor("Dr. Smith", "Pediatrics")
    print(doctor.details())

if __name__ == "__main__":
    main()
 
if __name__ == "__main__":
    main()
 