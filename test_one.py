import unittest
  
class SimpleTest(unittest.TestCase):
  
    # Returns True or False. 
    def test(self):        
        a = 1
        self.assertEqual(a,2)
  
if __name__ == '__main__':
    unittest.main()
