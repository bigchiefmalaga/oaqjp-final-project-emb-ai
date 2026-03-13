import unittest

from emotion_detection import emotion_detector
class TestEmotion(unittest.TestCase):
    def test_joy(self):
    self assertEqual(emtion_detector("I am glad this happened"), 'Joy')
    def test_anger(self):
    self assertEqual(emtion_detector("I am really mad about this"), 'anger')
    def test_disgust(self):
    self assertEqual(emtion_detector("I feel disgusted just hearing about this"), 'disgust')
    def test_sadness(self):
    self assertEqual(emtion_detector("I am so sad about this"), 'sadness')
    def test_fear(self):
    self assertEqual(emtion_detector("I am really afraid that this will happen"), 'fear')

    if __name__ == '__main__':
        unittest.main()