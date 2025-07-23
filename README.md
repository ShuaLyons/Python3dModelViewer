# Python 3D Model Viewer

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/shualyons/python3dmodelviewer)

A simple, interactive 3D model viewer built with Python, Pygame, and PyOpenGL.  
Supports loading `.obj` models and allows intuitive mouse controls for rotation, zooming, and panning. Includes a fixed HUD showing XYZ axes for orientation.


## Features

- Load and render Wavefront `.obj` 3D models using [PyWavefront](https://github.com/pywavefront/PyWavefront)
- Mouse-based controls:
  - **Left-click + drag:** Rotate the model
  - **Right-click + drag:** Pan the camera view
  - **Mouse scroll wheel:** Zoom in/out
- Fixed Heads-Up Display (HUD) showing XYZ axes:
  - Red = X axis
  - Green = Y axis
  - Blue = Z axis (diagonal)
- Easily customizable background color
- Lightweight dependencies: Python, Pygame, PyOpenGL, PyWavefront


## Demo

![Demo Screenshot](images/Python3DModelViewerDemo2.JPG)




## Installation

1. Clone this repository:

```bash
git clone https://github.com/shualyons/python3dmodelviewer.git
cd yourrepo

---
