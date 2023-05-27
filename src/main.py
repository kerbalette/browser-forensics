import argparse, os, importlib
from browser_forensics import chrome
from browser_forensics import common_lib

def main(browsertype, argcmd, location, operating_system):
    if browsertype == "chrome":
        browser = importlib.import_module('browser_forensics.chrome')

    if browsertype == "firefox":
        browser = importlib.import_module('browser_forensics.firefox')
    
    if location is None:
        browser_db = browser.get_default_browser_profile_path(operating_system)
    else:
        browser_db = location

    if argcmd == "history":
        browser.read_history(browser_db, operating_system)

    if argcmd == "downloads":
        browser.read_downloads(browser_db, operating_system)
    
    if argcmd == "search_terms":
        browser.read_search_terms(browser_db, operating_system)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Browser Forensics Data Extractor')

    parser.add_argument('-b', '--browsertype', help='The Browser type: Chrome or Firefox', required=False, default="chrome")
    parser.add_argument('-l', '--location', help='Location of the Browser profile', required=False)

    subparser = parser.add_subparsers(dest='command')
    subparser.add_parser('history')
    subparser.add_parser('downloads')
    subparser.add_parser('search_terms')

    args = parser.parse_args()
    
    main(args.browsertype, args.command, args.location, common_lib.GetOSType())
    

