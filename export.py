import requests
import csv

REPO = 'UUDigitalHumanitieslab/texcavator'

with open('issues.csv', 'wb') as f:
    writer = csv.writer(f, dialect='excel', delimiter=';')
    writer.writerow(['number', 'issue', 'state', 'labels', 'url'])

    p = {'state': 'all', 'sort': 'created', 'direction': 'asc', 'per_page': 100}
    r = requests.get('https://api.github.com/repos/{}/issues'.format(REPO), params=p)

    issues = []
    for issue in r.json(): 
        labels = []
        for label in issue['labels']: 
            labels.append(label['name'])

        issues.append([
            issue['number'], 
            issue['title'].encode('utf8'), 
            issue['state'], 
            ','.join(labels), 
            issue['html_url']
        ])

    writer.writerows(issues)
