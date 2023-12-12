from dotenv import load_dotenv

load_dotenv()

from app import app
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
)

if __name__ == "__main__":
    app.run(debug=True)
