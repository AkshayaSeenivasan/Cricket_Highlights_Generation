'''import os
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"

#from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
#from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import pandas as pd

print("Loading video...")
video = VideoFileClip("videos/full_match.mp4")
events = pd.read_csv("data/events.csv")

clips = []

print("Processing highlights...")

for i in range(len(events)):

    time = events.loc[i, "time"]
    event = events.loc[i, "event"]

    if event == "wicket":
        before, after = 8, 8
    elif event == "six":
        before, after = 5, 5
    else:
        before, after = 4, 4

    start = max(0, time - before)
    end = time + after

    clip = video.subclip(start, end)

    text = event.upper()

    txt = TextClip(text, fontsize=50, color='white', bg_color='black')
    txt = txt.set_position(('center', 'top')).set_duration(clip.duration)

    final_clip = CompositeVideoClip([clip, txt])

    clips.append(final_clip)

print("Merging clips...")

final_video = concatenate_videoclips(clips)

print("Saving output...")

final_video.write_videofile("output/highlights.mp4")

print("Done! Highlights created.")
'''
'''



from moviepy.editor import VideoFileClip, concatenate_videoclips
import pandas as pd

video = VideoFileClip("videos/full_match.mp4")
events = pd.read_csv("data/events.csv")

clips = []

for i in range(len(events)):
    time = events.loc[i, "time"]

    start = max(0, time - 5)
    end = time + 5

    clip = video.subclip(start, end)
    clips.append(clip)

final = concatenate_videoclips(clips)
final.write_videofile("output/highlights.mp4")

print("DONE ✅")'''

from moviepy.editor import VideoFileClip, concatenate_videoclips
import pandas as pd

video = VideoFileClip("videos/full_match.mp4")
events = pd.read_csv("data/events.csv")

clips = []

for i in range(len(events)):
    time = events.loc[i, "time"]

    start = max(0, time - 5)
    end = time + 5

    clip = video.subclip(start, end)
    clips.append(clip)

final = concatenate_videoclips(clips)
final.write_videofile("output/highlights.mp4")

print("DONE ✅")
