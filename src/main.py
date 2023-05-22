import argparse, os
from browser_forensics import chrome
from browser_forensics import common_lib

def main(argcmd, profile_path):
    if not profile_path.endswith('/'):
        profile_path = profile_path + '/'

    history_db = profile_path + 'History'

    if argcmd == "history":
        chrome.read_history(history_db)

    if argcmd == "downloads":
        chrome.read_downloads(history_db)

    if argcmd == "search_terms":
        chrome.read_search_terms(history_db)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Browser Forensics Data Extractor')

    operating_system = common_lib.GetOSType()
    user_home_folder = os.path.expanduser('~')

    if operating_system == 'osx':
        browser_profile_path = f'{user_home_folder}/Library/Application Support/Google/Chrome/Default/'
    else:
        browser_profile_path = f'C:\\Users\\{user_home_folder}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'

    subparser = parser.add_subparsers(dest='command')
    subparser.add_parser('history')
    subparser.add_parser('downloads')
    subparser.add_parser('search_terms')

    parser.add_argument('-b', '--browser', help='The Browser type: Chrome or Firefox', required=False, default="chrome")
    parser.add_argument('-l', '--location', help='Enter the location of browser profile', required=False, default=browser_profile_path )
    
    
    args = parser.parse_args()
    main(args.command, args.location)