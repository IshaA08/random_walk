import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making walks as long as the program is active
while True:
    # Generate a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Style the plot
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values, 
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Reds,
        edgecolors='none', 
        s=15
        )
    
    # Emphasize the start and end points
    ax.scatter(0, 0, c='green', edgecolors='none', s=150)
    ax.scatter(
        rw.x_values[-1],
        rw.y_values[-1],
        c='orange',
        edgecolors='none',
        s=150
    )
    plt.show()

    keep_running = input("Do you want to make another walk> (y/n)")
    if keep_running == 'n':
        break