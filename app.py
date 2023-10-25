# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:pagerrender_id>')
def pagerender(pagerrender_id):
    return render_template(pagerrender_id)

@app.route('/about/<username>/<int:post_id>')
def about(username=None,post_id=None):
    return render_template('about.html',name=username,id=post_id)


def formSubmittedFile(data):
    with open('database.txt' , mode='a') as mydata:
        #-->> so I opened the respective file with the mmode as a
        #-->> indicates that we are appending something to mode 
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        #-->> now we write those things to my respective database as well 
        file = mydata.write(f'\n{email}, {subject}, {message}')
    



@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        #-->> so now data is nothing but a sort of 
        #-->> dictionary with the key and value pairs as well too
        formSubmittedFile(data)
        return render_template('/thankyou.html')
    else:
        return "Something went wrong GO BACK and TRY AGAIN!!!!"
# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def blog():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
