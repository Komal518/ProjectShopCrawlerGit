from flask import Flask,render_template,request,redirect,flash,session

app = Flask(__name__)
app.secret_key = "mera college mahan"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            return redirect('/home')
        else:
            flash("could not find user details! try again")
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        phone = request.form.get('phone')
        if email and password and name and phone:
            if len(password) > 5:
                pass
            else:
                flash("password is invalid, should be greater than 5","danger")
        else:
            flash("invalid details",'danger')
    return render_template('register.html')

@app.route('/home',methods=['POST','GET'])
def home():
    if not session.get('is_logged'):
        return redirect('/')
    
    if request.method == 'POST':
        pname = request.form.get('pname')
        pprice = request.form.get('pprice')
        pqty = request.form.get('pqty')
        if pname and pprice and pqty:
            data={'name':pname,'price':pprice,'qty':pqty}
            if register.add_product_to_cloud(data=data):
                flash("data sucessfully added", 'success')
                return redirect("/data")
            else:
                flash("data could not be added", "danger")
        else:
            flash("please fill all details", "danger")
    
    data = register.get_product_from_cloud()
    return render_template('data.html',data=list(data))


@app.route('/forgot',methods=['POST','GET'])
def forgot():
    return render_template('forgot.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
