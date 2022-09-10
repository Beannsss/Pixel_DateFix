import datetime
import os
import shutil
import pytz

input_dir = './input/'
output_dir = './output/'
kr = pytz.timezone('Asia/Seoul')
utc = pytz.utc


def fix_date():
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            dt = datetime.datetime.strptime(file, 'PXL_%Y%m%d_%H%M%S%f.mp4').replace(tzinfo=datetime.timezone.utc)
            kr_dt_str = dt.astimezone(kr).strftime('PXL_%Y%m%d_%H%M%S%f.mp4').replace('000.mp4', '.mp4')
            shutil.copy2(input_dir + file, output_dir + kr_dt_str)


if __name__ == '__main__':
    fix_date()
