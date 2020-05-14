import time
import datetime
import sys
from pynput.mouse import Button, Controller
class Autostreaming(object):

    def __init__(self):
        self.mouse = Controller()
        pass

    def startstreaming(self):
        #load text file
        # time_file = open("time.txt", "r")
        # time_list = ('05-03-2020 21:25:00 10',
        #              '05-03-2020 22:00:00 20',
        #              '05-03-2020 22:30:00 30')
        time_tuple = ('04-05-2020 09:30:00 40',
                     '04-05-2020 12:30:00 40',
                     '04-05-2020 15:30:00 40',
                     '04-05-2020 22:30:00 40')

        # for date_time_duration in time_file.readlines():
        for date_time_duration in time_list:
        
        # like 04-05-2020 09:30:00 40
            input_date,input_time,input_duration=date_time_duration.split(' ')
        # input_date = 04-05-2020
        # input_time = 09:30:00
        # input_duration = 40
        # input_date = '05-03-2020'
        # input_time = '21:13:00'
        # input_duration = 2

            current_datetime = datetime.datetime.now()
            current_date = current_datetime.strftime('%d-%m-%Y')
            if input_date>= current_date:
                while(True):
                    _time = datetime.datetime.now()
                    current_time= _time.strftime('%H:%M:%S')
                    if(input_time==current_time):
                        print('trust I fiddled with the mouse')
                        time.sleep(int(input_duration)*60)
                        break
                    elif(input_time>current_time):
                        print('Waiting for the next stream to start at {}'.format(input_time)+" hrs on {}".format(input_date))
                        time.sleep(1)
                        continue
                    elif(input_date>current_date and input_time<current_time):
                        print('Waiting for the next stream to start at {}'.format(input_time)+" hrs on {}".format(input_date))
                        time.sleep(1)
                        continue
                    else:
                        break
                else:
                    pass

        _msg = "All streaming task finished"
        return _msg

    def stopstreaming(self):
        print("streaming stopped")
        return sys.exit()


start_streaming = Autostreaming()
start_streaming.startstreaming()