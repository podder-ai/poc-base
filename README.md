# poc-base

This is base repository for PoC (Proof of Concept) code.
Boilerplate project for creating python task using the [Pipeline-framework](https://github.com/podder-ai/pipeline-framework).

## How to implement your code

### Source code directory

```
$ tree . -L 2
.
├── Dockerfile
├── README.md
├── app
│   └── task.py   # main task implementation
├── data
├── envs
│   └── env.example
├── framework     # framework codes
│   ├── api
│   ├── config.py
│   ├── context.py
├── main.py
├── requirements
│   ├── requirements.develop.txt
│   └── requirements.txt    # add required packages here
├── run_codegen.py
├── scripts
│   ├── entrypoint.sh
│   └── pre-commit.sh       # execute before committing your codes
├── tests
│   └── test_task.py        # add unit test here
└── tmp                     # where to put your data 
```

### How to implement a task class

Add your code to `app/task.py`. 

#### Implementation sample

Please check task sample here [Sample](https://github.com/podder-ai/poc-base-sample)

#### __init__: Initialize task instance 

```python
def __init__(self, context: Context) -> None:
    self.context.logger.debug("Initiate task...")
    super().__init__(context)
```

#### execute: Main process

```python
def execute(self) -> None:

    self.context.logger.debug("START processing...")
    
    self.yourProcess(self.args.input_path)
    
    self.context.logger.debug("Completed.")
        
```

#### set_arguments: Arguments

```python
def set_arguments(self, parser) -> None:
    
    parser.add_argument('--input_path', dest="input_path", help='set input path', default='.')

```

### Framework API

Some framework APIs you can use for your implementation.

#### Logging

You can output logs with `self.context.logger`. `logger` is just a wrapper of logging. For further logging usage, please check [here](https://docs.python.org/3.6/library/logging.html)

```python
self.context.logger.debug("debug")
self.context.logger.info("info")
```

#### Command Line Arguments

You can access to arguments through `self.args` after set your arguments through `set_arguments` method.

Adding command line arguments implementation
```python
parser.add_argument('--model', dest="model_path", help='set model path')
```

Framework uses ArgumentParser in background. You can check usage of ArgumentParser usage [here](https://docs.python.org/3.6/library/argparse.html#argparse.ArgumentParser)

Get command line arguments
```python
model_path = self.args.model_path
```

#### Shared directory

You can use `shared` directory for storing your data. 

```bash
$ tree -L 1 ./shared
shared
├── data
└── tmp
```

- `shared` directory

You can get absolute path to `shared` directory by `self.context.file.get_shared_path`.

```python
self.context.file.get_shared_path('sample.csv')
# => /path/to/shared/sample.csv
```

- `shared/data` directory: `self.context.file.get_data_path`

Please use `shared/data` directory for storing your necessary data.

```python
self.context.file.get_data_path('sample.csv')
# => /path/to/shared/data/sample.csv
```

- `shared/tmp` directory

Please use `shared/tmp` directory for storing temporary files.

```python
self.context.file.get_tmp_path('sample-tmp.csv')
# => /path/to/shared/tmp/sample-tmp.csv
``` 

### Run

Run your task with argument
```bash
$ python main.py --inputs /path/to/input/a /path/to/input/b
```

## How to run your code

### For Mac os, Linux user

```bash
# clone poc-base
$ git clone git@github.com:podder-ai/poc-base.git
$ cd poc-base
# enable python3
$ python3 -m venv env
$ source env/bin/activate
# install required libraries
$ pip install -r requirements.txt
# run sample code
$ python main.py --inputs /path/to/input/a /path/to/input/b
```

### For Windows user with PowerShell

If using Powershell, the activate script is subject to the execution policies on the system. By default on Windows 7, the system's excution policy is set to `Restricted`, meaning no scripts as virtualenv activation script are allowed to be executed. 

In order to use the script, you can relax your system's execution policy to `Unrestricted`, meaning all scripts on the system can be executed. As an administrator run:

```
C:\>Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force -Verbose
```

```bash
# clone poc-base
C:\> git clone git@github.com:podder-ai/poc-base.git
C:\> cd poc-base
# enable python3
C:\>python3 -m venv C:\path\to\myenv
# Windows cmd.exe
C:\> C:\path\to\myenv\Scripts\activate.bat
# PowerShell PS
C:\> C:\path\to\myenv\Scripts\Activate.ps1
# install required libraries
C:\> pip install -r requirements.txt
# run sample code
C:\> python main.py --inputs /path/to/input/a /path/to/input/b
```

### Via Docker

To skip python environment setting, we are using Docker to run task. 
For detail Dockerfile check [here](./Dockerfile)


```bash
# build docker image with python enviroment
$ docker build -t poc-sample .

# run code
$ docker run -ti poc-sample python main.py --inputs /path/to/input/a /path/to/input/b
```

## Linter, Formatter and Unit Test
Please execute linters, formatters and unit tests before committing your source codes.

### How To Execute
You can execute them by the following command.
Make sure that you are under the root directory of your project. (e.q. poc-base/)
```
$ pip install -r ./requirements/requirements.develop.txt
$ sh ./scripts/pre-commit.sh
```

### Supported Libraries
#### Linter
- flake8
#### Formatter
- autopep8
- yapf
- autoflake
- isort
#### Unit Test
- pytest

### Rules of Development
Please follow the official documents of the libraries.


## Implementation note

Finally, your task implementation will be integrated to Pipeline-framework and deploy using Docker/Kubernetes.
To make it easier, please follow this implementation rules below.

- Only add your code to `app/task.py`
- Put your data set or model files to `data`
- Your task implementation will be compiled by Cython in integrating. Please don't use `__file__` in your code.
- Create virtual environment for your code. Please check [Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Please add issue & pull request if you have any request!


