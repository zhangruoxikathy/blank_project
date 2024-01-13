"""This module demonstrate the use of environment variables to specify
project configurations

The precedence of environment variables is the following:
  1. Use locally defined variables
  2. Use globally defined variables
  3. Use variables defined in .env
  4. Use default values defined in config.py

In Windows,
```
:: Default variables, or those in .env take precedence:
python demo_environment_variables.py

:: Now, set environment variables globally. These will take
:: precedence over those in .env
set DATA_DIR=../somedir/
set OUTPUT_DIR=../otherdir/
python demo_environment_variables.py

:: Unset variables if so desired. 
set DATA_DIR=
set OUTPUT_DIR=
```

In Unix-like machines, this can easily be done on a single line so
that the environment variables don't persist (are not set globally),
```
DATA_DIR=../somedir/ OUTPUT_DIR=../otherdir/ python demo_environment_variable.py
```
"""
import config
print(config.data_dir)
print(config.output_dir)
