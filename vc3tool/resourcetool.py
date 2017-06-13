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
import logging
from ConfigParser import ConfigParser

from optparse import OptionParser

from  vc3infoservice.infoclient import InfoClient 

class ResourceTool(object):
    
    def __init__(self, config):
        self.log = logging.getLogger() 
        self.log.debug('ResourceTool starting...')
        
        
    

class ResourceToolCLI(object):
    
    def __init__(self):
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
                          action="store_true", 
                          help="URL of central VC3 server")
        parser.add_option("--quiet", dest="logLevel", 
                          default=logging.WARNING,
                          action="store_const", 
                          const=logging.WARNING, 
                          help="Set logging level to WARNING [default]")
        parser.add_option("-r", "--resource", dest="resource", 
                          default="test-resource",
                          action="store", 
                          metavar="FILE1[,FILE2,FILE3]", 
                          help="The VC3 name of this resource.")
        parser.add_option("-u", "--user", dest="resource", 
                          default="test-user",
                          action="store", 
                          metavar="", 
                          help="VC3 user name")
        parser.add_option("-p","--pin", dest="pin", 
                          default="12345", 
                          metavar="PIN", 
                          action="store", 
                          help="The pairing PIN for this user+resource.")
        (self.options, self.args) = parser.parse_args()


    
if __name__ == '__main__':
    rtc = ResourceToolCLI()
       