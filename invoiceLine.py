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
    '/invoiceLine', 'InvoiceLine'
)

class InvoiceLine:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        invc=db.select('Invoice', limit=8)
        invcline=db.select('InvoiceLine', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-striped text-center w-75 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Invoice Line</th>'
        result += '<th>Invoice</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for invoiceLine in invcline:
                result += '<td class="bg-dark text-white w-25">' + str(invoiceLine.InvoiceLineId)+'</td>' 
                break
            for invoice in invc:
                result += '<td>' +invoice.BillingAddress+'</td>' 
                break
        result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
