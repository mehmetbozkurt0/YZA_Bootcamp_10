from datetime import date
from app.database import cursor, db

def get_all():
    cursor.execute("SELECT * FROM tblUser")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns,row)))
    return results

def check_user(email,password):
    try:
        cursor.execute("SELECT * FROM tblUser WHERE Email = ? AND Password = ?",(email,password))
        row = cursor.fetchone()

        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns,row))
        return None
    except Exception as e:
        print("Giriş hatası: ",e)

def add_task(user_id: int, text: str, completed: bool = False):
    try:
        cursor.execute("INSERT INTO tblTask (UserId, Title, IsCompleted) VALUES (?,?,?)",(user_id,text,int(completed)))
        db.commit()
    except Exception as e:
        print("Görev eklenemedi: ",e)

def get_tasks(user_id: int):
    try:
        cursor.execute("SELECT TaskId, Title, IsCompleted FROM tblTask WHERE UserId = ?", (user_id,))
        rows = cursor.fetchall()
        result = [{"id": row[0], "text": row[1], "completed": bool(row[2])} for row in rows]
        return result
    except Exception as e:
        print("Görevler yüklenemedi: ",e)

def delete_task_by_id(user_id,id):
    try:
        cursor.execute("DELETE FROM tblTask WHERE UserId = ? AND TaskId = ?",(user_id,id,))
        db.commit()
    except Exception as e:
        print("Silme hatası: ",e)

def update_task_by_id(user_id, task_id, completed):
    try:
        cursor.execute("UPDATE tblTask SET IsCompleted = ? WHERE UserId = ? AND TaskId = ?",(int(completed),user_id,task_id))
        db.commit()
    except Exception as e:
        print("Güncelleme hatası: ",e)

def register_user(email,password,username):
    try:
        cursor.execute("INSERT INTO tblUser (Email, Password, UserName) VALUES (?,?,?)",(email,password,username))
        db.commit()
    except Exception as e:
        print("Kullanıcı kaydedilemedi: ",e)

def check_user_exist(email):
    cursor.execute("SELECT * FROM tblUser WHERE Email = ?", (email,))
    return cursor.fetchone() is not None

def get_daily_quote():
    try:
        cursor.execute("SELECT COUNT(*) FROM tblQuote")
        count = cursor.fetchone()[0]
        if count == 0:
            return None

        today = date.today()
        day_key = int(today.strftime("%Y%m%d"))
        quote_id = (day_key % count) + 1

        cursor.execute("SELECT Text FROM tblQuote WHERE Id = ?", (quote_id,))
        row = cursor.fetchone()
        return row[0] if row else None
    except Exception as e:
        print("Günün sözü yüklenemedi:", e)
        return None


def get_reflection(user_id):
    today = date.today()
    cursor.execute("SELECT Mood, Feedback FROM tblReflection WHERE UserId = ? AND ReflectionsDate = ?", (user_id, today))
    return cursor.fetchone()

def save_or_update_reflection(user_id, mood, feedback):
    today = date.today()
    cursor.execute("SELECT Id FROM tblReflection WHERE UserId = ? AND ReflectionsDate = ?", (user_id, today))
    row = cursor.fetchone()

    if row:
        cursor.execute("UPDATE tblReflection SET Mood = ?, Feedback = ? WHERE Id = ?", (mood, feedback, row[0]))
    else:
        cursor.execute("INSERT INTO tblReflection (UserId, Mood, Feedback) VALUES (?, ?, ?)", (user_id, mood, feedback))
    db.commit()










