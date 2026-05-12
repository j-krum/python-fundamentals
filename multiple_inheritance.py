# multiple_inheritance.py
"""This is an exercise about multiple inheritance"""


class Person:

    def __init__(self, ur: int, id: int, name: str, email: str, celphone: int):
        """This is the Mother class:

        Args:
            ur (string): University Register
            id (int): identity number
            nome (str): name of the person
            email (string): e-mail of the person
            celphone (int): person celphone number
        """
        self.__ur = ur
        self.__id = id
        self.__name = name
        self.__email = email
        self.__celphone = celphone

    @property
    def ur(self):
        return self.__ur

    @ur.setter
    def ur(self, ur):
        self.__ur = ur

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def celphone(self):
        return self.__celphone

    @celphone.setter
    def celphone(self, celphone):
        self.__celphone = celphone

    def login(self):
        return "Login succeded."

    def request(self):
        return "Request successfully completed."

    def __str__(self) -> str:
        return f"Person: {self.name} | Email: {self.email}"


class Student(Person):
    def __init__(self, ur, id, name, email, celphone, matricule):
        super().__init__(ur, id, name, email, celphone)
        self.__matricule = matricule

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, matricule):
        self.__matricule = matricule

    def do_exam(self):
        return "Exam done."

    def __str__(self) -> str:
        return f"Person: {self.name} | Email: {self.email}"


class Professor(Person):
    def __init__(self, ur, id, name, email, celphone, department):
        super().__init__(ur, id, name, email, celphone)
        self.__department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

    def teach_class(self):
        return "Class teached."

    def __str__(self) -> str:
        return f"Person: {self.name} | Email: {self.email}"


class Tutor(Person):
    def __init__(self, ur, id, name, email, celphone, formation):
        super().__init__(ur, id, name, email, celphone)
        self.__formation = formation

    @property
    def formation(self):
        return self.__formation

    @formation.setter
    def formation(self, formation):
        self.__formation = formation

    def correct_test(self):
        return "Exam corrected."

    def __str__(self) -> str:
        return f"Person: {self.name} | Email: {self.email}"


class ProfessorTutor(Professor, Tutor):
    def __init__(self, ur, id, name, email, celphone, department, formation):
        Person.__init__(self, ur, id, name, email, celphone)
        self.__department = department
        self.__formation = formation

    @property
    def formation(self):
        return self.__formation

    @formation.setter
    def formation(self, formation):
        self.__formation = formation

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

    def teach_class(self):
        return "Class teached."

    def correct_text(self):
        return "Exam corrected."

    def __str__(self) -> str:
        return f"Person: {self.name} | Email: {self.email}"
