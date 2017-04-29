import unittest
import FrameGenerator1 as f1
import FrameGenerator1 as f2

class TestGenerateFrames(unittest.TestCase):

	# Test that it produces the correct amount of frames
	def testFrameGen1NumberOfFrames(self):
		frames = f1.GenerateAllFrames([1,2,3,4,5])
		self.assertEquals(len(frames), 5)

	# Test that it produces the correct amount of frames
	def testFrameGen2NumberOfFrames(self):
		frames = f2.GenerateAllFrames([1,2,3,4,5,6,7,8,9,10])
		self.assertEquals(len(frames), 10)

	# Test the color of the frames
	def testFrameGen1Color(self):
		frames = f1.GenerateAllFrames([9200, 9000, 4000, 0, -1])
		# Tests color for first frame
		(R1, G1, B1) = frames[0][0][0]
		self.assertEquals(R1, 255)
		self.assertEquals(G1, 255)
		self.assertEquals(B1, 255)
		# Test color for second frame
		(R2, G2, B2) = frames[1][0][0]
		self.assertEquals(R2, 250)
		self.assertEquals(G2, 5)
		self.assertEquals(B2, 0)
		# Test color for third frame
		(R3, G3, B3) = frames[2][0][0]
		self.assertEquals(R3, 0)
		self.assertEquals(G3, 222)
		self.assertEquals(B3, 33)
		# Test color for fourth frame
		(R4, G4, B4) = frames[3][0][0]
		self.assertEquals(R4, 0)
		self.assertEquals(G4, 0)
		self.assertEquals(B4, 0)
		# Test color for fifth frame
		(R5, G5, B5) = frames[4][0][0]
		self.assertEquals(R5, 0)
		self.assertEquals(G5, 0)
		self.assertEquals(B5, 0)

	# Test the color of the frames
	def testFrameGen2Color(self):
		frames = f2.GenerateAllFrames([9000, 4000, 3000, -1])
		# Tests color for first frame
		(R1, G1, B1) = frames[0][0][0]
		self.assertEquals(R1, 250)
		self.assertEquals(G1, 5)
		self.assertEquals(B1, 0)
		# Test color for second frame
		(R2, G2, B2) = frames[1][0][0]
		self.assertEquals(R2, 0)
		self.assertEquals(G2, 222)
		self.assertEquals(B2, 33)
		# Test color for third frame
		(R3, G3, B3) = frames[2][0][0]
		self.assertEquals(R3, 0)
		self.assertEquals(G3, 166)
		self.assertEquals(B3, 89)
		# Test color for fourth frame
		(R4, G4, B4) = frames[3][0][0]
		self.assertEquals(R4, 0)
		self.assertEquals(G4, 0)
		self.assertEquals(B4, 0)


if __name__ == '__main__':
    unittest.main()











    