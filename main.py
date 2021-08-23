import requests


def sms(contact, message):
    url = "https://messagingsuite.smart.com.ph/cgphttp/servlet/sendmsg"

    payload = {
        "destination": contact,
        "text": message
    }

    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Authorization': 'Basic cG5wLnByYnNAcG5wLmdvdi5waDpQcmJzQDIwMjE='}

    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)


if __name__ == '__main__':
    sms("09168845698", "Testing lang e hahaha kevs to")

