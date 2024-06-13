import urllib.request

def lambda_handler(event, context):
    url = f'http://localhost:2772/applications/TestAppConfig/environments/dev/configurations/TestConfigProfile'
    config = urllib.request.urlopen(url).read()
    return config