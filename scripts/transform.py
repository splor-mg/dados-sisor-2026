from frictionless import Package
import petl as etl
import logging
from scripts.pipelines import transform_pipeline
from dpm.utils import as_identifier

logger = logging.getLogger(__name__)

def transform_resource(resource_name: str, source_descriptor: str = 'datapackage.yaml', target_descriptor: str = 'datapackage.json'):
    logger.info(f'Transforming resource {resource_name}')
    
    package = Package(source_descriptor)
    resource = package.get_resource(resource_name)
    resource.transform(transform_pipeline)
    table = resource.to_petl()
    for field in resource.schema.fields:
        target = field.custom.get('target')
        target = target if target else as_identifier(field.name, case=str.lower)
        table = etl.rename(table, field.name, target)
    etl.tocsv(table, f'data/{resource.name}.csv', encoding='utf-8')
