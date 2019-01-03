import glob
import os
import shutil
import subprocess

from app import Task
from framework import Context

DAG_ID = 'dag_id'

'''
*** DO NOT DELETE!! ***
At least one unit test should be executed to pass building docker image job.

This is a unit test of task execute method with sample pdf files.
Refer the following url for more information about sample pdf files.
https://github.com/podder-ai/pdf-file-sample.git
'''

SAMPLE_GITHUB_URL = "https://github.com/podder-ai/pdf-file-sample.git"
SAMPLE_DATA_DIR = 'tests/podder_sample'
PDF_EXTENTION = '/**/*.pdf'

def test_with_sample_pdf():
    context = Context(DAG_ID)
    task = Task(context)
    data_path = context.file.get_data_path()
    sample_data_path = data_path + os.path.sep + SAMPLE_DATA_DIR

    # download sample pdf files
    context.logger.info('downloading sample pdf files ...')
    command = ["git", "clone", SAMPLE_GITHUB_URL, sample_data_path]
    subprocess.call(command)

    # get file path
    inputs = []
    for filename in glob.glob(
            sample_data_path + PDF_EXTENTION, recursive=True):
        inputs.append(filename.replace(data_path, ''))

    context.logger.info('executing task with sample pdf files ...')
    output = task.execute(inputs)
    context.logger.info(output)

    # delete sample data dir
    context.logger.info('deleting sample pdf files ...')
    shutil.rmtree(sample_data_path)
