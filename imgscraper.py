import praw, requests, urllib, shutil, os.path, sys

# Aculisme's Reddit Image Downloader
#
# This tool is used to download images from a
# target subreddit
#
# Format
# required: pythonVersion fileName.py subreddit 
# optional: numberToDownload minScore
#
# example: python3 downloadtest1.py dankmemes 50 100
#
# The above will return the first 50 submissions that 
# have a score over 100 from r/dankmemes sorted by newest. 
#
#
# Direct any queries to u/aculisme
#
# Have fun!

r = praw.Reddit('client') 

if len(sys.argv) >= 2:
    os.chdir('images/')
    # the subreddit was specified:
    targetSubreddit = sys.argv[1]
    subredditFolder = targetSubreddit+"/"
    if not os.path.exists(subredditFolder):
        # create folder for subreddit
        os.makedirs(subredditFolder) 
else:
    print("Remember to specify the target subreddit")
    sys.exit()

if len(sys.argv) >= 3:
    numberToDownload = int(sys.argv[2])
else:
    numberToDownload = 10

if len(sys.argv) >= 4:
    minScore = int(sys.argv[3])
else:
    minScore = 0

def downloadImage(imageUrl, localFileName):
    with urllib.request.urlopen(imageUrl) as response, open(localFileName+".jpg", 'wb') as out_file:
        # get data from url with requests as binary, ~copy it to the reddit id + .jpg
        shutil.copyfileobj(response, out_file)    
        print("done")
    
# move to memes / subreddit folder
os.chdir(subredditFolder)
maxToDownload = round(1.2*numberToDownload,1)
for submission in r.subreddit(targetSubreddit).new(limit=maxToDownload):
    try:
        if not submission.post_hint == 'image':
            continue
        if submission.num_crossposts > 1:
            continue
        if os.path.isfile(submission.id+".jpg"):    
            continue
        if submission.score < minScore:
            continue    
        print(submission.title) # to make it non-lazy
        image = submission.preview['images'][0]['source']['url']      
        downloadImage(image,submission.id)
    except:
        continue
    

# switch back to the parent directory
os.chdir("../../")     
