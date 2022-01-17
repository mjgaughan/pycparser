import os 
import sys
import glob 
import func_defs



def recurse_down(root_dir):
    print(root_dir)
    print(os.getcwd())
    for filename in glob.glob(root_dir + '**/*.i', recursive=True):
        print(filename)
        func_defs.show_func_defs(filename)
        ''' 
        try:
            func_defs.show_func_defs(filename)
        except BaseException:
            print("oops! error in %s", filename)
        '''

if __name__ == '__main__':
    recurse_down('linux/')
