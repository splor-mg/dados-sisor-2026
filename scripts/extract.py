from frictionless import Package
import logging
import requests
import shutil

logger = logging.getLogger(__name__)

def extract_resource(resource_name: str, descriptor: str = 'datapackage.yaml', raise_on_error: bool = False):
    package = Package(descriptor)
    resource = package.get_resource(resource_name)
    try:
        res = requests.post(
            resource.custom['api_url'],
            headers={'User-Agent': 'splor'},
            data=resource.custom['payload'],
            stream=True
        )
        res.raise_for_status()
        with open(resource.path, 'wb') as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as e:
        with open("logfile.log", "a") as log:
            log.write(f'Recurso não encontrado: {resource_name}\n')
        if raise_on_error:
            raise
