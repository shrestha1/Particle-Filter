import numpy as np
'''
we have particles, now those particles has to be used in motion model.
Additive motion noise can be added as well.

'''

def prediction_step(particles, u):
    
    new_particles = []

    u_r1 = u['r1']
    u_trans = u['trans']
    u_r2 = u['r2']

    for particle in particles:
        
        noise_r1 = u_r1 + np.random.uniform(0,0.05)
        noise_trans = u_trans + np.random.uniform(0,0.5)
        noise_r2 = u_r2 + np.random.uniform(0,0.05)

        particle['x'] += noise_trans*np.cos(particle['theta'] + noise_r1)
        particle['y'] += u_trans*np.sin(particle['theta'] + noise_r2)
        particle['theta'] += noise_r1 + noise_r2

        new_particles.append(particle)

    return new_particles

