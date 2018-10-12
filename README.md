(Sub)Reddit Image Scraper
=====================================

A Python script that checks Reddit for Imgur posts and downloads the corresponding images.

This tool is used to download images from a target subreddit.  

# Requirements:
Python 3.7
Pip installer  
Praw 6.0.0+  
Requests  

You can install all the dependencies by completing the following steps:
1. Installing Python 3.7 [(for mac)](https://www.python.org/downloads/mac-osx/) [(for windows)](https://medium.com/@itylergarrett.tag/how-to-install-python-3-7-on-windows-10-pc-the-non-developer-version-b063e1913b39) 
2. Installing pip3 [(for mac)](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x) [(for windows)](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
3. Navigating to the cloned repository in terminal/command prompt
4. Calling `pip install -r requirements.txt`

# Not included:
A Praw.ini file. There is plenty of documentation on [Praw's Website](https://praw.readthedocs.io).  
The Praw.ini file should look like this:  
```
[DEFAULT]
check_for_updates=True

comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

oauth_url=https://oauth.reddit.com

reddit_url=https://www.reddit.com

short_url=https://redd.it

# CHANGE THE INFORMATION BELOW
[client]
user_agent='reddit image scraper'
client_id=cCgTEws4RUXbRA
client_secret=fyJGNMum38aOZbrwzuVrgHjy2ic
password=examplepassworld
username=example202
```  
## Instructions for changing values in praw.ini:  ##  
1. Log in to your Reddit account and go to [reddit.com/prefs/apps](https://reddit.com/prefs/apps)
2. Click the _create app_ button
3. Call your app 'reddit image scraper'. Click the 'script' option. Write `https://reddit.com` as the redirect url.
4. Click 'create app'.
5. Change the information in praw.ini with the information from reddit
    1. The text right under 'personal use script' is the `client_id`
    2. The text left of 'secret' is the `client_secret`
    3. Your account password is the `password`
    4. Your account username is the `username`
    5. You should call the `user_agent` 'reddit image scraper'


# Format:
Required: `pythonVersion fileName.py subreddit`  

Optional: `pythonVersion fileName.py subreddit numberToDownload minScore`  

Example: `python3 downloadtest1.py dankmemes 50 100`  

The above will return the first `50` submissions that have a score over `100` from `r/dankmemes` sorted by newest.  

# Notes:

Direct any queries to [u/aculisme](https://reddit.com/u/aculisme)  

Have fun!
