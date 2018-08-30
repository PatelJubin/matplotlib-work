import numpy as np
import unittest
from matplotlib import pyplot as plt
from matplotlib import animation


class Issue1656(unittest.TestCase):

    # test that animations are added to figure.animations: fix for issue-1656
    def test_animation_is_added_to_figure_animations(self):
        fig, ax = plt.subplots()

        x = np.arange(0, 2*np.pi, 0.01)
        line, = ax.plot(x, np.sin(x))

        def animate(i):
            line.set_ydata(np.sin(x + i/10.0))  # update the data
            return line,

        def init():
            line.set_ydata(np.ma.array(x, mask=True))
            return line,

        self.assertEqual(len(fig.animations), 0)
        anim = animation.FuncAnimation(fig, animate, np.arange(1, 200),
                                       init_func=init, interval=25, blit=True)
        self.assertEqual(len(fig.animations), 1)
        assert fig.animations[0] == anim

if __name__ == '__main__':
    unittest.main()
