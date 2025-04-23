# redditPreferences
A Python/Flask app that sets user preferences. It is made to be run on PythonAnywhere.
This was purely created using AI and vibe coding, I do not take credit for anything here lol.

# General steps:
Go to https://www.reddit.com/prefs/apps
Create an app, name it, and get the client ID and client ID secret.
Create a PythonAnywhere account
Create a new web app in PythonAnywhere
WSGI config file is located under the code section of the web app.
Update WSGI with the provided code, replacing your client ID, client ID secret, project home, username, and password
The WSGI is so that it's not just hardcoded into the file, apparently, it is more secure
Go to Files>mysite and add RedditApp.py (Flask) and script.py (Python logic)
Update RedditApp.py and create/modify the KEY section
Test it by opening: http://<your-username>.pythonanywhere.com/run-script?key=[YOURKEY]
It should say something like: "Script Ran Successfully"

# IOS Shortcuts App


