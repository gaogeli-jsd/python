import os

default_dir = "test"
check_exist = ['from', 'dir1', 'text1.txt', 'dir3', 'text3.txt']

for check_dirfile_name in check_exist:
    check_dirfile_path = os.path.join(default_dir, check_dirfile_name)
    print(check_dirfile_path, os.path.exists(check_dirfile_path))