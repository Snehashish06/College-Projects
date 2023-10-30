import os
import config
import loguru
import mysql.connector



LOGGER = loguru.logger
if "MySQL80" not in os.system("net start").__str__():
    try:
        LOGGER.info("Trying to start SQL services")
        os.system('sc start "MySQL80"')
    except Exception as e:
        LOGGER.error(e)
else:
    os.system("CLS")
db = mysql.connector.connect(
    username = "root",
    host = "localhost",
    database = "BorrowedMoney",
    password = config.db_pass
)
cursor = db.cursor()
