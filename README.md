# Particle System on Processing Python
 
Interactive Particle Demonstration
This repository contains an Interactive Particle Demonstration developed as part of the Game Development 1 course at the University of California, Santa Cruz. The demonstration showcases many moving objects on the screen that are generated interactively and fade over time.

Acknowledgments
This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy and Mohamed-Ali-77. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Overview
The Interactive Particle Demonstration is an object-oriented program that displays particles that move and fade over time. The particles are generated based on user input (mouse clicks), and each particle has a limited lifespan.

Some of the Game Features
•	Object-Oriented Programming: The particles are managed using object-oriented principles, with attributes such as position, velocity, and lifespan.
•	Interactive Features: Users can interact with the program by clicking to generate new particles on the screen.
•	Particle Behavior: The particles move with a random velocity and fade over time, providing a dynamic visual effect.

Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the particle_demo.pde file in Processing.

Usage
Running the Program
1.	Launch Processing.
2.	Open the particle_demo.pde file from this repository.
3.	Click the Run button in Processing to start the particle demonstration.
4.	Mouse Interaction: Click anywhere on the screen to create new particles at the mouse location. The particles will move and fade out over time.
Particle Behavior
•	Position: Each particle is created at the location of the mouse click.
•	Velocity: Each particle has a random velocity, making it move in random directions.
•	Lifespan: The lifespan of the particles decreases over time, causing them to fade out gradually.

Example Code Snippet
```python
Copy code
# Defining fixed variables
particles = []

def setup():
    size(600, 400)  # Set up the screen size
    noStroke()  # No outlines for shapes

def draw():
    background(0)  # Black background
    
    # Update and display each particle
    for i in reversed(range(len(particles))):
        particle = particles[i]
        
        # Update position of particle so it moves
        particle['position'].add(particle['velocity'])
        
        # Reduce lifespan (fading effect)
        particle['lifespan'] -= 2
        
        # Display particle 
        fill(200, 255, particle['lifespan'])  # Fading and color variation
        circle(particle['position'].x, particle['position'].y, 50)  # The particle's shape

def mousePressed():
    # Create new particle at the mouse position
    new_particle = {
        'position': PVector(mouseX, mouseY),  # Starting position at the mouse click
        'velocity': PVector(random(-2, 2), random(-2, 2)),  # Random velocity for movement
        'lifespan': 255  # Lifespan to create fading
    }
    
    # Add the new particle to the list
    particles.append(new_particle)


