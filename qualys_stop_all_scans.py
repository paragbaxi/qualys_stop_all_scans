import qualysapi
from lxml import objectify

q = qualysapi.connect()
response = q.request('/api/2.0/fo/scan/',{'action': 'list','state':'Running'})
root = objectify.fromstring(bytes(response, encoding='utf-8'))
# Iterate scans and store scan references.
for scan in root.RESPONSE.SCAN_LIST.SCAN:
    print(f'Canceling {scan.TITLE.text}: {scan.REF.text}...')
    response = q.request('/api/2.0/fo/scan/',{'action': 'cancel','scan_ref': scan.REF.text})
    print(response)
