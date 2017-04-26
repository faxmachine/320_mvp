import Parser as p
import FrameGenerator as f
import Combine as c


musicFilePath = "../test_data/MindsEye_-_This_or_That.mp3"
framesPerSecond = 29
m = 3

# def Go(musicFilePath, style, ):

# Parses the mp3 file and extracts features
features = p.getSamples(musicFilePath, m)

# Generates frames from output of parser
frames = f.GenerateAllFrames(features)

# Combines mp3 and frames into a video output
success = c.createMP4(musicFilePath, frames, framesPerSecond)















