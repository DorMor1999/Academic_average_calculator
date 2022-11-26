from Model.course import Course


class Semester:
    def __init__(self, name):
        self.name = name
        self.avg = 0
        self.credits = 0
        self.courses = []

    def add_course(self, new_course):
        # add the first one
        if len(self.courses) == 0:
            self.courses.append(new_course)
            self.update("add", new_course)
            return True
        # add to the beginning
        elif self.courses[0].name > new_course.name and not self.courses[
            0].__eq__(new_course):
            self.courses.insert(0, new_course)
            self.update("add", new_course)
            return True
        # add to the end
        elif self.courses[-1].name < new_course.name and not \
                self.courses[-1].__eq__(new_course):
            self.courses.append(new_course)
            self.update("add", new_course)
            return True
        # add between
        else:
            for index in range(len(self.courses) - 1):
                if self.courses[index].name < new_course.name and \
                        self.courses[index + 1].name > new_course.name:
                    self.courses.insert(index + 1, new_course)
                    self.update("add", new_course)
                    return True
        # already inside the list so we don't add
        return False

    def remove_course(self, course):
        self.courses.remove(course)
        self.update("remove", course)

    def update(self, operation, course):
        if operation == "add":
            sum = (self.avg * self.credits) + (course.grade * course.credits)
            self.credits += course.credits
            self.avg = sum / (self.credits)
        else:
            sum = (self.avg * self.credits) - (course.grade * course.credits)
            self.credits -= course.credits
            if self.credits == 0:
                self.avg = 0
            else:
                self.avg = sum / (self.credits)

