import web
from navbar import Navbar
from database import Db

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'Artist',
    '/genre', 'Genre',
    '/employee', 'Employee',
    '/invoice', 'Invoice',
    '/mediaType', 'MediaType',
    '/invoiceLine', 'InvoiceLine'
)

class MediaType:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        mdtype=db.select('MediaType', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-striped table-hover text-center w-75 m-auto rounded">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Mediatype</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for MediaType in mdtype:
                result += '<td class="p-4">' +MediaType.Name+'</td>' 
                break
            result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
