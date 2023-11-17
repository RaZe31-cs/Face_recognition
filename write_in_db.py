import os
import sqlite3


def write():
    dirs = os.listdir(os.getcwd() + '\\Images')

    con = sqlite3.Connection('face_enc.sqlite')
    cur = con.cursor()
    for i in dirs:
        try:
            cur.execute('INSERT INTO Users(info) VALUES(?)', (i,))
        except Exception as e:
            pass
    con.commit()
    con.close()
