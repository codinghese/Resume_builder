from flask import Flask,render_template,request,flash,url_for
app=Flask(__name__)
app.secret_key = 'bhanu'
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/basic',methods=['POST','GET'])
def basic():

    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        address=request.form.get('address')
        a=True
        print(name+" "+ address+" "+phone)

        if len(name)<2:
            flash("Name too short",category='error')
            a=False
            
        if len(phone)<10:
            flash("Please enter a valid phone number",category='error')
            a=False

        if len(address)<4:
            flash("Address  to Short",category='error')
            a=False
        if len(email)<4:
            flash("Invalid email",category='error')
            a=False
        
        
        if a:
            l=[]
            l.append(name)
            l.append(email)
            l.append(address)
            l.append(phone)
            flash("Data Captured Successfully ",category='success')
            return render_template('resume.html',l=l)

        
        
    return render_template('basic.html')

app.run(debug=True)