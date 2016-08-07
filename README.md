# Version Disclosure
This script is used to extract the version information of the server, technology and ssl used on a HTTP server. This script supports HTTP and HTTPS protocols.

_Usage_: version_disclosure.py -s HOST -p PORT -P PROTOCOL

Options:
  -h, --help            show this help message and exit
  -s SERVER, --server=SERVER
                        Add the remote server
  -p PORT, --port=PORT  Add the remote port to connect. Default port is 80.
  -P PROTOCOL, --protocol=PROTOCOL
                        Protocol to use for connection. Default is HTTP.
                        Protocols valid are http, https.
