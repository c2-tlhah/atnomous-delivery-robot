# Pathfinding Algorithm Visualizer

## Overview

This project is a Python application that visualizes pathfinding algorithms on a 15x15 grid. The application uses the A* and Best First Search algorithms to find paths between a start and a delivery point on a grid with randomly placed obstacles. The visualization is implemented using PyQt5 for the GUI and Matplotlib for rendering the grid and paths.

## Features

- **Grid Visualization**: Displays a 15x15 grid with obstacles and paths.
- **Algorithm Selection**: Visualize paths computed by A* and Best First Search algorithms.
- **Pathfinding Algorithms**: Choose between A* and Best First Search to find paths between points.
- **Dynamic Obstacle Generation**: Randomly generates obstacles in the grid.
- **Interactive GUI**: Input start and delivery points, and see the pathfinding algorithms in action.
- **Real-Time Updates**: Update the visualization dynamically as new paths are calculated.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pathfinding-algorithm-visualizer.git

  Navigate to the Project Directory:

    cd pathfinding-algorithm-visualizer

Install Dependencies:
Ensure you have Python 3.x installed. The required packages are networkx, matplotlib, and PyQt5. Install them using pip:


    pip install networkx matplotlib PyQt5

Usage

  Run the Application:

    python pathfinding_gui.py

  Interface Overview:
      Start Input: Enter the x and y coordinates of the starting point.
      Delivery Input: Enter the x and y coordinates of the delivery point.
      Deliver Button: Calculate and visualize the path from the start point to the delivery point.
      Grid Visualization: The grid is displayed with obstacles, start point, delivery point, and the computed path.
      Algorithm Used: The application will display which algorithm (A* or Best First) was used for the current pathfinding task.
      Items Left: Displays the number of remaining paths to be computed.

  Application Workflow:
      Enter the start and delivery coordinates in the respective input fields.
      Click the "Deliver" button to compute and visualize the path.
      The grid will update to show the computed path and indicate which algorithm was used.
      You can perform up to 5 deliveries before the application indicates that all items have been delivered.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
Contact

For questions or feedback, please contact c2.tlhah@gmail.com.

Feel free to adjust any sections as needed, especially the links and contact information.
