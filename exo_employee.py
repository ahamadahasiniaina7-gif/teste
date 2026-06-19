class Employee:
    def __init__(self, id, nom, poste, salaire):
        self.id = id
        self.nom = nom
        self.poste = poste
        self.salaire = salaire

    def display_info(self):
        print(f"ID : {self.id}")
        print(f"Nom : {self.nom}")
        print(f"Poste : {self.poste}")
        print(f"Salaire : {self.salaire:,} Ar")

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "poste": self.poste,
            "salaire": self.salaire
        }


# Exemple d'utilisation
employe1 = Employee(1, "Jean", "Développeur", 1500000)

employe1.display_info()

# Conversion en dictionnaire
print("\nDictionnaire :")
print(employe1.to_dict())

#exercice 2
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} ajouté.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee} supprimé.")
        else:
            print("Employé non trouvé.")

    def find_employee(self, employee):
        if employee in self.employees:
            print(f"{employee} trouvé.")
            return True
        else:
            print(f"{employee} non trouvé.")
            return False

    def display_all(self):
        if not self.employees:
            print("Aucun employé.")
        else:
            print("Liste des employés :")
            for employee in self.employees:
                print(employee)


# Exemple d'utilisation
manager = EmployeeManager()

manager.add_employee("Alice")
manager.add_employee("Bob")

manager.display_all()

manager.find_employee("Alice")

manager.remove_employee("Bob")

manager.display_all()

#exercice 3
import json

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [
            emp for emp in self.employees
            if emp["id"] != employee_id
        ]

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp["id"] == employee_id:
                return emp
        return None

    def display_all(self):
        for emp in self.employees:
            print(emp)

    def save_to_json(self):
        with open("employees.json", "w", encoding="utf-8") as file:
            json.dump(self.employees, file, ensure_ascii=False, indent=4)