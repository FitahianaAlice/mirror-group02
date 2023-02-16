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

class Album:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        albums = db.select('Album', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border w-75 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th class="text-center">#</th>'
        result += '<th class="text-center">Album List</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for album in albums:
            albums = db.select('Album', where='AlbumId=$id', vars={'id': album.AlbumId})
            result += '<tr>'
            result += '<td class="bg-dark text-white text-center">' + str(album.AlbumId) + '</td>'
            result += '<td class="text-center">' + album.Title + '</td>'
            result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
