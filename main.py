import datetime
import os
import pytz
import shutil

input_dir = './input/'
output_dir = './output/'

# Three Lines to Change Possibly
pxl_format = 'PXL_%Y%m%d_%H%M%S%f.mp4'
to_tz = pytz.timezone('Asia/Seoul')
from_tz = pytz.utc

file_extension = pxl_format.rsplit('.', 1)[1]


def fix_date():
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            dt = datetime.datetime.strptime(file, pxl_format).replace(tzinfo=from_tz)
            kr_dt_str = dt.astimezone(to_tz).strftime(pxl_format).replace('000.', '.')
            shutil.copy2(input_dir + file, output_dir + kr_dt_str)


if __name__ == '__main__':
    fix_date()
