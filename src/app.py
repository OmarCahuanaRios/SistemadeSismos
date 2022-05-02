



from flask import Flask,render_template, request,redirect,url_for,flash
from flask_login import LoginManager,login_user,logout_user,login_required
from urllib3 import Retry
from config import config
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
from flask_wtf.csrf import CSRFProtect

from models.entities.user import User

app=Flask(__name__)
db=MySQL(app)
csrf=CSRFProtect()
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)



@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)

        if logged_user!=None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Password incorrect")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
        return render_template('auth/login.html')
    else:
        ("no recibo")
        return render_template('auth/login.html')



    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
        
@app.route('/home',methods=['GET','POST'])       
def home():
    if request.method=='POST':
    
        selectedValue=request.form['Zona']
        return redirect(url_for('GeneralMap',selectedValue=selectedValue))

    return render_template('home.html')     


@app.route('/<selectedValue>',methods=['GET','POST'])
def GeneralMap(selectedValue):
    if request.method=='POST':
        return redirect(url_for('Simulator'))
    if selectedValue=='GeneralMap':
        return render_template('GeneralMap.html')
    if selectedValue=='SpecificMap':
        return render_template('SpecificMap.html')


@app.route('/estadisticas',methods=['GET','POST'])
def estadisticas():
        
    return render_template('Result.html')
        

@app.route('/simulator',methods=['GET','POST'])
def Simulator():
    if request.method=='POST':
       return redirect(url_for('resultados'))
    return render_template('simulator.html')

@app.route('/listaplanes',methods=['GET','POST'])
def ListaPlanes():
    return render_template('ListaPlanes.html')

@app.route('/estadofuente',methods=['GET','POST'])
def EstadoFuente():
    return render_template('EstadoFuente.html')


@app.route('/result',methods=['GET','POST'])
def resultados():
    if request.method=='POST':
        return redirect(url_for('summary'))
    return render_template('Result.html')



@app.route('/summary',methods=['GET','POST'])
def summary():
    return render_template("Summary.html")














@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida solo para usuarios autenticados</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>",404



if __name__=='__main__': 
    csrf.init_app(app)
    app.config.from_object(config['development'])
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()