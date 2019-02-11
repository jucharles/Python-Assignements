(i) Create a connection socket when contacted by a client (browser)
(ii) Receive the HTTP request from this connection
(iii) Parse the request to determine the specific file being requested
(iv) Get the requested file from the server’s file system
(v) Create an HTTP response message consisting of the requested file
preceded by header lines
(vi) Send the response over the TCP connection to the requesting browser.

Build Instructions:
In terminal type 'cd 379-charles'
then type 'python 379charles.py

Go to any browser and type 'localhost:6969/379charles.html' or '127.0.0.1:/379charles.html'