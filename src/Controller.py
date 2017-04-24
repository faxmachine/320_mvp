import moviepy
import moviepy.editor as mpy
import Parser as P
import FrameGenerator


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

frames = GenerateFrames(features)

clip = mpy.ImageSequenceClip(frames, fps=28)
clip.write_videofile("movie.mp4", fps=28)










