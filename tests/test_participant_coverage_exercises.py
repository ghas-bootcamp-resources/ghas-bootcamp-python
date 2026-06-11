"""
Coverage exercise tests for participants.

Uncomment one or more tests in a branch, open a pull request, and compare the
coverage comment before and after the change. These tests intentionally cover
routes that the baseline suite leaves untouched.
"""

# from server.database import initialize_database
# from server.webapp import flaskapp
# import server.routes


# def test_login_records_activity():
#     initialize_database()
#     flaskapp.config["TESTING"] = True
#     client = flaskapp.test_client()
#
#     response = client.post(
#         "/login",
#         data={"username": "morgan", "password": "books2026"},
#         follow_redirects=True,
#     )
#
#     assert response.status_code == 200
#     assert b"Signed in as morgan" in response.data


# def test_profile_page_renders_seed_user():
#     initialize_database()
#     flaskapp.config["TESTING"] = True
#     client = flaskapp.test_client()
#
#     response = client.get("/profile/riley")
#
#     assert response.status_code == 200
#     assert b"riley" in response.data


# def test_review_creation_adds_discussion_note():
#     initialize_database()
#     flaskapp.config["TESTING"] = True
#     client = flaskapp.test_client()
#
#     response = client.post(
#         "/reviews",
#         data={"book_id": "1", "username": "jamie", "body": "Great discussion pick"},
#         follow_redirects=True,
#     )
#
#     assert response.status_code == 200
#     assert b"Great discussion pick" in response.data