from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/subscribe',methods=['GET','POST'])
def subscribe():
    print('Here!')
    form_data = request.form
    #print(repr(form))
    email = form_data['email']
    selected_shoe = form_data['sn']
    shoe_size = form_data['ss']
    weekly_update = False
    gender = 'Male'
    try:
        gender = form_data['sg']
        if gender == 'on':
            gender = 'Female'
    except:
        pass
    try:
        weekly_update = form_data['su']
        if weekly_update == 'on':
            weekly_update = True
    except:
        pass
    #This is the data, from here on can send the data to a db.
    print(email,selected_shoe,shoe_size,weekly_update,gender)
    return render_template('success.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
