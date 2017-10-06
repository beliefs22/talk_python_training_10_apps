import get_report
import get_token
import requests
import json


def main():

    get_report.print_the_header()
    url = 'http://api.wunderground.com/api/{token}/{features}/{settings}/q/{query}.{format}'

    code = input('What zipcode do you want the weather for (21234)? ')

    payload = {'token': get_token.get_token(),
               'features': 'conditions',
               'settings': 'lang:EN',
               'query': code,
               'format': 'json'
               }
    if get_report.check_api_use_rate():
        data = requests.get(url.format(**payload))
        if data.status_code == requests.codes.ok:
            fout = open('weather.json', 'w')
            weather_json = json.loads(data.text)
            print(weather_json, file=fout)
            get_report.print_report(weather_json)
    else:
        print("Please wait until your API calls have reset")


if __name__ == '__main__':
    main()
