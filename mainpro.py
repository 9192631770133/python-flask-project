from flask import Flask, redirect, render_template, request
from dbm import adddata,fetchdata, specificdata, updatedata,deletedata

app=Flask(__name__)
@app.route('/')
def home1():
   return render_template("index.html") 

@app.route('/createlink')
def createfunc():
    return render_template("create.html") 

@app.route('/savelink',methods=["POST"]) 
def savefun():
    firstname=request.form["fname"]
    lastname=request.form["lname"]
    disease=request.form["diseases"]
    phoneno=request.form["CNo."]
    t=(firstname,lastname,disease,phoneno)
    adddata(t)
    return render_template("/create.html")   

@app.route("/showlink")
def showfun():
    datalist=fetchdata()
    return render_template("showall.html",data=datalist)

@app.route("/editlink/<int:id>")
def displayforupdate(id):
    datalist=specificdata(id)
    return render_template("edit.html",data=datalist)

@app.route("/updatelink/<int:id>",methods=["POST"])
def updatefun(id):
    firstname=request.form["fname"]
    lastname=request.form["lname"]
    disease=request.form["diseases"]
    phoneno=request.form["CNo."]
    t=(firstname,lastname,disease,phoneno,id)
    updatedata(t)
    return redirect("/showlink")

@app.route("/deletelink/<int:id>")
def deletefun(id):
    deletedata(id)
    return redirect("/showlink")    
if __name__=="__main__":
    app.run()