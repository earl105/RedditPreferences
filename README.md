# redditPreferences
A Python/Flask app that sets user preferences. It is made to be run on PythonAnywhere.
This was purely created using AI and vibe coding, I do not take credit for anything here lol.

# General steps:
1. Go to https://www.reddit.com/prefs/apps
2. Create an app, name it, and get the client ID and client ID secret.
3. Create a PythonAnywhere account
4. Create a new web app in PythonAnywhere
5. WSGI config file is located under the code section of the web app.
6. Update WSGI with the provided code, replacing your client ID, client ID secret, project home, username, and password
7. The WSGI is so that it's not just hardcoded into the file, apparently, it is more secure
8. Go to Files>mysite and add RedditApp.py (Flask) and script.py (Python logic)
9. Update RedditApp.py and create/modify the KEY section
10. Test it by opening: http://<your-username>.pythonanywhere.com/run-script?key=[YOURKEY]
11. It should say something like: "Script Ran Successfully"

# IOS Shortcuts App
1. Download the "Actions" App. The App Icon is a blue gear.
2. # Set up the first automation as follows:
3. When [APP] is closed (Set app as settings)
4. Open URL (Set URL to the Python Anywhere URL)
5. Set automation #1 to run immediately (without needing confirmation)
6. # Set up the second automation as follows:
7. When [APP] is opened (Set app as settings)
8. Set a global text variable lastOpened to the Current Date, with the Date Format set to NONE and the Time Format set to SHORT.
9. Set automation #2 to run immediately (without needing confirmation)
10. # Set up the third automation as follows:
11. When [APP] is opened (Set app as Reddit)
12. Open shortcut "Reddit Settings"
13. Set automation #3 to run immediately (without needing confirmation)
14. # Set up the shortcut as follows:
15. 
