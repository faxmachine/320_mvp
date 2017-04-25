# to import use "import Parser"
# consider pydub for getting samplerate
import aubio
import numpy as np


class Parser:
	def getSamples(self, file):
		sampleArray = []
		samplerate = 0  # use original source samplerate
		hop_size = 512 # number of frames to read in one block
		s = aubio.source(file, samplerate, hop_size)
		total_frames = 0

		pitcher = aubio.pitch()
		pitcher.set_unit("Hz")

		while True: # reading loop
			samples, read = s()
			total_frames += read

			if(total_frames % 3 == 0):
				pitch = pitcher(samples)[0]
				print(pitch)
				sampleArray.append(pitch)

			if read < hop_size:
				break # end of file reached

		fmt_string = "read {:d} frames at {:d}Hz from {:s}"

		print(len(sampleArray))
		return sampleArray


