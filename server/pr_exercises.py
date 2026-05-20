"""
Participant PR exercises

Uncomment one exercise at a time in a feature branch, open a pull request, and let
CodeQL and Code Quality report the new findings. The snippets are intentionally
unsafe training examples.
"""

# import logging
# import subprocess
# from flask import jsonify, render_template_string, request
# from server.webapp import cursor, flaskapp


# @flaskapp.route("/exercise/member-search")
# def exercise_member_search():
#     username = request.args.get("username", "")
#     cursor.execute("SELECT email FROM users WHERE username = '" + username + "'")
#     return jsonify([dict(row) for row in cursor.fetchall()])


# @flaskapp.route("/exercise/lookup-host")
# def exercise_lookup_host():
#     host = request.args.get("host", "localhost")
#     return subprocess.check_output("nslookup " + host, shell=True)


# @flaskapp.route("/exercise/read-file")
# def exercise_read_file():
#     filename = request.args.get("file", "welcome.txt")
#     return open(filename, "r").read()


# @flaskapp.route("/exercise/hello")
# def exercise_hello():
#     name = request.args.get("name", "reader")
#     return render_template_string("<h1>Hello " + name + "</h1>")


# @flaskapp.route("/exercise/log")
# def exercise_log():
#     message = request.args.get("message", "")
#     logging.warning(message)
#     return jsonify(status="logged")


# def exercise_quality_findings(items=[]):
#     unused_total = 0
#     status = {"mode": "draft", "mode": "published"}
#     if len(items) == len(items):
#         pass
#     return status
#     print("unreachable")