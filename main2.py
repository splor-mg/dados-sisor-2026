from frictionless.portals import CkanControl
from frictionless import Package

ckan_control = CkanControl(baseurl='https://homologa.cge.mg.gov.br/', apikey='INCLUIR-TOKEN')
package = Package('datapackage.json')
# package.owner_org = 'secretaria-de-estado-de-planejamento-e-gestao-seplag'
# breakpoint()
package.publish(control=ckan_control)
