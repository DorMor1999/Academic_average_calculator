from Model.semester import Semester
from Model.course import Course


class Year:
    def __init__(self, name):
        self.name = name
        self.semesters = [Semester("Winter"), Semester("Spring"), Semester("Summer")]

    def get_avg(self):
        if self.semesters[0].credits + self.semesters[1].credits + self.semesters[2].credits == 0:
            return 0
        else:
            sum = (self.semesters[0].avg * self.semesters[0].credits) + (self.semesters[1].avg * self.semesters[1].credits) + (self.semesters[2].avg * self.semesters[2].credits)
            return sum / (self.semesters[0].credits + self.semesters[1].credits + self.semesters[2].credits)

    def get_credits(self):
        return self.semesters[0].credits + self.semesters[1].credits + self.semesters[2].credits
