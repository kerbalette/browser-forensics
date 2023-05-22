from browser_forensics import common_lib

def read_history(history_db):
    sql_cmd = "select datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Visit_time, visits.visit_duration, urls.url, urls.visit_count, datetime((urls.last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Last_Visit_Time FROM visits LEFT JOIN urls ON visits.url = urls.id ORDER BY Decoded_Last_Visit_time DESC"
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (Decoded_Visit_time, visit_duration, url, visit_count, Decoded_Last_Visit_Time) = row
        print (f"{Decoded_Visit_time}, {url}, {visit_count}")

def read_downloads(history_db):
    sql_cmd = "select datetime((start_time/1000000)-11644473600, 'unixepoch', 'localtime') AS timestamp, current_path, received_bytes, referrer, tab_url, mime_type FROM downloads ORDER BY timestamp DESC"
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (start_time, current_path, received_bytes, referrer, tab_url, mime_type) = row
        print(f'{start_time}, {current_path}, {received_bytes}, {referrer}, {tab_url}, {mime_type}')

def read_search_terms(history_db):
    sql_cmd = "SELECT urls.url AS search_url, keyword_search_terms.term FROM keyword_search_terms INNER JOIN urls on keyword_search_terms.url_id = urls.id"
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (search_url, term) = row
        print(f'{search_url}, {term}')
