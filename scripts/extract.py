from frictionless import Package
import logging
import requests
import shutil

logger = logging.getLogger(__name__)

def extract_resource(resource_name: str, descriptor: str = 'datapackage.yaml'):
    logger.info(f'Extracting resource {resource_name}')
    package = Package(descriptor)
    resource = package.get_resource(resource_name)
    res = requests.post(resource.custom['api_url'],
                        headers = {'User-Agent': 'splor'}, 
                        data = resource.custom['payload'], 
                        stream = True)
    res.raise_for_status()
    
    with open(resource.path, 'wb') as file:
        shutil.copyfileobj(res.raw, file)
