# Finite Difference Methods for Solving PDEs  

## Overview  
This repository contains implementations of the Finite Difference Method (FDM) for solving fundamental partial differential equations (PDEs). FDM is a widely used numerical method that approximates derivatives using discrete differences, making it suitable for solving PDEs in various scientific and engineering applications.  

## Implemented Equations  
### 1. **Heat Equation (FDM-heat equation.py)**  
   - A parabolic PDE that describes the distribution of heat (or temperature variation) over time.  
   - Implemented using the explicit finite difference method.  

### 2. **Laplace Equation (FDM-laplace eqn.py)**  
   - A steady-state elliptic PDE that models equilibrium conditions, such as electrostatics and steady-state heat conduction.  
   - Solved using the iterative finite difference approach.  

### 3. **Poisson’s Equation (FDM-poissions eqn.py)**  
   - An extension of the Laplace equation that includes a source term, used in electrostatics, fluid dynamics, and heat transfer.  
   - Discretized using a second-order central difference scheme.  

### 4. **Wave Equation (FDM-wave equation.py)**  
   - A hyperbolic PDE that describes wave propagation in physics and engineering (e.g., sound waves, water waves).  
   - Implemented using an explicit second-order time-stepping scheme.  

4. Modify parameters within scripts to test different initial and boundary conditions.  

## Results & Visualization  
- Each script generates numerical solutions and visualizes results using `matplotlib`.  
- Users can compare analytical and numerical solutions by adjusting grid resolution and time steps.  

## Future Work  
- Extend FDM implementations to higher-dimensional PDEs.  
- Compare FDM results with spectral methods and Physics-Informed Neural Networks (PINNs).  
- Implement adaptive mesh refinement for improved accuracy.  
