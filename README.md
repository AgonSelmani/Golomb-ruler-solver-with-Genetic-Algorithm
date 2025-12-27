# Golomb-ruler-solver-with-Genetic-Algorithm

#UNFINISHED************************************

# Golomb Ruler Solver using a Genetic Algorithm

A Python implementation of a Genetic Algorithm to find optimal or near-optimal Golomb Ruler configurations. This project demonstrates the application of evolutionary computation to a non-trivial combinatorial optimization problem.

## 📋 Table of Contents
- [Overview](#overview)
- [What is a Golomb Ruler?](#what-is-a-golomb-ruler)
- [Features](#-features)
- [Algorithm Overview](#-algorithm-overview)
- [Installation & Usage](#️-installation--usage)
- [Example](#-example)
- [Project Structure](#️-project-structure)
- [Technologies Used](#-technologies-used)
- [Results & Learning](#-results--learning)

## Overview

This project implements a Genetic Algorithm from scratch to solve the Golomb Ruler problem. The algorithm evolves a population of potential rulers over generations, using selection, crossover, and mutation to find rulers with unique distances and minimal length.

## What is a Golomb Ruler?

A Golomb Ruler is a set of marks at integer positions along a ruler such that no two pairs of marks are the same distance apart. The goal is to find the shortest possible ruler for a given number of marks. This is an NP-hard combinatorial optimization problem with applications in radio astronomy, sensor placement, and coding theory.

## Features

- **Complete GA Implementation:** Built from scratch in pure Python
- **Adaptive Mechanisms:** Dynamic mutation rates and population diversity tracking
- **Multiple Stopping Criteria:** Time-based, generation-based, and convergence-based stopping
- **Validation System:** Comprehensive checks for Golomb Ruler validity
- **Performance Analysis:** Comparison against known mathematical optima

## Algorithm Overview

### Genetic Algorithm Components:
- **Representation:** Each individual is a sorted list of unique integers
- **Fitness Function:** Rewards valid rulers with more unique distances and shorter length
- **Selection:** Tournament selection for parent choice
- **Crossover:** Single-point crossover with repair mechanisms
- **Mutation:** Point mutation while maintaining validity constraints

### Key Implementation Details:
- **Elitism:** Preserves best solution across generations
- **Diversity Tracking:** Monitors population variety to prevent premature convergence
- **Adaptive Parameters:** Adjusts mutation rate based on improvement streaks

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/AgonSelmani/golomb-ruler-solver.git
   cd golomb-ruler-solver
   
2. **Run the solver**
   ```bash
   python GolombRuler.py

3. **Follow the prompts to enter the number of marks (e.g., 5, 6, 7)**
   ```text
   Searching for Golomb Ruler with 5 marks (Known optimal length: 11)

   Generation 20: Best length 12 (Fitness: -12.0), Diversity: 45.2
   Generation 40: Best length 11 (Fitness: -11.0), Diversity: 32.1

   Found optimal solution with length 11!

   Solution: [0, 1, 4, 9, 11]
   Length: 11
   Valid Golomb Ruler: Yes
   Execution time: 4.27 seconds


 **Project Structure**
   ```text

   golomb-ruler-solver/
   ├── GolombRuler.py          # Main algorithm implementation
   ├── README.md               # Project documentation (this file)
   └── .gitignore             # Git ignore file for Python projects



##Technologies Used

Language: Python 3
Concepts: Evolutionary Algorithms, Genetic Algorithms, Combinatorial Optimization
Libraries: random, time, math


## Results & Learning

Through this project, I gained deep understanding of:
   Evolutionary Computation: Designing and tuning genetic algorithms
   Constraint Handling: Managing solution validity in optimization problems
   Algorithm Analysis: Evaluating heuristic performance and convergence
   Problem Solving: Applying computational thinking to mathematical challenges

The algorithm successfully finds optimal solutions for small instances (n ≤ 8) and provides good approximations for larger problems, demonstrating the power of evolutionary approaches for NP-hard problems.



