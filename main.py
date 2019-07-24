import subprocess, datetime, time, os, logging
import win32com.client as win32

def ping(host):
    response = os.system('ping -n 1 ' + host)

    if response == 0:
        return "up"
    else:
        return 'down'

services_list = ['srv2',
#                '2',
#                '3',
                'googjjle.com'
                ]

def add_log_entry(host, status):
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logging.info(' {} - host {} is {}'.format(str(datetime.datetime.now())[:-7], host, status))


def send_warning(service):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'it@teplopribor.ru'
    mail.Subject = 'Service {} is down'.format(service)
    mail.Body = 'Service {} is down at {}'.format(service, str(datetime.datetime.now())[:-7])
    mail.HTMLBody = 'Service {} is down at {}'.format(service, str(datetime.datetime.now())[:-7]) #this field is optional

    # To attach a file to the email (optional):
#    attachment  = "Path to the attachment"
#    mail.Attachments.Add(attachment)

    mail.Send()

def pinging():
    while True:
        for service in services_list:
            resp = ping(service)
            add_log_entry(service, resp)
            if resp =='down':
                send_warning(service)
        time.sleep(10)

if __name__ == '__main__':
    pinging()
