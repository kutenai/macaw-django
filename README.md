macaw-django
============

Utilities for working with Django and Macaw.

This module is pretty manual... so, nothing fancy here.

# Prerequisites
You need Python.. I don't know the minimum version, probably 2.6+. I write it with 2.7.8.

# Installation

You'll just have to clone the repo and run local. This isn't all nice and packaged.. someday?

First - setup virtualenvwrapper and create a virtualenv for your work here.
This is optional, but if you're not using that for your django development,
you really should be.

cd <someplace in your django project probably>
git clone git@github.com:kutenai/macaw-django.git
cd macaw-django
pip install -r requirements.txt

# Create a yaml definition file.

See the example file..


# Running the watcher

Start the tool and point it to some directories.

cd <INSTALLDIR>
python macaw_to_django.py <your_defs>.yaml ../<path to your django templates dir>  <path to your Macaw dir>

The tool will watch the MacawDir path. When files change, it will take the top level files, which
should be your *.html files..and compare them against the entries in your .yaml file. It will remove
the basepath, so you just need the filename in the .yaml file.

If it finds a match, then it will use Beautifulsoup to open the file, and search for the specified class name.
-- you did specify a class name in the .yaml file didn't you?

It will extract the code that contains this class. In practice, this is assumed to be some 'block of code'
in your your html file.. like a header, or navbar, or body code.. etc..

The code will apply some django fixups... at this point, there is one.. it tries to apply some {% static %} mappings. This is pretty basic, and obviously, converting the 'raw html' to something that works in a django template will be a huge ongoing update.. but it's a start.

# Setting up your Django project.
All of this assumes you have a few things configured in your Django project. Specifically, you have the directory that Macaw publishes to in your STATIC files path.. this is critical, otherwise the 'static' files won't be found.

I also have created some softlinks, and added the generated styles.css to my django project, by including them in my styles.less file.. this part is a work in progress, but it works.






