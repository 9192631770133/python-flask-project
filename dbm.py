import pymysql as p
def getconnection():
    return p.connect(user="root",password="",database="patient",host="localhost")

def adddata(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into patientlist (firstname,lastname,disease,phoneno) values(%s,%s,%s,%s)"
    cur.execute(query,t)
    con.commit()
    con.close()

def fetchdata():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from patientlist")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificdata(id):
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from patientlist where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updatedata(t):
    con=getconnection()                  
    cur=con.cursor()
    query="update patientlist set firstname=%s,lastname=%s,disease=%s,phoneno=%s where id=%s"
    cur.execute(query,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getconnection()                  
    cur=con.cursor()
    query="delete from patientlist where id=%s"
    cur.execute(query,(id,))
    con.commit()
    con.close()