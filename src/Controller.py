import moviepy
import moviepy.editor as mpy
import Parser as P
import FrameGenerator as F


# update    = ""

# # UILayer
# musicFile  = getMusicFile
# style      = getStyle

# # Parser
# update     = "Getting Samples"
# samples    = getSamples(musicFile)

# # Generate Frames
# update     = "Getting Frames"
# frames     = getFrames(samples, style)

# # Combine
# update     = "Redering Video"
# finalVideo = createMP4(musicFile, frames)
# update     = ""

# if finalVideo is False:

# 	update = "Video could not be rendered :'("

# else:

	# update = "Done"


path = "../test_data/MindsEye_-_This_or_That.mp3"
test = P.Parser()
features = test.getSamples(path)

frames = F.GenerateAllFrames(features)

clip = mpy.ImageSequenceClip(frames, fps=28)
clip.write_videofile("movie.mp4", fps=28)

vclip = mpy.VideoFileClip("movie.mp4")
audioClip = mpy.AudioFileClip(path)
vclip2 = vclip.set_audio(audioClip)

vclip2.write_videofile("movie.mp4", fps=28)










