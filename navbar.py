import web

class Navbar:
    def get_navbar(self):
        result = '<html><head><title>Test Groupe 02</title>'
        result += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
        result += '</head>'
        result += '<nav class="navbar navbar-expand navbar-light bg-info w-75 mt-4 mb-4 ml-auto mr-auto rounded" >'
        result += '<div class="container justify-content-md-center">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item"><a class="nav-link text-light" aria-current="page" href="/">Home</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" aria-current="page" href="/album">Album</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/artist">Artist</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/genre">Liste de genre</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/employee">Employee</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/invoice">Invoice</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="#">InvoiceLine</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="#">MediaType</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="#">Playlist</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="#">Playlist Track</a></li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        return result
