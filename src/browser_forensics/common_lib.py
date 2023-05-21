import sqlite3, platform

def fetch_db(db, command):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor.fetchall()


def GetOSType():
    platform_type = platform.system()
    match platform_type:
        case "Darwin":
            return "osx"
        case _:
            return "windows"