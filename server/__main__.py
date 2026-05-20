import os
import sys

sys.path.append(".")

from server.database import initialize_database
from server.webapp import database, cursor, flaskapp
import server.routes


if __name__ == "__main__":
    initialize_database()
    flaskapp.run(
        "0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=bool(os.environ.get("DEBUG", False)),
    )

    cursor.close()
    database.close()
