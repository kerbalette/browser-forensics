from browser_forensics import common_lib

def read_history(history_db):
    sql_cmd = "select datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Visit_time, visits.visit_duration, urls.url, urls.visit_count, datetime((urls.last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Last_Visit_Time FROM visits LEFT JOIN urls ON visits.url = urls.id ORDER BY Decoded_Last_Visit_time DESC"
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (Decoded_Visit_time, visit_duration, url, visit_count, Decoded_Last_Visit_Time) = row
        print (f"{Decoded_Visit_time}, {url}, {visit_count}")
