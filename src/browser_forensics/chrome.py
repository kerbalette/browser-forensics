from browser_forensics import common_lib
import os

operating_system = ''

def get_default_browser_profile_path(operating_system):
    path = ''
    user_home_folder = os.path.expanduser('~')

    if operating_system == 'osx':
            path = f'{user_home_folder}/Library/Application Support/Google/Chrome/Default/'
    elif operating_system == "windows":
            path = f'C:\\Users\\{user_home_folder}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

    return path    

def read_history(profile_path, operating_system):
    sql_cmd = "select datetime((visits.visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Visit_time, visits.visit_duration, urls.url, urls.visit_count, datetime((urls.last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS Decoded_Last_Visit_Time FROM visits LEFT JOIN urls ON visits.url = urls.id ORDER BY Decoded_Last_Visit_time DESC"
    history_db = complete_db(profile_path, 'History', operating_system)
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (Decoded_Visit_time, visit_duration, url, visit_count, Decoded_Last_Visit_Time) = row
        print (f"{Decoded_Visit_time}, {url}, {visit_count}")

def read_downloads(profile_path, operating_system):
    sql_cmd = "select datetime((start_time/1000000)-11644473600, 'unixepoch', 'localtime') AS timestamp, current_path, received_bytes, referrer, tab_url, mime_type FROM downloads ORDER BY timestamp DESC"
    history_db = complete_db(profile_path, 'History', operating_system)
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (start_time, current_path, received_bytes, referrer, tab_url, mime_type) = row
        print(f'{start_time}, {current_path}, {received_bytes}, {referrer}, {tab_url}, {mime_type}')

def read_search_terms(profile_path, operating_system):
    sql_cmd = "SELECT urls.url AS search_url, keyword_search_terms.term FROM keyword_search_terms INNER JOIN urls on keyword_search_terms.url_id = urls.id"
    history_db = complete_db(profile_path, 'History', operating_system)
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (search_url, term) = row
        print(f'{search_url}, {term}')

def complete_db(profile_path, browser_db_file, operating_system):
     
    if operating_system == 'osx':
        if not profile_path.endswith('/'):
             profile_path = profile_path + '/'
    
    return profile_path + browser_db_file
