import Parser
import GenerateFrames
import Combine
import UILayer


update    = ""

# UILayer
musicFile  = getMusicFile
style      = getStyle

# Parser
update     = "Getting Samples"
samples    = getSamples(musicFile)

# Generate Frames
update     = "Getting Frames"
frames     = getFrames(samples, style)

# Combine
update     = "Redering Video"
finalVideo = createMP4(musicFile, frames)
update     = ""

if finalVideo is False:

	update = "Video could not be rendered :'("

else:

	update = "Done"


