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