import sqlite3


def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

def get_questions_and_asnwer():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM questionandanswer")
    return cur.fetchall()

def get_answer_from_memory(question):
    rows = get_questions_and_asnwer()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer=row[1]
            break
    return answer

def insert_questions_and_answer(question,answer):
    con = create_connection()
    cur = con.cursor()
    query="insert into questionandanswer values('"+question+"','"+answer+"')"
    cur.execute(query)
    con.commit()
    con.close()
    
    

