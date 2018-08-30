# poc-base

This is base repository for PoC (Proof of Concept) code.

## Usage

### Preparation

```bash
$ git clone git@github.com:takp/poc-base.git
$ cd poc-base
$ pip install -r requirements.txt
$ cp .env.sample .env
```

### Add your code

Add your code to `app/task.py`. 

#### __init__: Initialize task instance 

```python
 def __init__(self):
 
    self.context.logger.debug("Initiate task...")

    super().__init__()
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

For more detail implement, please check task example here [Examples](./examples)

### Framework API

#### Logging

You can output logs with `self.context.logger`.

For further logging usage. Please check [here](https://docs.python.org/3.6/library/logging.html)

```python
self.context.logger.debug("debug")
self.context.logger.info("info")
```

#### Env var

You can access to environment variables with `self.context.config`.

```dotenv
ENV=local
```
```python
self.context.config.get("ENV") # local
```

#### Command Line Arguments

You can access to arguments through `self.args` after set your arguments through `set_arguments` method.

Adding command line arguments.
```python
parser.add_argument('--model', dest="model_path", help='set model path')
```

Framework uses ArgumentParser in background. You can check usage of ArgumentParser [here](https://docs.python.org/3.6/library/argparse.html#argparse.ArgumentParser)

Get command line arguments
```python
model_path = self.args.model_path
```

### Add your environment variables to `.env` file.

```dotenv
ENV=develop
```

### Run

```bash
$ python main.py
```
