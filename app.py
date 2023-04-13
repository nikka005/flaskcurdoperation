from flask import Flask,render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Nikka@005@localhost/ab1'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)

class andthisdata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), )
    text = db.Column(db.String(500), )
    def __repr__(self) -> str:
        return f"{self.sno} - {self.email}"

@app.route('/',methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        email = request.form['email1']
        about = request.form['about1']
        mydata = andthisdata(email=email,text=about)
        db.session.add(mydata)
        db.session.commit()

    allmydata = andthisdata.query.all()
    return render_template('index.html', allmydata=allmydata)

@app.route('/show')
def products():
    allmydata = andthisdata.query.all()
    print(allmydata)
    return 'this is products page'

@app.route('/update/<int:sno>',methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        email = request.form['email1']
        about = request.form['about1']
        mydata = andthisdata.query.filter_by(sno=sno).first()
        mydata.email=email
        mydata.text = about
        db.session.add(mydata)
        db.session.commit()
        return redirect("/")
    mydata = andthisdata.query.filter_by(sno=sno).first()
    return render_template ('update.html',mydata=mydata)

@app.route('/delete/<int:sno>')
def Delete(sno):
    mydata = andthisdata.query.filter_by(sno=sno).first()
    db.session.delete(mydata)
    db.session.commit()
    return redirect("/ ")

if __name__ ==('__main__'):
    db.create_all()
    app.run(debug=True)   