#!/usr/bin/python

import ConfigParser
import os
import sys
import syslog
import urllib
import urllib2

def logger(message,logtype=syslog.LOG_INFO):
    """
    Simple logger
    """
    syslog.syslog(logtype,message)
    print message

def readConfig(fileLocation):
    """
    Reads config at argument location
    """
    config = ConfigParser.ConfigParser()
    if config.read(fileLocation) == []:
        logger('ERROR: Cannot read config file.',syslog.LOG_ERR)
        quit()
    return config

def getFile(location):
    """
    gets file, or all files in a directory
    """
    if not os.path.exists(location):
        logger('Error: '+location+' does not exist.',syslog.LOG_ERR)
        quit()
    if os.path.isdir(location):
        for f in os.listdir(location):
            getFile(location+'/'+f)
    else:
        sendFile(location)

def sendFile(location):
    """
    post to web api
    """
    # get text
    f = open(location,'r')
    text = f.read()
    f.close()
    # send request
    values = {'file_name':location,'server_name':server,'file':text,'update_key':update_key}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req).read()
    except urllib2.HTTPError,msg:
        logger(str(msg),syslog.LOG_ERR)
        return 0
    # make sure api returns correctly
    if response != 'ok\n':
        logger('ERROR: File input error: '+location,syslog.LOG_ERR)
    logger('Sent '+location+' successfully.')

if __name__ == '__main__':
    # make sure file was specified
    if len(sys.argv) < 2:
        print "Run like config.py /path/to/config/file"
        quit()
    config = readConfig(sys.argv[1])

    # get settings
    try:
        url = config.get('settings','url')
        server = config.get('settings','server')
        update_key = config.get('settings','key')
        files = config.get('settings','files').split(',')
    except ConfigParser.NoOptionError,msg:
        logger('ERROR: {0} not given in {1} section.'.format(msg.option,msg.section),syslog.LOG_ERR)

    # go through list 
    for f in files:
        getFile(f)