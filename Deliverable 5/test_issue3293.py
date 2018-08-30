import pytest
from matplotlib import rcParams
from matplotlib.testing.decorators import image_comparison
from matplotlib.testing.decorators import knownfailureif
import matplotlib.pyplot as plt
import unittest

class Issue3293(unittest.TestCase):
    
    # test that rcParams markerfacecolor is present
    def test_marker(self):
        
        def marker():
            return "lines.marker" in rcParams.keys()
        self.assertEqual(marker(), True)
    # note this is the intended test for image comparions
    #this is here to show what it would look like
    # Baseline images dont run from here
    #@image_comparison(baseline_images=['test'],extensions=['png'])
    @pytest.mark.xfail
    def test_lines_markerfacecolor(self):
        rcParams["lines.markerfacecolor"] = 'r'
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.set_title('Marker Face Color')
        ax.plot(range(4),markevery=1,marker="o")

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
