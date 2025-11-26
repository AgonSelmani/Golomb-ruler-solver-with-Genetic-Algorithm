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

## 🚀 Features

- **Complete GA Implementation:** Built from scratch in pure Python
- **Adaptive Mechanisms:** Dynamic mutation rates and population diversity tracking
- **Multiple Stopping Criteria:** Time-based, generation-based, and convergence-based stopping
- **Validation System:** Comprehensive checks for Golomb Ruler validity
- **Performance Analysis:** Comparison against known mathematical optima

## 🧠 Algorithm Overview

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

## 🛠️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/AgonSelmani/golomb-ruler-solver.git
   cd golomb-ruler-solver
