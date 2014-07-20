import os
import time
import logging
import yaml

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

class TemplateUpdater(object):

    def __init__(self,yamldefs,paths):
        pass

        with open(yamldefs,'r') as fp:
            self.tables=yaml.load(fp)

    def watch(self,path):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        event_handler = LoggingEventHandler()
        observer = Observer()

        #path=os.path.join(os.getcwd(),'../design/DitchApp')
        observer.schedule(event_handler,path,recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()




