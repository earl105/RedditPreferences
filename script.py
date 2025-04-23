import praw
import os
import logging

# --- Configuration ---
# Load from Environment Variables (Recommended for Security)
# Set these variables in your PC/Pi's environment before running the script
# Example: export REDDIT_CLIENT_ID='your_client_id'
REDDIT_CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.environ.get("REDDIT_USERNAME")
REDDIT_PASSWORD = os.environ.get("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.environ.get("REDDIT_USER_AGENT", "linux:nsfw_toggle_script:v1.1 (by /u/_de414)") # Updated user agent

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("nsfw_toggle.log"), # Log to a file
                        logging.StreamHandler()                 # Also print to console
                    ])

# --- Input Validation ---
if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD]):
    logging.error("Missing Reddit API credentials. Set environment variables or hardcode in script.")
    exit(1) # Exit if credentials are missing

# --- Reddit API Function ---
def disable_nsfw_and_blur():
    """Logs into Reddit and disables the NSFW viewing preference and blurs NSFW content."""
    try:
        logging.info("Attempting to disable NSFW setting and enable blur...")
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD,
            user_agent=REDDIT_USER_AGENT,
        )

        # Verify authentication (optional but good practice)
        if reddit.user.me() and reddit.user.me().name == REDDIT_USERNAME:
            logging.info(f"Successfully authenticated as u/{REDDIT_USERNAME}.")
        else:
            logging.warning("Authentication check failed or username mismatch.")
            # Decide if you want to proceed anyway or raise an error

        # The core action: Update preferences
        reddit.user.preferences.update(over_18=False, label_nsfw=True)
        logging.info("Successfully updated preferences: NSFW (over_18) set to False, Blur NSFW (label_nsfw) set to True.")

    except praw.exceptions.PRAWException as e:
        logging.error(f"PRAW Error during NSFW/Blur toggle: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True) # Log full traceback for unexpected errors

# --- Main Execution --- For testing ---
#logging.info("Script started. Running NSFW and Blur toggle.")
#disable_nsfw_and_blur()
#logging.info("Script completed.")
#print("Reddit script executed successfully!")