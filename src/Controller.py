import moviepy
import moviepy.editor as mpy
from moviepy.editor import *
import Parser as P
import FrameGenerator as F


path = "../test_data/MindsEye_-_This_or_That.mp3"
audioClip = mpy.AudioFileClip(path)

test = P.Parser()
features = test.getSamples(path)

# Generates frames from output of parser
frames = F.GenerateAllFrames(features)

# Creates a video from array of frames
clip = mpy.ImageSequenceClip(frames, fps=29)

# Sets the audio to the video
clip = clip.set_audio(audioClip)

# Writes the final video to local machine
clip.write_videofile("movie.mp4", fps=29)















