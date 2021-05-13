import requests
import json
import datetime
import pytz
import os

api = 'https://zapus.me/api/v1'


def post(action, header, body):
    return requests.post(api + action, headers=header, data=json.dumps(body))


def get(action):
    return requests.get(api + action)


def logs(file, method, log):
    date_time = datetime.datetime.now()
    timezone = pytz.timezone("America/Sao_Paulo")
    date_time = timezone.localize(date_time)

    if not os.path.exists('./logs'):
        os.makedirs('./logs')

    file = open('./logs/' + file + '_' + date_time.strftime("%d_%m_%Y") + '.log', 'a+', encoding='utf-8')
    file.write('|- START register ----------------------------------------------------------------- -|\n')
    file.write('dateTime: ' + date_time.strftime("%d-%m-%Y %H:%M:%S") + '\n')
    file.write('method: ' + method + '\n')
    file.write('log: ' + json.dumps(log.json(), ensure_ascii=False) + '\n')
    file.write('|- END register ------------------------------------------------------------------- -|\n\n')
    file.close()
