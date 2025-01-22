# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from ecole.ecole.models.student import Student
from ecole.ecole.daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass()
class StudentDao(Dao[Student]):
    def create(self, teacher: Student) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param teacher: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_teacher: int) -> Optional[Student]:
        """Renvoit le teacher correspondant à l'entité dont l'id est id_teacher
           (ou None s'il n'a pu être trouvé)"""
        teacher: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT s.student_nbr, p.first_name, p.last_name, p.age FROM student s INNER JOIN person p ON s.id_person = p.id_person WHERE s.student_nbr = %s;"
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Student(record["first_name"], record["last_name"], record["age"])
            teacher.id = record["student_nbr"]

        else:
            teacher = None

        return teacher

    def update(self, course: Student) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Student) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
