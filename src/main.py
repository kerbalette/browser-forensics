import argparse, platform, os
from browser_forensics import chrome

def main(profile_path):
    history_db = profile_path + '/History'
    chrome.read_history(history_db)


def GetOSType():
    platform_type = platform.system()
    match platform_type:
        case "Darwin":
            return "osx"
        case _:
            return "windows"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Browser Forensics Data Extractor')

    operating_system = GetOSType()
    user_home_folder = os.path.expanduser('~')

    if operating_system == 'osx':
        browser_profile_path = f'{user_home_folder}/Library/Application Support/Google/Chrome/Default/'
    else:
        browser_profile_path = f'C:\\Users\\{user_home_folder}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

    parser.add_argument('-b', '--browser', help='The Browser type: Chrome or Firefox', required=False, default="chrome")
    parser.add_argument('-l', '--location', help='Enter the location of browser profile', required=False, default=browser_profile_path )
    args = parser.parse_args()
    print(args.location)
    print(browser_profile_path)

    #print(f'{args.location} and also {browser_profile_path}')

    main(args.location)