#!/usr/bin/python

'''This script is to use to compare a list of systems which have connected to Sophos against the list of systems in AMP.'''

sophosdevices = open("/home/vicki/SophosDevices", "r")
sophoslist = sophosdevices.read().splitlines()

AMPdevices = open("/home/vicki/AMPlist", "r")
AMPlist = AMPdevices.read().splitlines()

sophos_only = [name1 for name1 in sophoslist if name1 not in AMPlist]
for result in sophos_only:
    print(result.strip('"'))
