from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "dsfgjhklkfskdghjklo8t7ir6ey"    # /eyebrow waggle


@app.route('/')
def show_homepage():
    """Display homepage."""

    return render_template("index.html")


@app.route('/application-form')
def show_app_form():
    """Display application form."""

    # pass list of possible jobs
    all_jobs = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html",
                           all_jobs=all_jobs)


@app.route('/application-success')
def submit_application():
    """Retrieve user responses from application form and display success message."""

    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    job = request.args.get('job')
    salary = float(request.args.get('salary'))

    if not salary.is_integer():
        salary = "{:,.2f}".format(salary)
    else:
        salary = int(salary)
        salary = "{:,}".format(salary)

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           job=job)


# these two routes are extra
# flash messages aren't working
@app.route('/login')
def login_page():
    """Redirect to home page and flash failure message to user."""

    flash("Sorry, we are still implementing the Login feature. Coming soon!")
    return redirect('/')


@app.route('/contact')
def contact_page():
    """Redirect to home page and flash failure message to user."""

    flash("Sorry, we are still implementing the Contact Page feature. Coming soon!")
    return redirect('/')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
