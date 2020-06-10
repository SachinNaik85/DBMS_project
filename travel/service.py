import smtplib
from essential import gmail
import random


def shorten_mail(email):
    lst = email.split('@')
    email = lst[0][:3]
    for i in range(3, len(lst[0])):
        email += '*'
    email += lst[1]
    return email


def send_email(reciever):
    # creates SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(gmail['sender'], gmail['password'])

        # message to be sent
        secret_key = random.randint(100000, 999999)
        subject = "YES TRAVELS password reset code"
        text = f"Hello Sir/Madam \n use this code for resetting your password\n {secret_key}"
        message = 'Subject: {}\n\n{}'.format(subject, text)

        # sending the mail
        s.sendmail(gmail['sender'], reciever, message)

        # terminating the session
        s.quit()
        return secret_key
    except Exception as e:
        print('error in sending mail')


def read_status():
    file = open('travel/login_status.txt', 'r')
    file_data = file.read()
    file_data = file_data.split()
    status = bool(int(file_data[0]))
    file.close()
    return status


def write_status(status, name):
    file = open('travel/login_status.txt', 'w')
    line = int(status)
    file.writelines(str(line))
    file.writelines('\n')
    file.writelines(str(name))
    file.close()
    return


def read_name():
    file = open('travel/login_status.txt', 'r')
    try:
        file_data = file.read()
        file_data = file_data.split()
        name = str(file_data[1])
        return name
    except IndexError as e:
        print(e)
    finally:
        file.close()


def buses():
    class Bus:
        busname : str
        journey_date : str
        amount : str
        seats : str
        booking_time : str
        booking_date : str
        departure : str
        arrival : str
    list = []
    for i in range(2):
        bus = Bus()
        bus.busname = 'VRL7266'
        bus.journey_date = '10-06-2020'
        bus.amount = '2000 INR'
        bus.seats = '2'
        bus.booking_date = '01-06-2020'
        bus.booking_time = '06:30 PM'
        bus.departure = '09:30 PM'
        bus.arrival = '07:00 AM'
        list.append(bus)
    return list


def hotels():
    return None