import moviepy
import moviepy.editor as mpy

import numpy
import PIL
from PIL import Image

#class FrameGenerator:




hight = 640
width = 480

def GenerateFrame(pitch):
		
	R = 0
	G = 0
	B = 0

	if pitch > 9180:
		R = 255
		G = 255
		B = 255

	if pitch > 4590 and pitch <= 9180:
		val = int(pitch / 36)
		R = val
		G = 255 - val
		B = 0

	if pitch > 0 and pitch <= 4590:
		val = int(pitch / 18)
		R = 0
		G = val
		B = 255 - val

	im = Image.new("RGB", (hight, width), (R,G,B))
	
	return numpy.array(im)



def GenerateAllFrames(features):
		# Float from 0 to 10,000
		
	frames = []

	for f in features:
		frames.append(GenerateFrame(f))

	return frames


def test():
	array = []
	for x in range(-100, 9500):
		if x % 2 == 0:
			array.append(x)
	frames = GenerateAllFrames(array)
	

	clip = mpy.ImageSequenceClip(frames, fps=60)

	clip.write_videofile("movie.mp4", fps=60)



















