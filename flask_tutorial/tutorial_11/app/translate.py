from flask_babel import _
from app import app
import os, requests, uuid, json


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation key is not configured.')
    if 'MS_TRANSLATOR_ENDPOINT' not in app.config or \
            not app.config['MS_TRANSLATOR_ENDPOINT']:
        return _('Error: the translation endpoint is not configured.')
    headers = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
               'Content-type': 'application/json',
               'X-ClientTraceId': str(uuid.uuid4()),
               }

    path = '/translate?api-version=3.0'
    body = [{'text': text}]
    r = requests.post(f"{app.config['MS_TRANSLATOR_ENDPOINT']}"
                     f"{path}"
                     f"&to={source_language}&to={dest_language}",
                      headers=headers, json=body)
    print(f"{app.config['MS_TRANSLATOR_ENDPOINT']}"
                     f"{path}"
                     f"&to={source_language}&to={dest_language}")
    response = r.json()
    print(response)

    #r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
    #                 '/Translate?text={}&from={}&to={}'.format(
    #                     text, source_language, dest_language),
    #                 headers=headers)


    if r.status_code != 200:
        #return _('Error: the translation service failed.')
        pass
    return json.loads(r.content.decode('utf-8-sig'))

def translateB():
    # -*- coding: utf-8 -*-

    # This simple app uses the '/translate' resource to translate text from
    # one language to another.

    # This sample runs on Python 2.7.x and Python 3.x.
    # You may need to install requests and uuid.
    # Run: pip install requests uuid

    import os, requests, uuid, json

    key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
    if not key_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
    subscription_key = os.environ[key_var_name]

    endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
    if not endpoint_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
    endpoint = os.environ[endpoint_var_name]

    # If you encounter any issues with the base_url or path, make sure
    # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
    path = '/translate?api-version=3.0'
    params = '&to=de&to=it'
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        "Ocp-Apim-Subscription-Region": "westeurope",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': 'Hello World!'
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))