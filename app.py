from flask import Flask, redirect, url_for, render_template, request
import os
os.add_dll_directory(r'C:\Users\haris\anaconda3\Lib\site-packages\clidriver\bin')
import ibm_db,openpyxl

app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;UID=hlh20247;PWD=WwDIq5ImrO7lj72Y;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt",'','')

print(conn)
connState = ibm_db.active(conn)
print(connState)


@app.route("/")
def login():
    return render_template("form.html")

@app.route("/", methods =['get','post'] )
def submit():
    if request.method  == "post":
        name = request.form.get['Name']
        Age = request.form.get['Age']
        subject = request.form['subject']
        print(name)
        sql= "INSERT into REGISTER_HC VALUES (NAME, AGE, SUBJECT) where (?,?,?)"
        stmt=ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 2, Age)
        ibm_db.bind_param(stmt, 1, name)
        ibm_db.bind_param(stmt, 3, subject)
        ibm_db.execute(stmt)



if __name__ == "__main__":
    app.run(debug=True)