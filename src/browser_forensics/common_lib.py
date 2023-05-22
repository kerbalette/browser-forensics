import sqlite3, platform, configparser, os

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
        
def get_default_browser_profile_path(operating_system, browser_type):
    path = ''
    user_home_folder = os.path.expanduser('~')
    
    if browser_type == 'firefox':
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

    if browser_type == 'chrome':
        if operating_system == 'osx':
            path = f'{user_home_folder}/Library/Application Support/Google/Chrome/Default/'
    elif operating_system == "windows":
            path = f'C:\\Users\\{user_home_folder}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

    return path