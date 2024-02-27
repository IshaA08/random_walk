from random import choice

class RandomWalk:
    """
    A class that generates random walks, which is
    a simplified model of physical Brownian motion
    that models things like molecules in liquids
    """

    def __init__(self, num_points=5000):
        """Initialize walk attributes"""
        self.num_points = num_points

        # Start the walk at (0, 0)
        self.x_values = [0]
        self.y_values = [0]