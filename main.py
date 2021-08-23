import requests


def sms(contact, message):
    url = "https://messagingsuite.smart.com.ph/cgphttp/servlet/sendmsg"

    payload = {
        "destination": contact,
        "text": message
    }

    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Authorization': os.environ.get('TOKEN')}

    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)


if __name__ == '__main__':
    mobile_number = ""
    body = ""
    sms(mobile_number, body)

