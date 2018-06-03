# coding:utf8
"""
Run this file by python3, it automatically unzip or move files matched pattern to
dst_dir without file directory hierarchy.
"""
import os
import shutil
import zipfile
import re

PATTERN = '.*\.(mp4|avi|wmw|jpg|mkv)$'
MATCHER = re.compile(PATTERN, re.IGNORECASE)


def unzip_target_file(zip_file, dst_dir):
    if zipfile.is_zipfile(zip_file):
        with zipfile.ZipFile(zip_file, 'r') as my_zip:
            for member in my_zip.namelist():
                # filename could be decoded as cp437 as well in windows.
                filename = os.path.basename(member).encode('cp437').decode('gbk')
                if MATCHER.match(filename):
                    print('Target file matched！' + filename)
                    source = my_zip.open(member)
                    target = open(os.path.join(dst_dir, filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
    else:
        print('Invalid zipfile!')


def get_all_archives(src_dir):
    return [os.path.join(src_dir, item) for item in os.listdir(src_dir)
            if zipfile.is_zipfile(os.path.join(src_dir, item)) and item.endswith('zip')]


def mv_target_file(src_dir, dst_dir):
    for root, dirs, files in os.walk(src_dir):
        for filename in files:
            if MATCHER.match(filename):
                print('Target file matched！' + filename)
                source = os.path.join(root, filename)
                target = os.path.join(dst_dir, filename)
                shutil.move(source, target)


def main(src_dir=None):
    if not src_dir:
        src_dir = os.path.abspath(os.curdir)
    dst_dir = os.path.join(src_dir, 'unarchived')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    # Move all the target file under src_dir to dst_dir
    mv_target_file(os.path.join(src_dir, 'new'), dst_dir)
    # Unzip all the target file under src_dir to dst_dir
    for zip_file in get_all_archives(src_dir):
        print('zip file found!', zip_file)
        unzip_target_file(zip_file, dst_dir)


if __name__ == '__main__':
    main(src_dir=r'D:\MyDrivers\hotfix')
