import moviepy.editor as mpy
import numpy
import PIL
from PIL import Image
from math import sin

height = 640
width = 480

def GenerateFrame(pitch):	
	R = 0
	G = 100
	B = 50

	if pitch > 5000:
		R = (pitch ** 2) % 255
		G = (pitch * 255) % 255
		B = int((1/pitch) % 255)

	if pitch > 4590 and pitch <= 6000:
		val = int(pitch / 36)
		R = (pitch) % 255
		G = (pitch ** 2) % 255
		B = (pitch) % 255

	if pitch > 0 and pitch <= 1590:
		R = int((1/pitch) % 255)
		G = (pitch) * 255
		B = (pitch ** 2) % 255

	im = Image.new("RGB", (height, width), (int(R),int(G),int(B)))


	return numpy.array(im)


def GenerateAllFrames(features):
	frames = []
	for f in features:
		frames.append(GenerateFrame(f))
	return frames