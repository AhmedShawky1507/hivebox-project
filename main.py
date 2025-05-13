import requests
print(requests.get('https://semver.org/').text.split('Semantic Versioning ')[1].split('<')[0])