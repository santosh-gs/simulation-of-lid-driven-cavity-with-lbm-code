# Multi-Processing Simulation of a Lid Driven Cavity using LBM

### Simulation Results
These are the results obtained using the Cython code for 60X60 Nodes at Reynolds Number = 3000.

#### Time Step: 2000
![t2000](https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%202000.png?raw=true)

#### Time Step: 10000
![t10000](https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2010000.png?raw=true)

#### Time Step: 40000
![t40000](https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2040000.png?raw=true)

#### Time Step: 60000
![t60000](https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2060000.png?raw=true)

#### Time Step: 100_000
![t100000](https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%20100_000.png?raw=true)

### Requirements
These are the tested environment specifications:
* Python 3.9.13
* Cython 0.29.33
* NumPy 1.21.6
* Matplotlib 3.4.1
* Microsoft C++ Build Tools 2014 or later [(2022)](https://visualstudio.microsoft.com/visual-cpp-build-tools/) [(Instructions)](https://github.com/bycloudai/InstallVSBuildToolsWindows)

### Instructions
#### Python
* Files: `lbm_final.py`
* Define the simulation parameters in the `Allocate_Memory()` function.
* Run the python file to generate `UV_Serial_Iterations.plt` (data in a text file).
* Analyze the data using `lbm_output.py` or MATLAB.



