import os

default_dir = 'test'

for dirfile in os.listdir(default_dir):
    check_dirfile = os.path.join(default_dir, dirfile)
    print(check_dirfile, os.path.isfile(check_dirfile))

for dirfile in os.listdir(default_dir):
    check_dirfile = os.path.join(default_dir, dirfile)
    if os.path.isfile(check_dirfile):
        print(f'{check_dirfile} is a file.')    