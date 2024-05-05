
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
        )
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)

    
# Commented out for ease of demonstration purposes
# Uncomment all of the lines below and make a PR with these changes
# Code was taken from PyGoat: https://github.com/adeyosemanputra/pygoat/blob/master/introduction/views.py#L137
# Modified for it to be called once a user hits the endpoint and provides data
# @flaskapp.route('/sql-example')
def sql_lab(request):
     if request.user.is_authenticated:

         name=request.POST.get('name')

         password=request.POST.get('pass')

         if name:

             if login.objects.filter(user=name):

                 sql_query = "SELECT * FROM introduction_login WHERE user='"+name+"'AND password='"+password+"'"
                 print(sql_query)
                 try:
                     print("\nin try\n")
                     val=login.objects.raw(sql_query)
                 except:
                     print("\nin except\n")
                     return render(
                         request, 
                         'Lab/SQL/sql_lab.html',
                         {
                             "wrongpass":password,
                             "sql_error":sql_query
                         })

                 if val:
                     user=val[0].user
                     return render(request, 'Lab/SQL/sql_lab.html',{"user1":user})
                 else:
                     return render(
                         request, 
                         'Lab/SQL/sql_lab.html',
                         {
                             "wrongpass":password,
                             "sql_error":sql_query
                         })
             else:
                 return render(request, 'Lab/SQL/sql_lab.html',{"no": "User not found"})
         else:
             return render(request, 'Lab/SQL/sql_lab.html')
     else:
         return redirect('login')
