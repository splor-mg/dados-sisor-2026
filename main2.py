from frictionless.portals import CkanControl
from frictionless import Package

ckan_control = CkanControl(baseurl='https://homologa.cge.mg.gov.br/', apikey='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJRSEREbEEtSFBDVklEdzYwdlJ4WHI0VEM3UXltSldJZ1pTc3cxZEtFUm12cHNhLU5KTVBsRUdFM3VWcTUxbkpfeUpnVnpLX2dRS0t2VWkzUCIsImlhdCI6MTc0MzE5MDQ5MH0.nFcMQcti5sr2j7QPFmZkIbxA9Sols_aimeS_Za4tKY8')
package = Package('datapackage.json')
# package.owner_org = 'secretaria-de-estado-de-planejamento-e-gestao-seplag'
# breakpoint()
package.publish(control=ckan_control)
