## NVCC Plugin for Jupyter notebook
- Load Extension
> `%load_ext nvcc_plugin`

- Mark a cell to be treated as cuda cell
> `%%cuda --name example.cu --compile false`
>> NOTE: The cell must contain either code or comments to be run successfully. 
>> It accepts 2 arguments. `-n` | `--name`  - which is the name of either CUDA source or Header
>> The name parameter must have extension `.cu` or `.h`
>> Second argument `-c` | `--compile`; default value is `false`. The argument is a flag to specify
>> if the cell will be compiled and run right away or not. It might be usefull if you're playing in
>> the `main` function

- To compile and run all CUDA files you need to run
```
%%cuda_run
# This line just to bypass an exeption and can contain any text
```

### Credit
This repo is forked from https://github.com/andreinechaev/nvcc4jupyter 

### Patched
The plugin in this repo was patched in order to work with COSC 407 assignments, specifically A6 and A7
