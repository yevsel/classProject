
from numpy import byte

# Convert WMV video format to MP4 in few lines

with open('./project_explanation_1.wmv', "rb") as video_1:
    with open('./video_file.mp4', "wb") as video_2:
        for i in video_1():
            video_2.write(byte(i))
