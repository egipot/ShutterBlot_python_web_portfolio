from flask import Flask


app = Flask(__name__)
print(__name__)
#__main__

@app.route('/')
def my_home():
    #return render_template('index.html')
    return "<p>Hellowie Egipot!!!Whooohooo! </p>"

#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/blog/2020/dogs')
#def blog2():
#    return 'this is my dog'

    