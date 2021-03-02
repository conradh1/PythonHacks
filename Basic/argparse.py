#!/bin/env python

import argparse
import sys


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    #parser.add_argument('list_fqdn')
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('--dump', action='store_true', default=False)
    action_group.add_argument('--set', help='set single setting in a form: <setting_name>=<setting_value>')
    action_group.add_argument('--update', help='update settings with contents of the file provided')
    
    args = parser.parse_args()

    if args.dump:
         print "dump"
    elif args.set:
        print "set"
        #(setting, value) = args.set.split('=', 1)
        
    elif args.update:
        if args.update == '-':
            f = sys.stdin
        #else:
            #f = open(args.update, 'r')
        #updated_settings = json.loads(f.read())
        #update_settings(ml, updated_settings)
        #if args.update != '-':
            #f.close()

