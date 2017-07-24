#!/bin/env python

__author__ = "John Hover, Jose Caballero"
__copyright__ = "2017 John Hover"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9.1"
__maintainer__ = "John Hover"
__email__ = "jhover@bnl.gov"
__status__ = "Production"

# Factory tarball
# http://dev.racf.bnl.gov/dist/src/tgz/autopyfactory-2.4.10.tar.gz
import os
import sys
import logging
from urlparse import urlparse
from optparse import OptionParser
from ConfigParser import SafeConfigParser
from vc3client.client import VC3ClientAPI, InfoMissingPairingException

class ResourceTool(object):
    
    def __init__(self, config, options):
        self.log = logging.getLogger() 
        self.log.debug('ResourceTool starting...')

        self.config  = config
        self.options = options

        self.client = VC3ClientAPI(self.config)

        #self.certfile = self.options.cert;
        #self.keyfile  = self.options.key;

        self.write_keys()

    def  write_keys(self):
        try:
                (cert, key) = self.client.getPairing(self.options.pin)
                print(cert)
                print("")
                print(key)
                #certpath = os.path.expanduser(options.certfile)
                #keypath = os.path.expanduser(options.keyfile)
                #cf = open(certpath, 'w')
                #cf.write(cert)
                #cf.close()
                #if os.path.isfile(keypath):
                #    os.remove(keypath)
                #original_umask = os.umask(0o177)  # 0o777 ^ 0o600
                #try:
                #    kf = os.fdopen(os.open(keypath, os.O_WRONLY | os.O_CREAT, 0o600), 'w')
                #finally:
                #    os.umask(original_umask)
                #kf.write(self.key)
                #kf.close()                
        except InfoMissingPairingException:
            print("Invalid pairing code or not satisfied yet. Try in 30 seconds.")   

class ResourceToolCLI(object):
    
    def __init__(self):
        logging.basicConfig()
        self.log = logging.getLogger()
        self.log.debug('ResourceToolCLI starting...')
        self._parseopts()
        


    def _parseopts(self):
        parser = OptionParser(usage='''%prog [OPTIONS]
vc3-info-client is a client for the information store for VC3

This program is licenced under the GPL, as set out in LICENSE file.

Author(s):
John Hover <jhover@bnl.gov>
''', version="%prog $Id: infocliente.py 1-31-17 23:58:06Z jhover $" )
        parser.add_option("-c", "--config", 
                            action="store", 
                            dest="configpath", 
                            default="~/vc3-services/etc/resourcetool.conf", 
                            help="configuration file path.")
        parser.add_option("-d", "--debug", 
                          dest="logLevel", 
                          default=logging.WARNING,
                          action="store_const", 
                          const=logging.DEBUG, 
                          help="Set logging level to DEBUG [default WARNING]")
        parser.add_option("-v", "--info", 
                          dest="logLevel", 
                          default=logging.WARNING,
                          action="store_const", 
                          const=logging.INFO, 
                          help="Set logging level to INFO [default WARNING]")
        parser.add_option("-s", "--infoserver", 
                          dest="infoserver", 
                          default="dev.virtualclusters.org:20333",
                          action="store", 
                          help="URL of central VC3 server")
        parser.add_option("--quiet", dest="logLevel", 
                          default=logging.WARNING,
                          action="store_const", 
                          const=logging.WARNING, 
                          help="Set logging level to WARNING [default]")
        parser.add_option("-r", "--resource", dest="resource", 
                          action="store", 
                          metavar="FILE1[,FILE2,FILE3]", 
                          help="The VC3 name of this resource.")
        parser.add_option("-u", "--user", dest="resource", 
                          action="store", 
                          metavar="", 
                          help="VC3 user name")
        parser.add_option("-p","--pin", dest="pin", 
                          metavar="PIN", 
                          action="store", 
                          help="The pairing PIN for this user+resource.")
        (self.options, self.args) = parser.parse_args()

        config = SafeConfigParser()

        if self.options.configpath:
            config.read(os.path.expanduser(self.options.configpath))

        if self.options.infoserver:
            try:
                (host, port) = self.options.infoserver.split(':')
            except ValueError:
                self.log.error("Missing port in hostname.")
                sys.exit(1)

            config.add_section('netcomm')
            config.set('netcomm', 'httpport',  '20333')
            config.set('netcomm', 'httpsport', port)
            config.set('netcomm', 'infohost',  host)

        r = ResourceTool(config, self.options)

    
if __name__ == '__main__':
    rtc = ResourceToolCLI()

       
