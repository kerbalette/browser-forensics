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

    parser.add_argument('-b', '--browsertype', help='The Browser type: Chrome or Firefox', required=False, default="chrome")
    parser.add_argument('-l', '--location', help='Location of the Browser profile', required=False)

    subparser = parser.add_subparsers(dest='command')
    subparser.add_parser('history')
    subparser.add_parser('downloads')
    subparser.add_parser('search_terms')

    args = parser.parse_args()
    
    if args.location is None:
        browser_path = common_lib.get_default_browser_profile_path(common_lib.GetOSType(),args.browsertype)
    else:
        browser_path = args.location


    main(args.command, browser_path)
    

