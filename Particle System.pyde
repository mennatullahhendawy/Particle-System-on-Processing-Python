#defining fixed variables
particles = []

def setup(): #setting up the screen
    size(600, 400)  # Set up the screen size
    noStroke()  # No outlines for shapes

def draw():
    background(0)  # Black background

    # Update and display each particle
    for i in reversed(range(len(particles))): #for loop to create endless number of particles by clicking
        particle = particles[i] 
        
        # Update position of particle so it moves
        particle['position'].add(particle['velocity'])
        
        # Reduce lifespan (fading effect)
        particle['lifespan'] -= 2
        
        # Display particle 
        fill(200, 255, particle['lifespan'])  # Fading for all particles and making the circle not monochrome
        circle(particle['position'].x, particle['position'].y, 50) #the shape

def mousePressed():
    # Create new particle at the mouse position
    new_particle = {
        'position': PVector(mouseX, mouseY),  # Starting position at the mouse click
        'velocity': PVector(random(-2, 2), random(-2, 2)),  # Random velocity so the particle moves randomly 
        'lifespan': 255 # Lifespan to create fading
    }
    
    # Add the new particle to the list
    particles.append(new_particle) 
