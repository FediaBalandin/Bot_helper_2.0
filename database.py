import sqlite3

def create_db():
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    con.close()




def create_table():
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = f'CREATE TABLE IF NOT EXISTS users' \
                    f'(id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
                    f'user_id INTEGER, ' \
                    f'subject TEXT, ' \
                    f'level TEXT, ' \
                    f'task TEXT, ' \
                    f'answer TEXT);'
    cur.execute(sql_query)
    con.close()





def insert_data(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = 'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);'
    VALUES = (1, user_id, 0, 0, 0, 0)
    cur.execute(
        sql_query,
        VALUES
    )
    con.commit()
    # # 'INSERT INTO users (user_id, subject) VALUES (100079937, "math");'
    # sql_query = f'INSERT INTO users user_id VALUES {user_id};'
    # cur.execute(sql_query)
    # con.commit()
    con.close()

def subject_math(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET subject = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('math', user_id,))
    # cur.execute(f'UPDATE users SET subject = "math2" WHERE user_id = {user_id}')

    con.commit()
    con.close()
    
def subject_physics(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET subject = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('physics', user_id,))
    con.commit()
    con.close()

def subject_history(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET subject = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('history', user_id,))
    con.commit()
    con.close()

def subject_chemistry(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET subject = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('chemistry', user_id,))
    con.commit()
    con.close()

def subject_clear(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET subject = ? WHERE user_id = ?;"
    cur.execute(sql_query, (0, user_id,))
    con.commit()
    con.close()

def lvl_basic(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET level = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('basic', user_id,))
    con.commit()
    con.close()

def lvl_pro(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET level = ? WHERE user_id = ?;"
    cur.execute(sql_query, ('pro', user_id,))
    con.commit()
    con.close()

def lvl_clear(user_id):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET level = ? WHERE user_id = ?;"
    cur.execute(sql_query, (0, user_id,))
    con.commit()
    con.close()

def task__(user_id, task):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET task = ? WHERE user_id = ?;"
    cur.execute(sql_query, (task, user_id,))
    con.commit()
    con.close()

def answer__(user_id, answer):
    con = sqlite3.connect('db_bot_helper.sqlite')
    cur = con.cursor()
    sql_query = "UPDATE users SET answer = ? WHERE user_id = ?;"
    cur.execute(sql_query, (answer, user_id,))
    con.commit()
    con.close()
