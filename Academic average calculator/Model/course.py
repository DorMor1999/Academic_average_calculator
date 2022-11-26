class Course:
    def __init__(self, name, credits, grade):
        self.name = name
        self.credits = credits
        self.grade = grade

    def __eq__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        return other.name == self.name