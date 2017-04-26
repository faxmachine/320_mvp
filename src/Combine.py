import moviepy.editor as mpy


def createMP4(musicFilePath, frames, framesPerSecond):
	
	# Imports mp3 file
	audioClip = mpy.AudioFileClip(musicFilePath)

	# Creates a video from array of frames
	videoClip = mpy.ImageSequenceClip(frames, fps=framesPerSecond)

	# Sets the audio to the video
	finalClip = videoClip.set_audio(audioClip)

	# Creates name for new video
	strings = musicFilePath.split("/")
	string = strings.pop()
	strings = string.split(".")
	string = strings[0]+".mp4"

	# Writes the final video to local machine
	finalClip.write_videofile("videoLibrary/"+string, fps=framesPerSecond)

	return True














