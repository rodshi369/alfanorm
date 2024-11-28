# -*- coding: utf-8 -*-

import sqlite3
import csv
import sys
import  datetime

# __connection = None


def get_connection(namebase: str):
    # if __connection is None:
    __connection = sqlite3.connect(namebase)
    return __connection


def init_db(force: bool = False, nametable: str = "log"):
    conn = get_connection(sys.argv[0].replace("main.py", "")+"log.db")
    cur = conn.cursor()

    if force:
        cur.execute("DROP TABLE IS EXISTS "+nametable)

    cur.execute("CREATE TABLE IF NOT EXISTS "+nametable+" (id INTEGER  PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT NOT NULL,dt DATETIME, reg3137 REAL, "
                                                        "reg3139 REAL, reg3141  REAL, reg3143 REAL, reg3145 REAL, reg3154 REAL, "
                                                        "reg3156 REAL, reg1280  REAL, reg1282 REAL, reg1283 REAL, reg3161 REAL, "
                                                        "reg3162 REAL, reg3163 REAL);")

    conn.commit()


def add_record_log(param: list):
    conn = sqlite3.connect(sys.argv[0].replace("main.py", "")+"log.db")
    cur = conn.cursor()
    param.insert(0, datetime.datetime.now())
    try:
        cur.execute("""INSERT INTO log (dt, reg3137, reg3139, reg3141, reg3143,reg3145, reg3154, reg3156, reg1280, reg1282, reg1283, reg3161, reg3162, reg3163)
                    VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", param)
        conn.commit()
    except Exception as err:
        print(err)


def get_record(query, param):
    conn = sqlite3.connect(sys.argv[0].replace("main.py", "")+"log.db")
    cur = conn.cursor()
    rez = cur.execute(query, param)
    conn.commit()
    return rez

def convertDBtoCSV():
    conn = sqlite3.connect(sys.argv[0].replace("main.py", "") + "log.db")
    cursor = conn.cursor()
    cursor.execute("select * from log;")
    with open("out.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    csv_file.close()
    conn.close()