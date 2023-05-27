import configparser
from browser_forensics import common_lib

def get_default_browser_profile_path(operating_system):
    path = ''
    user_home_folder = os.path.expanduser('~')

    config = configparser.ConfigParser()
    os_browser_dir = ''
    if operating_system == 'osx':
        config.read(f'{user_home_folder}/Library/Application Support/Firefox/profiles.ini')
        os_browser_dir = f'{user_home_folder}/Library/Application Support/Firefox/'
    elif operating_system == "windows":
        config.read(f'{user_home_folder}\AppData\Roaming\Mozilla\Firefox\profiles.ini')
        os_browser_dir = f'{user_home_folder}\\AppData\\Roaming\\Mozilla\\Firefox\\'

    config_dict = {s:dict(config.items(s)) for s in config.sections()}
    for i in config_dict:
        config_elements = (config_dict[i].items())
        for y in config_elements:
            if y[0] == 'default' and y[1] == '1':
                path = config_dict[i]['path']
    path = os_browser_dir + path
    return path


def read_history(profile_path, operating_system):
    sql_cmd = "SELECT datetime(visit_date/1000000,'unixepoch') AS visit_date, url, title, visit_count, frecency FROM moz_places mp INNER JOIN moz_historyvisits mhv ON mp.id = mhv.place_id"
    history_db = complete_db(profile_path, 'places.sqlite', operating_system)
    result = common_lib.fetch_db(history_db, sql_cmd)
    for row in result:
        (visit_date, url, title, visit_count, frecency) = row
        print (f"{visit_date}, {url}, {title}, {visit_count}, {frecency}")

def read_downloads(profile_path, operating_system):
    print ("downloads")

def read_search_terms(profile_path, operating_system ):
    print("search_terms")

def complete_db(profile_path, browser_db_file, operating_system):
     
    if operating_system == 'osx':
        if not profile_path.endswith('/'):
             profile_path = profile_path + '/'
    
    return profile_path + browser_db_file    