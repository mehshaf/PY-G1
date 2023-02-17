#from __future__ import print_function
#####################################################################
### IMPORTs
#####################################################################
import bib
import os
import time
import platform
import sys      
import zipfile     
Liste = sys.argv



#####################################################################
### FKTs
#####################################################################

def fdirtest():
    vakt_pfad = os.getcwd()
    bib.flog ("vakt_pfad: " + vakt_pfad + "\n")
    vverzeichnis = "VERZEICHNIS"
    bib.fverzeichniserzeugen(vakt_pfad, vverzeichnis)
    vuser =  bib.fwhoami()
    bib.flog ("vuser: " + vuser + "\n")
   
    vdateien = os.listdir(vakt_pfad)
    for vdatei in vdateien:        
       bib.flog(vdatei + "\n")    
    return 







####################################################################
### MAIN
#####################################################################
bib.flogstart()

#bib.zippen()
#-#l_zipdatei = "C:/D/TOOLS/Software/PYTHON/Test-Programme/test123.zip"
#-#l_quellpfad = "C:/D/TOOLS/Software/PYTHON/Test-Programme/Dir1"
#-#bib.zippen(l_zipdatei, l_quellpfad)
#-#bib.make_tarfile(l_zipdatei, l_quellpfad)

# bib.zippen2
#-#l_zipdatei = "C:/D/TOOLS/Software/PYTHON/Test-Programme/test2.zip"
#-#l_quellpfad = "C:/D/TOOLS/Software/PYTHON/Test-Programme"
#-#l_quellunterverzeichnis = "Dir1"
#-#bib.zippen2(l_zipdatei, l_quellpfad, l_quellunterverzeichnis)


#bib.make_tarfile()
#-#l_output_filename = "C:/D/TOOLS/Software/PYTHON/Test-Programme/test123.tar.gz"
#-#l_source_dir = "C:/D/TOOLS/Software/PYTHON/Test-Programme/Dir1"
#-#bib.make_tarfile(l_output_filename, l_source_dir)

#bib.fdirtest()
fdirtest()





bib.flogende()
