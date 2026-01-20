from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def hello():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone()
    return f"Hello from Jenkins CICD and Docker"

app.run(host="0.0.0.0", port=5000)
