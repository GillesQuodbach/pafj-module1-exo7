# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from ecole.ecole.models.course import Course
from ecole.ecole.daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]

        # connection a la base de donnée
        # Dao.connection = connection a la BD
        # cursor = permet d'executer des requête sql
        # as = garanti que le cursor est fermé après utilisation
        with Dao.connection.cursor() as cursor:
            # select toutes les colonnes de la table course ou id_course = valeur fourni
            sql = "SELECT * FROM course WHERE id_course=%s"
            # execute la requête "sql" en remplaçant %s par la valeur de id_course
            # !!! (id_course,) = la virgule s'assure qu'on passe un tuple
            cursor.execute(sql, (id_course,))
            # récupère la première ligne trouvé sinon None
            record = cursor.fetchone()
        # si un cours est trouvé
        if record is not None:
            # on crée un objet Course avec les valeurs récupérées
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
        else:
            course = None

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
