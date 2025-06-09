from flask import Flask ,render_template,request,redirect,url_for,flash,Response,session


app=Flask(__name__,template_folder='Templates') #Parametro


#Creamos Ruta Principal
@app.route("/")
def Index():
     return render_template('index.html')


@app.route("/galeria")
def Prod():
     return render_template('galeria.html')
   
if __name__ == "__main__":
        app.run(port =5000,debug=True)


