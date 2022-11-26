from flask import Flask, render_template, request, redirect, url_for
from Model.management import Management

app = Flask(__name__)


global management
management = Management()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        management.the_user = None
    return render_template("index.html", office=management)


@app.route('/About')
def about():
    return render_template("about.html", office=management)


@app.route('/Contact')
def contact():
    return render_template("contact.html", office=management)


@app.route('/Register', methods=['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST':
        msg = management.register(str(request.form["email"]), str(request.form["password"]))
    return render_template("register.html", office=management, msg=msg)


@app.route('/Sign_in', methods=['GET', 'POST'])
def sign_in():
    msg = ""
    if request.method == 'POST':
        msg = management.sign_in(str(request.form["email"]), str(request.form["password"]))
        if msg == "":
            return redirect(url_for('home'))
    return render_template("sign in.html", office=management, msg=msg)


@app.route('/Year_<year>', methods=['GET', 'POST'])
def year(year):
    msg = ""
    if request.method == 'POST':
        msg = management.add_course(str(request.form["name"]), request.form["credits"], request.form["grade"], int(year), str(request.form["semester"]))
    year_avg = management.the_user.years[int(year) - 1].get_avg()
    year_credits = management.the_user.years[int(year) - 1].get_credits()
    return render_template("year.html", office=management, msg=msg, year=int(year)-1, year_avg=year_avg, year_credits=year_credits)


@app.route('/Add_year')
def add_year():
    management.the_user.add_year()
    management.save_users_list_data()
    return redirect(url_for('home'))


@app.route('/remove_<name>_<year>_<semester>')
def remove_course(name, year, semester):
    management.the_user.remove_course(management.the_user.search_by_name_course(name), int(year), semester)
    management.save_users_list_data()
    return redirect(url_for('year', year=year))


@app.route('/Overall')
def overall():
    overall_avg = management.the_user.get_avg()
    overall_credits = management.the_user.get_credits()
    num_of_courses = len(management.the_user.all_courses)
    return render_template("overall.html", office=management, overall_avg=overall_avg, overall_credits=overall_credits, num_of_courses=num_of_courses)


if __name__ == "__main__":
    app.run(debug=True)