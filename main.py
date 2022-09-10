# This is a sample Python script.
import datetime
import os
import shutil

from dateutil import parser
import pytz

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
input = './input/'
output = './output/'
kr = pytz.timezone('Asia/Seoul')
utc = pytz.utc


def print_hi(name):
    for root, dirs, files in os.walk(input):
        for file in files:
            dt = datetime.datetime.strptime(file, 'PXL_%Y%m%d_%H%M%S%f.mp4').replace(tzinfo=datetime.timezone.utc)
            kr_dt_str = dt.astimezone(kr).strftime('PXL_%Y%m%d_%H%M%S%f.mp4').replace('000.mp4', '.mp4')
            shutil.copy2(input + file, output + kr_dt_str)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
