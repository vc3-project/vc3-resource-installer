#!/bin/env python

__author__ = "John Hover, Jose Caballero"
__copyright__ = "2017 John Hover"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9.1"
__maintainer__ = "John Hover"
__email__ = "jhover@bnl.gov"
__status__ = "Production"

#
#  https://github.com/PanDAWMS/autopyfactory/archive/master.zip

# Factory tarball
# http://dev.racf.bnl.gov/dist/src/tgz/autopyfactory-2.4.10.tar.gz
import logging

class ResourceTool(object):
    
    def __init__(self):
        self.log = logging.getLogger() 
        self.log.debug('ResourceTool starting...')


class ResourceToolCLI(object):
    
    def __init__(self):
        self.log = logging.getLogger()
        self.log.debug('ResourceToolCLI starting...')

   
    
if __name__ == '__main__':
    rtc = ResourceToolCLI()
       