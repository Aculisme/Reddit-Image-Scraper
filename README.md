imgur-hosted-reddit-posted-downloader
=====================================

A Python script that checks Reddit for Imgur posts and downloads the corresponding images.

This tool is used to download images from a target subreddit.  

# Requirements:
Python 3.7  
Praw 6.0.0+  
Requests  

# Not included:
A Praw.ini file. There is plenty of documentation on [Praw's Website](https://praw.readthedocs.io)

# Format:
Required: pythonVersion fileName.py subreddit  

Optional: pythonVersion fileName.py subreddit numberToDownload minScore  

Example: python3 downloadtest1.py dankmemes 50 100  

The above will return the first 50 submissions that have a score over 100 from r/dankmemes sorted by newest.  

# Notes:

Direct any queries to [u/aculisme](https://reddit.com/u/aculisme)  

Have fun!