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

class Artist:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        artists = db.select('Artist', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border w-50 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>#</th>'
        result += '<th>Artist Name</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for artist in artists:
            albums = db.select('Album', where='ArtistId=$id', vars={'id': artist.ArtistId})
            result += '<tr>'
            result += '<td class="bg-dark text-white text-center">' + str(artist.ArtistId) + '</td>'
            result += '<td>' + artist.Name + '</td>'
            result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
