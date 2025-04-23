#link will be something like http://<your-username>.pythonanywhere.com/run-script?key=[YOURKEY]

from flask import Flask, request
from script import disable_nsfw_and_blur  # <-- import function instead of running script

app = Flask(__name__)

SECRET_KEY = "[CREATE A KEY]"  # change this to something strong

@app.route('/run-script', methods=['GET'])
def run_script():
    key = request.args.get("key")
    if key != SECRET_KEY:
        return "Unauthorized", 403

    try:
        disable_nsfw_and_blur()  # <- run function directly
        return "Script ran successfully!"
    except Exception as e:
        return f"Error: {str(e)}", 500
