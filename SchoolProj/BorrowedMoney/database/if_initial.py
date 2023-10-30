import os
import config
import mysql.connector

h_h = ...
def ini_config():
    if open("BorrowedMoney/database/is_initial.txt", "r").read()=="1":return
    else:
        os.system("cd c:/SchoolProj")
        os.system("pip install -U -r requirements.txt --force-reinstall")
        db = mysql.connector.connect(
            username = "root",
            host = "localhost",
            password = config.db_pass
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS BorrowedMoney;")
        open("BorrowedMoney/database/is_initial.txt", "w").write("1")

ini_config()
