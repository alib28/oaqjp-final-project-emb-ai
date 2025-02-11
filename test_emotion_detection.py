import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """ Test Case for emotion_detector """
    def test_dominant_emotion(self):
        """ Checks if correct dominant emotion is detected"""
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1["dominant_emotion"],"joy")
        
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2["dominant_emotion"],"anger")
        
        res_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_3["dominant_emotion"],"disgust")
        
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4["dominant_emotion"],"sadness")
        
        res_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_5["dominant_emotion"],"fear")

if __name__ == "__main__":
    unittest.main()