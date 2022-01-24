import logging
from pathlib import Path

logfile = 'log_1.log'

log = logging.getLogger("my_log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)

log.info("start program")

try:    
    for x in Path('directory/').iterdir():
        p = x.parent / (x.stem.replace('-', '/') + '.txt')
        p.parent.mkdir(parents=True, exist_ok=True)
        x.rename(p)   
    log.info("finish program")
except Exception as Ex:
	log.error(Ex)