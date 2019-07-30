import json
import os
import ipaddress

def lambda_handler(event, context):
    #Logic goes here. The below code is just a dummy.

    ip = event['headers']['X-Forwarded-For']
    if (validate_ipaddress(ip) == False):
        return {
            'statusCode': 302,
            'headers': {
                "Location" : "https://www.abhaisasidharan.xyz"
            }
        }
    result = os.popen("curl https://ipinfo.io/" + ip).read()
    sites = dict([('IN', 'react.abhaisasidharan.xyz'), ('US', 'ng.abhaisasidharan.xyz'), ('any', 'vue.abhaisasidharan.xyz')])
    result_json = json.loads(result)
    
    if (result_json['country'] == 'IN'):
        redirect_to = 'https://react.abhaisasidharan.xyz'
    elif (result_json['country'] == 'US'):
        redirect_to = 'https://ng.abhaisasidharan.xyz'
    else:
        redirect_to = 'https://vue.abhaisasidharan.xyz'

    return {
        'statusCode': 302,
        'headers': {
            "Location" : redirect_to
        }
    }
    
def validate_ipaddress(ip):
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        ipaddress.ip_address(ip)
        return True
    except ValueError as errorCode:
        pass
        return False
