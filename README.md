# podder-task

This is base repository for PoC (Proof of Concept) code.
Boilerplate project for creating python task using the [podder-pipeline](https://github.com/podder-ai/podder-pipeline).

## How to implement your code

### Source code directory

```
$ tree . -L 2
.
├── Dockerfile
├── README.md
├── api
│   ├── __init__.py
│   ├── grpc_server.py
│   ├── protos
│   └── task_api.py
├── app
│   ├── __init__.py
│   └── task.py             # main task implementation
├── inputs.json
├── main.py
├── requirements
│   ├── requirements.develop.txt
│   └── requirements.txt    # add required packages here
├── run_codegen.py
├── scripts
│   ├── entrypoint.sh
│   └── pre-commit.sh       # execute before committing your codes
├── shared
│   ├── data
│   └── tmp
└── tests
    └── test_task.py        # add unit test here
```

### How to implement a task class

Add your code to `app/task.py`.

#### Implementation sample

Please check task sample here [Sample](https://github.com/podder-ai/podder-task-sample)

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

### API

`podder-task-base` python module provides many APIs for the development.

#### Logging

You can output logs with `self.context.logger`. `logger` is just a wrapper of logging. For further logging usage, please check [here](https://docs.python.org/3.6/library/logging.html)

```python
self.context.logger.debug("debug")
self.context.logger.info("info")
```

#### Command Line Arguments

You can add your own command line argument using `self.context.config.set_argument` within `task.py`.

After you execute with command line arguments, you can access to the passed arguments through `self.context.config.get`.

For example, set `--model` to command line argument.

```python
# Set your command line argument
def set_arguments(self) -> None:
    self.context.config.set_argument('--model-path', dest="model_path", help='set model path')
```

```bash
# Execute main.py with argument "--model"
$ python main.py --model-path /path/to/model
```

```python
# You can access to the value passed to "--model"
def execute(self, inputs: List[Any]) -> List[Any]:
    model = self.context.config.get('model_path')
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
# clone podder-task
$ git clone git@github.com:podder-ai/podder-task.git
$ cd podder-task
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
# clone podder-task
C:\> git clone git@github.com:podder-ai/podder-task.git
C:\> cd podder-task
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
$ docker build -t podder-task-sample .

# run code
$ docker run -ti podder-task-sample python main.py --inputs /path/to/input/a /path/to/input/b
```

## Configuration

Copy and create `.env` file and add your env variables.

```bash
$ cp .env.sample .env
```

## Linter, Formatter and Unit Test

Please execute linters, formatters and unit tests before committing your source codes.

### How To Execute

You can execute them by the following command.
Make sure that you are under the root directory of your project. (e.q. podder-task/)
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

Finally, your task implementation will be integrated to Podder-Pipeline and deploy using Docker/Kubernetes.
To make it easier, please follow this implementation rules below.

- Only add your code to `app/task.py`
- Put your data set or model files to `data`
- Your task implementation will be compiled by Cython in integrating. Please don't use `__file__` in your code.
- Create virtual environment for your code. Please check [Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Please add issue & pull request if you have any request!
