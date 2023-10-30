import config
import loguru
import mysql.connector



db = mysql.connector.connect(
    username = "root",
    host = "localhost",
    database = "BorrowedMoney",
    password = config.db_pass
)
cursor = db.cursor()
LOGGER = loguru.logger