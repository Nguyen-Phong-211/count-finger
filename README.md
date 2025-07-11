# count-finger

## Purpose

**count-finger** is a project for recognizing the number of raised fingers using a camera. This application supports detecting a single hand and counting the number of fingers shown.

## Description

The project uses Python for image analysis from a camera, identifies the user's hand, and counts the number of raised fingers. Note: The system only detects one hand at a time.

## System Requirements

- Python (recommended version 3.10 or higher)
- A computer with a camera (webcam or external camera)
- Python libraries (e.g., OpenCV, numpy, etc.)

## Features

- Detects hand via camera
- Counts the number of raised fingers
- Displays results directly on the screen
- Simple and easy to use

## Installation

1. Install Python if you haven’t already.
2. Clone the repository:
   ```bash
   git clone https://github.com/Nguyen-Phong-211/count-finger.git
   cd count-finger
   ```
3. Install required libraries:
   ```bash
   pip install opencv-python numpy
   ```
4. Connect your camera to your computer.

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```
2. Place your hand in front of the camera. The number of raised fingers will be displayed on the screen.

## Example

- If you show 3 fingers in front of the camera, the program will display **3**.

## Contribution

If you want to contribute to the project, please fork the repository and submit a pull request.

## Contact

- Author: [Nguyen-Phong-211](https://github.com/Nguyen-Phong-211) - zephyrnguyen.vn@gmail.com

## License

Currently, there is no license information for this project.

---

**Note:** This project only detects one hand at a time.
