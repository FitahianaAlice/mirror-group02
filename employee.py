import web
from navbar import Navbar
from database import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'Artist',
    '/genre', 'Genre',
    '/employee', 'Employee',
    '/invoice', 'Invoice'
)

class Employee:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        employe=db.select('Employee', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Employee</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for employee in employe:
                result += '<td>' +employee.LastName+'</td>'
                break
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
