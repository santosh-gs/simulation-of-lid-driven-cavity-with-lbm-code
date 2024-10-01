# Multi-Processing Simulation of a Lid Driven Cavity using LBM

### Simulation Results
These are the results obtained using the Cython code for 60X60 Nodes at Reynolds Number = 3000.

#### Time Step: 2000, 10000, 40000, 60000, 100000

<div style="display: flex; justify-content: space-between;">

  <img src="https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%202000.png?raw=true" width="50%" />
  <img src="https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2010000.png?raw=true" width="50%" />

</div>

<div style="display: flex; justify-content: space-between;">

  <img src="https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2040000.png?raw=true" width="50%" />
  <img src="https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%2060000.png?raw=true" width="50%" />
</div>

<div style="display: flex; justify-content: center;">

  <img src="https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code/blob/main/results/Re%203000%20and%20t%20100_000.png?raw=true" width="50%" />

</div>

### Requirements
These are the tested environment specifications:
* Python 3.9.13
* Cython 0.29.33
* NumPy 1.21.6
* Setuptools 58.1.0
* Matplotlib 3.4.1
* Microsoft C++ Build Tools 2014 or later [(2022)](https://visualstudio.microsoft.com/visual-cpp-build-tools/) [(Instructions)](https://github.com/bycloudai/InstallVSBuildToolsWindows)

### Instructions
#### Python
* Files: `lbm_final.py`
* Define the simulation parameters in the `Allocate_Memory()` function.
* Run the python file to generate `UV_Serial_Iterations.plt` (tab-separated numerical data in a text file).
* Analyze the data using `lbm_output.py` or MATLAB.

#### Cython
* Clone the repo: `git clone https://github.com/santosh-gs/simulation-of-lid-driven-cavity-with-lbm-code.git`
* Or add the following files to a folder: `LBM_Cython.pyx` `LBM_Cython.py` `setup.py`
* Open the cloned or defined folder in VS Code or any code editor. Alternatively, navigate to the folder in a terminal.
* Define the simulation parameters in the `LBM_Cython.pyx`.
* Run `python setup.py build_ext --inplace` in the terminal of the code editor.
* A `.pyd` file will be generated after successful compilation in case of Windows.
* For macOS and Linux, a `.so` (shared object) file will be generated.
* Now run the `LBM_Cython.py` python file to generate `UV_Cython.plt`.
* Analyze the data using `lbm_output.py` or MATLAB.
