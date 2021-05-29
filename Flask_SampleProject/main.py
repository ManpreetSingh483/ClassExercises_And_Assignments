from urllib import request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello world </h1>'


# Using Jinja 2template
# http://127.0.0.1:5000/welcome
@app.route('/welcome')
def welcome():
    return render_template('hello.html')  # Using render function from flask

# Using template for PATH parameter
# http://127.0.0.1:5000/welcome/Manpreet
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)  # Passing parameter to template


# http://127.0.0.1:5000/name
@app.route('/name')
def print_name():
    return '<h1> Manpreet </h1>'


# Get request (default is get request)
# http://127.0.0.1:5000/sum?a=10&b=20
# or
# @app.route('/sum', methods=['GET'])
@app.route('/sum')
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'Sum' + str(c)


# One way of writing in single line(In screenshot)

@app.route('/user_data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        #Declare Dictionary of values
        #dict = {'first_name': first_name, 'last_name':last_name}
        result = '''
                    <h1>First Name : {} </h1>
                    <h1>Last Name : {} </h1>
                    
            '''
        return result.format(first_name, last_name)
        #return dict
    return 'No Get method allowed, only post method accepted'


# http://127.0.0.1:5000/user
@app.route('/user')
def user_form():
    # Previously was used in this way
    # return '''
    # <form method="POST" action="http://127.0.0.1:5000/user-data">
    #        <div><label>First Name: <input type="text" name="fname"></label></div>
    #        <div><label>Last Name: <input type="text" name="lnm"></label></div>
    #        <input type="submit" value="Submit">
    # </form>
    # '''
    return render_template('user.html')  # Using render function from flask


if __name__ == '__main__':
    app.run()
