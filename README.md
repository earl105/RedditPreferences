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
12. Every 3 months, you have to renew your PythonAnywhere site unless you pay, but it only takes two seconds.

# IOS Shortcuts App
1. Download the "Actions" App. The App Icon is a blue gear.
 # Set up the first automation as follows:
2. When [APP] is closed (Set app as settings)
3. Open URL (Set URL to the Python Anywhere URL, http://<your-username>.pythonanywhere.com/run-script?key=[YOURKEY])
4. Set automation #1 to run immediately (without needing confirmation)
 # Set up the second automation as follows:
5. When [APP] is opened (Set app as settings)
6. Set a global text variable lastOpened to the Current Date, with the Date Format set to NONE and the Time Format set to SHORT.
7. Set automation #2 to run immediately (without needing confirmation)
 # Set up the "Reddit Settings" shortcut as follows:
8. Get global text variable lastOpened
9. Get Minutes between Current Date and Global Variable - Text
10. Set the Current Date format to match (the Date Format set to NONE and the Time Format set to SHORT)
11. Calculate the absolute value (abs(x)) of Time Between Dates
12. If the Calculation Result is less than or equal to 3 (3-minute cooldown)
13. (OPTIONAL) Show Notification: Last Time Settings was opened: [Global Variable - Text] (\n) Minutes since: [Calculation Result]
14. Open URL (set to Python Anywhere URL, http://<your-username>.pythonanywhere.com/run-script?key=[YOURKEY])
15. Otherwise
16. Open [APP] (set app to Reddit)
17. End IF 
 # Set up the third automation as follows:
18. When [APP] is opened (Set app as Reddit)
19. Open shortcut "Reddit Settings"
20. Set automation #3 to run immediately (without needing confirmation)

**(Automation 2)** When you open the settings app, it logs the time you last opened the settings app, allowing for this step:  


Now, when you open Reddit **(Automation 3)**, it checks **(using the "Reddit Settings" shortcut)** if the settings app has been opened within the past 3 minutes (or however long you set it to).  

If the settings app has been opened recently, it will incessantly redirect you to the website that changes your Reddit Preferences.  

This essentially puts the app on a time-out for those 3 minutes after settings have been opened.  

This is helpful as there is a short delay between running the site and the phone app recognizing that the preferences have changed.  

Otherwise, it proceeds to Reddit like normal.  

**(Automation 1)** When you close settings, it resets your user preferences, making it so that any time it is changed, it gets changed back immediately.





