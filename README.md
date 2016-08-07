# Version Disclosure
This script is used to extract the version information of the server, technology and ssl used on a HTTP server. This script supports HTTP and HTTPS protocols.

_Usage_: version_disclosure.py -s HOST -p PORT -P PROTOCOL

Options:<br>
  -h, --help                        show this help message and exit<br>
  -s SERVER, --server=SERVER        Add the remote server<br>
  -p PORT, --port=PORT              Add the remote port to connect. Default port is 80.<br>
  -P PROTOCOL, --protocol=PROTOCOL  Protocol to use for connection. Default is HTTP. Protocols valid are http, https.<br>
