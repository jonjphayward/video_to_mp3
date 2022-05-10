import os
import getpass
from subprocess import call
from datetime import datetime, timedelta


#create datetime vars
today = datetime.now()
yesterday = datetime.now() - timedelta(days=1)
timestamp = today.strftime("%d-%m-%Y %H;%M")

#get username
username = getpass.getuser()

#collect path vars
root_folder = os.path.abspath(os.getcwd())

#check requirements
ffmpeg = os.path.join(root_folder, "ffmpeg.exe")

logs = os.path.join(root_folder, "logs")
video_input = os.path.join(root_folder, "input")
mp3_output = os.path.join(root_folder, "output")

if not os.path.exists(logs):
    # Create a new directory because it does not exist 
    os.makedirs(logs)

if not os.path.exists(video_input):
    # Create a new directory because it does not exist 
    os.makedirs(video_input)

if not os.path.exists(mp3_output):
    # Create a new directory because it does not exist 
    os.makedirs(mp3_output)

input_list = os.listdir(video_input)

for f in input_list:
    filename, ext = os.path.splitext(f)
    newname = filename + ".mp3"
    
    call([ffmpeg, "-i", os.path.join(video_input, f), "-b:a", "128K", "-vn", os.path.join(mp3_output, newname)])