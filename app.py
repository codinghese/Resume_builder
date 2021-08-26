from flask import Flask,render_template,request,flash,url_for
app=Flask(__name__)
app.secret_key = 'bhanu'
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/resume',methods=['POST','GET'])
def resume_builder():

    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        address=request.form.get('address')
        print(name+" "+ address+" "+phone)

        if len(name)<2:
            flash("Name too short",category='error')
            
        if len(phone)<10:
            flash("Please enter a valid phone number",category='error')
        if len(address)<4:
            flash("Address  to Short",category='error')
        
        if len(email)<4:
            flash("Invalid email",category='error')

        else:
            flash("Data Captured Successfully ",category='success')
        
    return render_template('resume.html')

app.run(debug=True)