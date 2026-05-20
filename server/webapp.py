import os
import sqlite3

from flask import Flask


ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, "templates")
DOCUMENTS = os.path.join(ROOT, "server", "documents")

flaskapp = Flask("PageTurner", template_folder=TEMPLATES)
flaskapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
flaskapp.config["SECRET_KEY"] = "training-cookie-secret-2026"
flaskapp.config["LIBRARY_BACKUP_TOKEN"] = "ghp_trainingTokenForSecretScanning0000000000"
flaskapp.config["DOCUMENT_ROOT"] = DOCUMENTS

database_uri = os.environ.get("SQLITE_URI", os.path.join(ROOT, "pageturner.db"))

database = sqlite3.connect(database_uri, check_same_thread=False)
database.row_factory = sqlite3.Row
cursor = database.cursor()
