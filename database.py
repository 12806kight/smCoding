from flask import Flask,render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="servicemetal",
  password="Holiday314!",
  database="sm"
)

app = Flask(__name__)
 
# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    try: 
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT * from product") 
        db = mycursor.fetchall() 
        return render_template("index.html", dbhtml = db)                                   
    except Exception as e: 
        return(str(e))
 
if __name__ == '__main__':  
   app.run()