from pathlib import Path

from server.webapp import database, cursor, flaskapp


BOOKS = [
    ("The Hobbit", "JRR Tolkien", "fantasy", "true"),
    ("Kindred", "Octavia Butler", "science fiction", "true"),
    ("The Left Hand of Darkness", "Ursula K. Le Guin", "science fiction", "false"),
    ("The Fifth Season", "N. K. Jemisin", "fantasy", "false"),
    ("A Psalm for the Wild-Built", "Becky Chambers", "cozy science fiction", "true"),
]

USERS = [
    ("admin", "admin@example.com", "admin123", "true", "Library administrator"),
    ("morgan", "morgan@example.com", "books2026", "false", "Runs the Wednesday book club"),
    ("riley", "riley@example.com", "reader", "false", "<script>console.log('club notes')</script>"),
]

REVIEWS = [
    (1, "morgan", "A comfort read for rainy afternoons."),
    (2, "riley", "Still the best pick for a lively discussion."),
]


def initialize_database():
    cursor.executescript(
        """
        DROP TABLE IF EXISTS reviews;
        DROP TABLE IF EXISTS books;
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS audit_log;

        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            read TEXT NOT NULL
        );

        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            is_admin TEXT NOT NULL,
            bio TEXT NOT NULL
        );

        CREATE TABLE reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            body TEXT NOT NULL
        );

        CREATE TABLE audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            action TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    cursor.executemany(
        "INSERT INTO books (name, author, genre, read) values (?, ?, ?, ?)", BOOKS
    )
    cursor.executemany(
        "INSERT INTO users (username, email, password, is_admin, bio) values (?, ?, ?, ?, ?)",
        USERS,
    )
    cursor.executemany(
        "INSERT INTO reviews (book_id, username, body) values (?, ?, ?)", REVIEWS
    )
    database.commit()
    seed_documents()


def seed_documents():
    document_root = Path(flaskapp.config["DOCUMENT_ROOT"])
    document_root.mkdir(parents=True, exist_ok=True)
    (document_root / "spring-reading-list.txt").write_text(
        "Kindred\nThe Fifth Season\nA Psalm for the Wild-Built\n", encoding="utf-8"
    )
    (document_root / "welcome.txt").write_text(
        "Welcome to PageTurner Library Admin.\n", encoding="utf-8"
    )