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