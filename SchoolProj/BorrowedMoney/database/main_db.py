import datetime
import loguru

from .. import *


def create_table() -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS borrowedMoney (
                   borrower_name varchar(300) PRIMARY KEY,
                   borrowed_amount bigint NOT NULL,
                   borrowed_date date
    );
                   """)

create_table()


def formatter(dat) -> str:
    count = 1
    text = ""
    for i in dat:
        date = i[-1].__str__().split("-")
        date.reverse()
        daterep = date.__str__().replace("[", "").replace("]", "").replace("', ", "-").replace("'", "")
        text+=f"""{count}: Date: {daterep}\n\t> Name: {i[0]}\n\t> Borrowed Amount: {i[1]}\n\n"""
        count+=1
    return text

class get:
    

    def name_data(name: str) -> None:
        try:
            cursor.execute(f"SELECT * from BorrowedMoney WHERE borrower_name = '{name}'")
            
        except Exception as e:LOGGER.error(e);return None
        else: return None if cursor.fetchone() == None else " "

    def borrowed_amount(name: str)  -> int:
        try:
            cursor.execute(f"SELECT borrowed_amount FROM borrowedMoney WHERE borrower_name='{name}'")
        except Exception as e:
            return LOGGER.error(e)
        else:
            return cursor.fetchone()

    def get_borrowers() -> list:
        try:
            cursor.execute("SELECT * FROM BorrowedMoney")
        except Exception as e:
            LOGGER.error(e)
        else:
            return formatter(cursor.fetchall())


class update:


    def new_borrower(name: str, amount: int, date: datetime = datetime.datetime.date(datetime.datetime.now())) -> None:
        if get.name_data(name):
            try:
                cursor.execute(f"UPDATE borrowedMoney SET borrowed_amount={get.borrowed_amount(name)[0]+amount}, borrowed_date = '{date}';")
            except Exception as e:
                LOGGER.error(e)
            else:
                return db.commit()

        try:
            cursor.execute(f"INSERT INTO borrowedMoney(borrower_name, borrowed_amount, borrowed_date) VALUES('{name}', {amount}, '{date}');")
        except Exception as e:
            LOGGER.error(e)
        else:
            db.commit()
    
    def del_borrower(name: str, amount: str, date: datetime = datetime.datetime.date(datetime.datetime.now())) -> None:
        try:
            if amount == "*" or int(amount)>=get.borrowed_amount(name)[0]:
                cursor.execute(f"DELETE FROM borrowedMoney WHERE borrower_name='{name}'")
        except Exception as e:
            LOGGER.error(e)
        amount = int(amount)
        try:
            if amount<get.borrowed_amount(name)[0]:
                cursor.execute(f"UPDATE borrowedMoney SET borrowed_amount={get.borrowed_amount(name)[0]-amount}, borrowed_date = '{date}' WHERE borrower_name='{name}';")
        except Exception as e:
            LOGGER.error(e)
        db.commit()