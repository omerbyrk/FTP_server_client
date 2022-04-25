from pyftpdlib import authorizers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pathlib import Path

_authorizer = authorizers.DummyAuthorizer()
_currentpath = Path(__file__).parent.absolute().__str__()


_authorizer.add_user("omer", "123456", _currentpath+"\\home".__str__(), "elradfmw", "Giriş Başarılı", "Çıkış Yapıldı")

_handler = FTPHandler
_handler.timeout = 0
_handler.banner = "FTP Server'a hoş geldiniz"
_handler.authorizer = _authorizer


_server = FTPServer(("localhost", 2121), _handler)
_server.serve_forever()