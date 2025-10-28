AI Experiments - Instructions
=============================

Author: Jayesh  
Repository: https://github.com/jayesh-oss/ai  
Language: Python 3.10+ and Prolog  
Purpose: Collection of Artificial Intelligence practical experiments and implementations.


------------------------------------------------------------
1. Setup Instructions
------------------------------------------------------------

Before running any Python experiment, make sure the following are installed:

Required Libraries:
-------------------
pip install numpy<2 pandas networkx matplotlib pgmpy==0.1.24

(NumPy version must be below 2 to avoid compatibility issues with pgmpy and torch.)


------------------------------------------------------------
2. How to Run Python Programs
------------------------------------------------------------

1. Open PowerShell or Command Prompt.
2. Navigate to the project folder:
   cd "C:\Users\Jayesh\Documents\Prolog"

3. Run the experiment file using Python:
   python "filename.py"

   Example:
   python "hill climbing.py"
   python "bayesian network.py"
   python "min max.py"

If you see "ModuleNotFoundError", install the missing library using:
   pip install library_name


------------------------------------------------------------
3. How to Run Prolog Programs
------------------------------------------------------------

1. Open SWI-Prolog.
2. Load the file:
   ?- [filename].

3. Run the main goal:
   ?- start.
   (or any other predicate defined in the code)

Example:
   ?- [bfs].
   ?- path(a, b).


------------------------------------------------------------
4. Experiments Included
------------------------------------------------------------

1. Experiment 1 - Uninformed Search (BFS / DFS)
2. Experiment 2 - Informed Search (A* Algorithm)
3. Experiment 3 - Minimax Algorithm (Tic Tac Toe AI)
4. Experiment 4 - Hill Climbing Algorithm
5. Experiment 5 - Bayesian Network (Heart Disease Prediction)
6. Experiment 6 - Constraint Satisfaction / Graph Problems
7. Experiment 7+ - Additional AI logic implementations in Python and Prolog


------------------------------------------------------------
5. Common Issues & Fixes
------------------------------------------------------------

Error: ModuleNotFoundError: No module named 'numpy'
Fix: pip install numpy<2

Error: ImportError: cannot import name 'BayesianModel'
Fix: pip install pgmpy==0.1.24

Error: NumPy 2.x incompatibility
Fix: pip install "numpy<2" --force-reinstall


------------------------------------------------------------
6. Credits
------------------------------------------------------------

Developed by: Jayesh  
Subject: Artificial Intelligence Lab Experiments

------------------------------------------------------------
End of README
------------------------------------------------------------
