
from matplotlib import rcParams
import unittest

class Issue3293(unittest.TestCase):

    # test that rcParams markerfacecolor is present
    def test_marker(self):
        
        def marker():
            return "lines.marker" in rcParams.keys()
        self.assertEqual(marker(), True)



    # test that rcParams markerfacecolor is present
    def test_markerfacecolor(self):

        def present():
           return "lines.markerfacecolor" in rcParams.keys()
        self.assertEqual(present(), True)



    # test that rcParams markerfacecolor is present
    def test_markerfacecolorValue(self):
        def present():
           return "lines.markerfacecolor" in rcParams.keys()	
        def giveValue():
            if (present()):
                rcParams["lines.markerfacecolor"] = 'b'
                assert rcParams["lines.markerfacecolor"]  == 'b'
            else:
                assert False == True
	# to be tested colors in the future
	# similar idea
        giveValue()



if __name__ == '__main__':
    unittest.main()
