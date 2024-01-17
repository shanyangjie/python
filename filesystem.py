import os
import shutil

def show_dir(path):
    print('====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))


tmpdir = '/Users/sy/Desktop/temp'

os.mkdir(tmpdir)
os.makedirs('/Users/sy/Desktop/temp/mkdir1/mkdir2/mkdir3')
# show_dir(tmpdir)

os.rmdir('/Users/sy/Desktop/temp/mkdir1/mkdir2/mkdir3')
# show_dir(tmpdir)

# os.removedirs(tmpdir)
shutil.rmtree(tmpdir)

shutil.copy('/Users/sy/Desktop/python/args.py', '/Users/sy/Desktop/dist.py')
shutil.copytree('/Users/sy/Desktop/python', '/Users/sy/Desktop/py_backup')