import os
import re
import time
import logging
import yaml
from os.path import relpath
from bs4 import BeautifulSoup
import HTMLParser

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler,LoggingEventHandler


class MacawHandler(FileSystemEventHandler):

    def __init__(self,specs=None,designbase=None,templatebase=None):
        super(MacawHandler,self).__init__()

        self.design_base = designbase
        self.template_base = templatebase
        self.specs = specs

    def on_created(self, event):
        """
        When a file is created, check to see if the filename matches one
        of our target files.
        :param event:
        :return:
        """

        designpath=relpath(event.src_path,self.design_base)

        if self.specs.get(designpath):
            self.update_template(event.src_path,self.specs.get(designpath))

    def update_template(self,src,specs):
        """
        Write update the template using the source file and the specs
        :param src:
        :param spec:
        :return:
        """

        class_to_find = specs.get('class',None)
        template = specs.get('template',None)

        if not class_to_find or not template:
            raise Exception("Specification must include a class name and target template.")
        try:
            soup = BeautifulSoup(open(src))
            src_block = soup(attrs={'class':class_to_find})
            template_file = os.path.join(self.template_base,template)

            fixed_code = self.django_fixups(src_block[0].prettify())

            with open(template_file,'w') as fp:
                fp.write(specs.get('prefix',''))
                fp.write("\n\n")
                fp.write(fixed_code)
                fp.write("\n")


        except HTMLParser.HTMLParseError as e:
            print("Failed to parse the input file.")
            raise(e)

    def django_fixups(self,text):
        """
        Fix some django code sections..
        :param text:
        :return:
        """

        text = re.sub(r'(src|data-rimage|data-src)="([^"]+)"',r'''\1="{% static '\2' %}"''',text)
        return text


class TemplateUpdater(object):

    def __init__(self,yamldefs):

        with open(yamldefs,'r') as fp:
            self.specs=yaml.load(fp)

    def watch(self,designbase='.',templatebase='.'):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        event_handler = MacawHandler(specs=self.specs,
                                     designbase=designbase,
                                     templatebase=templatebase)
        observer = Observer()

        observer.schedule(event_handler,designbase,recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()




