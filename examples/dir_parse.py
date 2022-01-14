import os 
import sys
import glob 
import func_defs



def recurse_down(root_dir):
    for filename in glob.glob(root_dir + '**/*.c', recursive=True):
        print(filename)
        func_defs.show_func_defs(filename)



if __name__ == '__main__':
    recurse_down('../')
