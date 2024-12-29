This is a simple example project showing a hardware module written in verilog and the tests written in python using cocotb.

1) Create a python virtual environment.
   On ubuntu this can be done using:
   `python3 -m venv ~/.envs/my_venv_name`
   This assume you have a folder `~/.envs` where you keep your python virtual environments and that you
   want to call the env `my_venv_name`.

2) Open the python virtual environment.
   `source ~/.envs/my_venv_name/bin/activate`

3) Install cocotb-test.  This will also install cocotb.
   `pip install cocotb-test`
   If you're missing dependencies see the cocotb installation instructions for help.

4) Install verilator.

5) Run the test.
   `python test_adder.py`.

