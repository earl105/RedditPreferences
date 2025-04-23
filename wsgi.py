# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import os
os.environ["REDDIT_CLIENT_ID"] = "[INSERT HERE]"
os.environ["REDDIT_CLIENT_SECRET"] = "[INSERT HERE]"
os.environ["REDDIT_USERNAME"] = "[INSERT HERE]"
os.environ["REDDIT_PASSWORD"] = "[INSERT HERE]"
os.environ["REDDIT_USER_AGENT"] = "linux:nsfw_toggle_script:v1.1 (by /u/_de414))"

# add your project directory to the sys.path
project_home = '[INSERT HERE]' #/home/your-username/mysite
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from RedditApp import app as application  # noqa



