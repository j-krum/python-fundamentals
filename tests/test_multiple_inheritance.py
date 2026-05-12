# test_multiple_inheritance.py

from multiple_inheritance import Professor, ProfessorTutor, Student


class TestMultipleInheritance:
    professor_tutor_has_department = ProfessorTutor(
        123123, 456456, "Joe", "joe@mail.com", 789789, "IT", None
    )
    professor_tutor_has_formation = ProfessorTutor(
        123123, 456456, "Joe", "joe@mail.com", 789789, None, "Data Science"
    )
    professor_tutor_string = ProfessorTutor(
        123123, 456456, "Joe", "joe@mail.com", 789789, "IT", "Data Science"
    )
    professor_has_department = Professor(
        123123, 456456, "Joe", "joe@mail.com", 789789, "IT"
    )
    student_has_matricule = Student(
        123123, 456456, "Joe", "joe@mail.com", 789789, 678678
    )

    def test_professor_tutor_has_department(self):
        assert self.professor_tutor_has_department.department == "IT"

    def test_professor_tutor_has_formation(self):
        assert self.professor_tutor_has_formation.formation == "Data Science"

    def test_professor_tutor_string(self):
        assert str(self.professor_tutor_string) == "Person: Joe | Email: joe@mail.com"

    def test_professor_has_department(self):
        assert self.professor_has_department.department == "IT"

    def test_student_has_mastricule(self):
        assert self.student_has_matricule.matricule == 678678
