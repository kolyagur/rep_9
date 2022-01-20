import glob, os
import logging

logfile = 'log_1.log'

log = logging.getLogger("my_log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)

log.info("start program")

try:
    os.chdir("directory")
    for file in glob.glob("*.txt"):
        os.rename(file,file.replace('-','/'))
    log.info("finish program")
except Exception as Ex:
	log.error(Ex)        