import web

class Navbar:
    def get_navbar(self):
        result = '<html><head><title>Test Groupe 02</title>'
        result += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
        result += '</head>'
        result += '<nav class="navbar navbar-expand-lg navbar-light bg-light rounded " >'
        result += '<div class="container-fluid justify-content-md-center">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item"><a class="nav-link" aria-current="page" href="/">Home</a></li>'
        result += '<li class="nav-item"><a class="nav-link" aria-current="page" href="#">Album</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/artist">Artist</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/genre">Liste de genre</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/employee">Employee</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/invoice">Invoice</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">InvoiceLine</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">MediaType</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Playlist</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="#">Playlist Track</a></li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        return result
