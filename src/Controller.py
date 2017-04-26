import Parser as p
import FrameGenerator1 as f1
import FrameGenerator2 as f2
import Combine as c


# musicFilePath = "../test_data/MindsEye_-_This_or_That.mp3"
framesPerSecond = 29
m = 3

def go(musicFilePath, style):

	# Parses the mp3 file and extracts features
	features = p.getSamples(musicFilePath, m)

	# Style selection
	# Generates frames from output of parser
	frames = []

	# Generates frames with style 1
	print ("Generating Frames")

	if style == 1:
		print ("With Style 1")
		frames = f1.GenerateAllFrames(features)
	if style == 2:
		print ("With Style 2")
		frames = f2.GenerateAllFrames(features)

	print ("Combining Frames With Music")
	
	# Combines mp3 and frames into a video output
	success = c.createMP4(musicFilePath, frames, framesPerSecond)

	if success is True:
		print ("Video Successfully Created")














