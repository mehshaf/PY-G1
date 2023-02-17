#####################################################################
### IMPORTs
#####################################################################
from config import *
import os
import time
import platform
import sys      
import zipfile     
Liste = sys.argv



# Logfile
BETRIEBSSYSTEM=platform.system()
if BETRIEBSSYSTEM.upper() == 'WINDOWS':
   logfile = 'C:\D\TOOLS\Software\PYTHON\Test-Programme\logfile.log'
elif BETRIEBSSYSTEM.upper() == 'LINUX':
   logfile = '/home/susz81/SCRIPTS/PYTHON/logfile.log'
else:
   logfile = 'UNKNOWN.log'


#####################################################################
### FKTs
#####################################################################

def flog(log_string):
   global logfile 
   if vlog == None or vlog == "" or vlog == "FALSE":
      DebugPrint = False
   else: 
      ## Log:
      logfile_obj = open(logfile, 'a')
      logfile_obj.write(log_string)
      if vstdlog == "YES":
         ## STDLOG:
         sys.stdout.write(log_string)                
      return
#####################################################################
def faktuell_zeit():
   global jahr, monat, tag, stunde, minute, sekunde, wtag, str_jahr, str_monat, str_tag, str_stunde, str_minute, str_sekunde
   # Aktuelle, lokale Zeit als Tupel
   lt = time.localtime()
   jahr, monat, tag = lt[0:3]
   # Uhrzeit
   stunde, minute, sekunde = lt[3:6]
  
   # Wochentag
   wtage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
   wtagnr = lt[6]
   wtag = wtage[wtagnr]
   
   #vsicherung_stempel = str(jahr) + str(monat) + str(tag) + '_' + str(stunde) + str(minute) + str(sekunde)
   str_jahr    = str(jahr)
   str_monat   = str(monat)
   str_tag     = str(tag)
   str_stunde  = str(stunde)
   str_minute  = str(minute)
   str_sekunde = str(sekunde)

   if len(str(str_monat)) == 1:
      str_monat = '0' +  str_monat   
   if len(str(str_tag)) == 1:
      str_tag = '0' +  str_tag
   if len(str(str_stunde)) == 1:
      str_stunde = '0' +  str_stunde
   if len(str(str_minute)) == 1:
      str_minute = '0' +  str_minute
   if len(str(str_sekunde)) == 1:
      str_sekunde = '0' +  str_sekunde 
   #zeit_stempel()
   return
#####################################################################
#####################################################################
def log_zeit():
   global jahr, monat, tag, stunde, minute, sekunde, wtag, str_jahr, str_monat, str_tag, str_stunde, str_minute, str_sekunde
   faktuell_zeit()  
   vakt_zeit = str_tag + '.' + str_monat + '.' +  str_jahr + '---' + str_stunde + ':' + str_minute + ':' + str_sekunde + '---' + wtag  
   flog  ("vakt_zeit:"+  vakt_zeit + '\n')
   return  
#####################################################################
#####################################################################
def stempel_zeit():
   global jahr, monat, tag, stunde, minute, sekunde, wtag, str_jahr, str_monat, str_tag, str_stunde, str_minute, str_sekunde, vsicherung_stempel
   faktuell_zeit()
   vsicherung_stempel = str_jahr + str_monat + str_tag + '_' + str_stunde + str_minute + str_sekunde 
   flog ("vsicherung_stempel:" + vsicherung_stempel + '\n')
   return
#####################################################################
def flogstart():
      VERSIONF = platform.python_version()
      VERSIONs=sys.version.split(" ")
      BETRIEBSSYSTEM=platform.system()
      flog ('____________________________________________\n')
      flog ('PYTHON VERSION: ' + VERSIONF + '   BETRIEBSSYSTEM: ' + BETRIEBSSYSTEM + '\n')
      log_zeit()
      stempel_zeit()    
      return 

#####################################################################

#####################################################################
def flogende():
      log_zeit() 
      flog ('##################################################\n') 
      return 

#####################################################################

#####################################################################
def zippen(zipdatei, quellpfad):
   import zipfile 
   
   #zipdatei = "C:/D/TOOLS/Software/PYTHON/Test-Programme/sample.zip"
   #quellpfad = "C:/D/TOOLS/Software/PYTHON/Test-Programme/Dir1"
   
   ZF = zipfile.ZipFile(zipdatei, "w")
   for dirname,dirs,filenames in os.walk(quellpfad):
     for filename in filenames:
       ZF.write(os.path.join(dirname,filename))
   ZF.close()  
#####################################################################

#####################################################################
def zippen2(zipdatei, quellpfad, quellunterverzeichnis):
   import zipfile 
   
   ZF = zipfile.ZipFile(zipdatei, "w")
   os.chdir(quellpfad)
   for dirname,dirs,filenames in os.walk(quellunterverzeichnis):
     for filename in filenames:
       ZF.write(os.path.join(dirname,filename))
   ZF.close()  
#####################################################################

#####################################################################
def make_tarfile(output_filename, source_dir):
    import tarfile
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
#####################################################################

#####################################################################
#Anlegen eines Verzeichnisses: falls das Verzeichnis vorhanden ist, 
#dann wird es ausgelagert und erneut angelegt.
def fverzeichniserzeugen(vhauptverz, vunterverz):
   global vsicherung_stempel
   flog("FVERZEICHNISERZEUGEN:" + "\n")
   if os.path.isdir(vhauptverz): 
      flog("Das Hauptverzeichnis ist vorhanden: " +  vhauptverz + "\n")
      os.chdir(vhauptverz)
      if os.path.isdir(vunterverz):
         vunterverz_backup = vunterverz + '___' + vsicherung_stempel 
         os.rename(vunterverz, vunterverz_backup)
         os.mkdir(vunterverz, vberechtigung)
      else:
         os.mkdir(vunterverz, vberechtigung)
   else:
      flog("!Das Hauptverzeichnis ist nicht vorhanden!: " + vhauptverz + "\n")

#####################################################################

#####################################################################
def fwhoami():
    import getpass 
    #########global vuser
    flog("FWHOAMI:" + "\n") 
    luser = getpass.getuser()
    #flog ("vuser: " + vuser + "\n")
    return  luser

#####################################################################

#####################################################################

#####################################################################


