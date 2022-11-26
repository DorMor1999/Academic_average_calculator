from Model.user import User
from Model.course import Course
import pickle


class Management:
    def __init__(self):
        #self.all_users = []
        self.read_users_lists_data()
        self.the_user = None

    def add_user(self,new_user):
        # add the first one
        if len(self.all_users) == 0:
            self.all_users.append(new_user)
        # add to the beginning
        elif new_user.email < self.all_users[0].email:
            self.all_users.insert(0, new_user)
        # add to the end
        elif new_user.email > self.all_users[-1].email:
            self.all_users.append(new_user)
        else:
            for index in range(len(self.all_users)-1):
                if new_user.email > self.all_users[index].email and new_user.email < self.all_users[index + 1].email:
                    self.all_users.insert(index + 1, new_user)
        self.save_users_list_data()
        return True

    # save data to binary file
    def save_users_list_data(self):
        file = open('../Model/data/users_list.txt', "wb")  # open file in write binary mode
        pickle.dump(self.all_users, file)  # dump list data into file
        file.close()  # close file pointer

    # read data from binary file
    def read_users_lists_data(self):
        file = open("../Model/data/users_list.txt", "rb")  # open file in read binary mode
        self.all_users = pickle.load(file)  # read binary data from file and store in list
        file.close()


    # check user with email
    def search_by_email_user(self, email):
        low = 0
        high = len(self.all_users) - 1
        while low <= high:
            middle = int((low + high) / 2)
            # found
            if email == self.all_users[middle].email:
                return self.all_users[middle]
            elif email > self.all_users[middle].email:
                low = middle + 1
            else:
                high = middle - 1
        # not found
        return -1

    # server mathods
    def sign_in(self, email, password):
        msg = ""
        the_user = self.search_by_email_user(email)
        if the_user == -1:
            msg += "We dont have a user with that email account!"
        elif not the_user.log_in(password):
            msg += "Incorrect password!"
        else:
            self.the_user = the_user
        return msg


    def register(self, email, password):
        msg = ""
        new_user = User()
        if self.search_by_email_user(email) != -1:
            return "We already have a user with that email account!"
        if not new_user.set_email(email):
            if msg == "":
                msg += "You can only register with yahoo or gmail!"
            else:
                msg += " , You can only register with yahoo or gmail!"
        if not new_user.set_password(password):
            if msg == "":
                msg += "Password must be at least 6 characters!"
            else:
                msg += " , Password must be at least 6 characters!"
        if msg == "":
            self.add_user(new_user)
            msg = "You have successfully registered"
        return msg

    #add course
    def add_course(self, name, credits, grade, year, semester):
        msg = ""
        if self.the_user.search_by_name_course(name) != -1:
            return "We already have a course with that name!"
        else:
            if len(name) < 1:
               msg += "The name must be at least one character long!"
            if len(credits) >= 1:
                credits = float(credits)
                if credits > 30 or credits < 0.5:
                    if msg == "":
                        msg += "The value of the credit points can only be between 0.5 and 30!"
                    else:
                        msg += ", The value of the credit points can only be between 0.5 and 30!"
            else:
                if msg == "":
                    msg += "Please enter credits!"
                else:
                    msg += ", Please enter credits!"
            if len(grade) >= 1:
                grade = int(grade)
                if grade > 100 or grade < 0:
                    if msg == "":
                        msg += "The value of the grade can only be between 0 and 100!"
                    else:
                        msg += ", The value of the grade can only be between 0 and 100!"
            else:
                if msg == "":
                    msg += "Please enter grade!"
                else:
                    msg += ", Please enter grade!"
            if msg == "":
                new_course = Course(name, credits, grade)
                if semester == "Winter":
                    semester = 0
                elif semester == "Spring":
                    semester = 1
                else:
                    semester = 2
                self.the_user.add_course(new_course, year, semester)
                self.save_users_list_data()
            return msg