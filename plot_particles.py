import matplotlib.pyplot as plt
import numpy as np


def initialize_particles(nparticles=1000):
    particles = []

    for i in range(nparticles):
        particle = dict()
        particle['x'] = np.random.uniform(0, 20) 
        particle['y'] = np.random.uniform(0, 20)
        particle['theta'] = np.arctan(particle['y']/particle['x'])
        
        particles.append(particle)
    
    return particles 
    

def plot_particles(particles):
    x_parti = []
    y_parti = []

    for particle in particles:
        x_parti.append(particle['x'])
        y_parti.append(particle['y'])

    plt.scatter(x_parti, y_parti, s=2.5, color='r')


plot_particles(initialize_particles())
plt.show()