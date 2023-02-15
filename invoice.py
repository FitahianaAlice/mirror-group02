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

class Invoice:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        invc=db.select('Invoice', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Invoice</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for invoice in invc:
                result += '<td>' +invoice.BillingCity+'</td>' 
                break
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
