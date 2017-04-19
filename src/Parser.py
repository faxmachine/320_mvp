# to import use "import Parser"
# consider pydub for getting samplerate
import aubio

class Parser:
	def getSamples(self, file):
		sampleArray = []
		samplerate = 0  # use original source samplerate
		hop_size = 1 # number of frames to read in one block
		s = aubio.source(file, samplerate, hop_size)
		total_frames = 0

		while True: # reading loop
			samples, read = s()
			total_frames += read

			if(total_frames % 30 == 0):
				sampleArray.append(samples)
			if read < hop_size:
				break # end of file reached

		fmt_string = "read {:d} frames at {:d}Hz from {:s}"
		print (fmt_string.format(total_frames, s.samplerate, file))
		print(len(sampleArray))
		return sampleArray


# test
path = "../test_data/MindsEye_-_This_or_That.mp3"
test = Parser()
test.getSamples(path)