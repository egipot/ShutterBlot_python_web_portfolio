from flask import Flask, render_template, url_for, request, redirect 
import csv


app = Flask(__name__)
#print(__name__)
#__main__

@app.route('/')
def my_home():
    return render_template('index.html')
    #return "<p>Hello Egipot!!!</p>"

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_textfile(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email, subject, message])
        #file2 = database2.write(f'\n{email}, {subject}, {message}')

# POST means the browser wants us to save information ; GET means the browser wants us to send information
@app.route('/submit_form', methods=['POST', 'GET']) 
def submit_form():
    #return 'form submitted hooooraaay!!!'
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_textfile(data)
            write_to_csv(data)  
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again.'




