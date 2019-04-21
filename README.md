![alt text](pata.png "PATA logo")

# Project for Another Trajectory Algorithm

The aim of this project is to explore different ways for estimating particle trajectories given an initial subset of trajectories. The trajectories follow some dynamics and the equations that describe the dynamics are known. In rough the idea is to jump between computing new trajectories from the dynamics or to use the existing trajectories as a basis and estimate the new trajectory by "interpolation". There are three main challenges:

1. Understand what and how can we estimate/interpolate
1. Understand how can we make decisions on when to estimate or to simply use the physics
1. How can we run this efficiently

Python and stuff for other stuff.

## Goals

1. Calculate trajectories.
1. Build a database of diatomic collisions.
1. Use open source tools for data exploraion and processing: matplotlib, numpy, pandas, etc..
1. Benchmark open-source tools for prediction/learning: tensforflow, pytorch, pymc3.
1. Ducks! Ducks are awesome!

## Plotting styles

For uniform data plotting in the project, please use one of the provided matplotlib mplstyle under `./styles`.

* Default matplotlib style. Best for `jupyter-lab` light theme.
* Latex fonts with **light** theme: `helvet2.mplstyle`.
* Latex fonts with **dark** theme: `helvet2dark.mplstyle`.
* Normal fonts with **dark** theme: `mpl2dark.mplstyle`.

## Running code from the project

The yaml file `pata.yml` can be used with conda to create a **pata** environment with all the required software. Just run in a terminal:

`conda env create -f pata.yml`