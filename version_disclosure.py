#!/usr/bin/python

import re, httplib, optparse

__author__ = "invad3rsam"
__version__ = "v1.0.0"

###
#   Description:
#     This script is used to extract the version information of the server, 
#     technology and ssl used on a HTTP server. This script supports HTTP and
#     HTTPS protocols.
###


def http_version(host, port):
    try:
        conn = httplib.HTTPConnection(host, port)
        conn.request("GET", "/")
        response = conn.getresponse()
        server_string = response.getheader("Server")
        extract_version(server_string)
    except:
        print "[-] Unable to connect %s on %s"%(host, port)


def https_version(host, port):
    try:
        conn = httplib.HTTPSConnection(host, port)
        conn.request("GET", "/")
        response = conn.getresponse()
        server_string = response.getheader("Server")
        extract_version(server_string)
    except:
        print "[-] Unable to connect %s on %s"%(host, port)


def extract_version(server_string):
    apache_re = re.compile(r"Apache")
    iis_re = re.compile(r"IIS")
    php_re = re.compile(r"PHP")
    asp_re = re.compile(r"ASP")
    openssl_re = re.compile(r"OpenSSL")

    finding_string = ""

    split_data = server_string.split(" ")
    for data in split_data:
        if apache_re.match(data):
            version = data.split("/")[1].strip()
            finding_string += "[+] Apache Server Version Disclosure\n\r\tVersion:" + version + "\n\r"
        if iis_re.match(data):
            version = data.split("/")[1].strip()
            finding_string += "[+] IIS Server Version Disclosure\n\r\tVersion:" + version + "\n\r"
        if php_re.match(data):
            version = data.split("/")[1].strip()
            finding_string += "[+] PHP Version Disclosure\n\r\tVersion:" + version + "\n\r"
        if asp_re.match(data):
            version = data.split("/")[1].strip()
            finding_string += "[+] ASP.NET Version Disclosure\n\r\tVersion:" + version + "\n\r"
        if openssl_re.match(data):
            version = data.split("/")[1].strip()
            finding_string += "[+] OpenSSL Version Disclosure\n\r\tVersion:" + version + "\n\r"
    print finding_string


def main():
    parser = optparse.OptionParser(usage="version_disclosure.py -s HOST -p PORT -P PROTOCOL")
    parser.add_option("-s", "--server", dest="server", help="Add the remote server")
    parser.add_option("-p", "--port", dest="port", default=80, help="Add the remote port to connect. Default port is 80.")
    parser.add_option("-P", "--protocol", dest="protocol", default="http", help="Protocol to use for connection. Default is HTTP. Protocols valid are http, https.")
    #parser.add_option("-h", "--help", help="Show this help box")
    options, args = parser.parse_args()

    if (options.server):
        server, port, protocol = options.server, options.port, options.protocol
        if protocol == "http":
            http_version(server, port)
        elif protocol == "https":
            https_version(server, port)
        else:
            print "[-] Invalid Protocol - ", protocol
            parser.print_help()
            SystemExit(1)
    else:
        print "[-] Server IP address required."
        parser.print_help()
        SystemExit(1)


if __name__ == "__main__":
    main()