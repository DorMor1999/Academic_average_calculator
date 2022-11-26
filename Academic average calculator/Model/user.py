from Model.year import Year
from Model.semester import Semester
from Model.course import Course


class User:
    def __init__(self):
        self.email = ""
        self.password = ""
        self.num_of_years = 0
        self.all_courses = []
        self.years = []

    def set_password(self, password):
        if len(password) > 5:
            self.password = password
            return True
        else:
            return False

    def set_email(self, email):
        if "@gmail.com" in email or "@yahoo.com" in email:
            self.email = email
            return True
        else:
            return False

    def log_in(self, password):
        if password == self.password:
            return True
        else:
            return False

    def add_course(self, new_course, year, semester):
        self.add_course_to_all_courses(new_course)
        self.years[int(year) - 1].semesters[semester].add_course(new_course)
        return True

    def remove_course(self, course, year, semester):
        self.all_courses.remove(course)
        if semester == "Winter":
            semester = 0
        elif semester == "Spring":
            semester = 1
        else:
            semester = 2
        self.years[year - 1].semesters[semester].remove_course(course)


    def add_year(self):
        self.num_of_years += 1
        year = Year(self.num_of_years)
        self.years.append(year)


    # check course with name
    def search_by_name_course(self, course):
        low = 0
        high = len(self.all_courses) - 1
        while low <= high:
            middle = int((low + high) / 2)
            # found
            if course == self.all_courses[middle].name:
                return self.all_courses[middle]
            elif course > self.all_courses[middle].name:
                low = middle + 1
            else:
                high = middle - 1
        # not found
        return -1

    def get_avg(self):
        credits = 0
        sum = 0
        for year in self.years:
            credits += year.get_credits()
            sum += year.get_avg() * year.get_credits()
        if credits == 0:
            return 0
        else:
            return sum / credits

    def get_credits(self):
        credits = 0
        for year in self.years:
            credits += year.get_credits()
        return credits

    def add_course_to_all_courses(self, new_course):
        # add the first one
        if len(self.all_courses) == 0:
            self.all_courses.append(new_course)
            return True
        # add to the beginning
        elif self.all_courses[0].name > new_course.name and not self.all_courses[
            0].__eq__(new_course):
            self.all_courses.insert(0, new_course)
            return True
        # add to the end
        elif self.all_courses[-1].name < new_course.name and not \
                self.all_courses[-1].__eq__(new_course):
            self.all_courses.append(new_course)
            return True
        # add between
        else:
            for index in range(len(self.all_courses) - 1):
                if self.all_courses[index].name < new_course.name and \
                        self.all_courses[index + 1].name > new_course.name:
                    self.all_courses.insert(index + 1, new_course)
                    return True
        # already inside the list so we don't add
        return False


# u = User()
# u.add_year()
# c = Course("c", 5, 74)
# u.add_course(c, 1, 0)
# a = Course("a", 5, 72)
# u.add_course(a, 1, 0)
# print(u.all_courses[0].name)
# print(u.all_courses[1].name)
# print(u.years[0].semesters[0].courses[0].name)
# print(u.years[0].semesters[0].courses[1].name)
# print(u.years[0].semesters[0].avg)
# print(u.get_credits())
#
#
# u.remove_course(c, 1, 0)
# u.remove_course(a, 1, 0)
# print(u.get_avg())
# print(u.get_credits())