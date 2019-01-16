from typing import Any, List, Dict

'''
This service is only used for main.py/
'''
class InputsService(object):

    def create(context: Context) -> List:
    json_data = read_json(context)
    inputs = []
    for job_data in enumerate(json_data):
        inputs.append({
            "job_id": str(uuid.uuid4()),
            "job_data": job_data
        })
    return inputs

    def read_json(context: Context) -> List:
        json_path = context.config.get('inputs')[0]
        with open(json_path) as f:
            return json.load(f)
