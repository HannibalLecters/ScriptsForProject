import os
import datetime
import time

path_to_folder = ('C:\\WG\\WoT_trunks\\win64\\Reports\\')

def start_script():

    while True:

        if len(os.listdir(path_to_folder)) == 0:
            print('Объекты не найдены')

        else:

            for f in (os.listdir(path_to_folder)):
                os.chdir(path_to_folder)
                print('Объект найден -->', f, datetime.datetime.fromtimestamp(os.path.getctime(f)).strftime('[%d %B, %Y, %H:%M:%S]'))
            break

        time.sleep(5)

start_script()
            
