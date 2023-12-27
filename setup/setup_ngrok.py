import os
import sys
import logging
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler("app.log")

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


def setup_ngrok(app):
    ngrok_auth = os.getenv("NGROK_AUTH_TOKEN")
    if ngrok_auth is not None:
        ngrok.set_auth_token(ngrok_auth)
    port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000

    try:
        # Open an ngrok tunnel to the dev server
        tunnel = ngrok.connect(port)
        BASE_URL = tunnel.public_url
        logger.info('ngrok tunnel "{}" -> "http://127.0.0.1:{}"'.format(BASE_URL, port))
    except Exception as e:
        logger.error(f"Failed to create ngrok tunnel: {str(e)}")

    # Set the base URL in the FastAPI app
    print(BASE_URL)
    app.base_url = BASE_URL

    return BASE_URL
