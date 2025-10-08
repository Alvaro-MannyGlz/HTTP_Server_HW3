### README

This repository contains the solution for CSCI 4406 - Homework 3: HTTP Server.

The assignment implements a basic web server using sockets that serves static files using the HTTP/1.0 GET method. The server is designed to compile and execute on a Linux machine.

---

### Files

* `http_server.py`: The HTTP server implementation.

---

### How to Run

The server must be run from the command line, specifying the port it should listen on.

1.  **Launch the server:**
    ```
    python3 http_server.py -p <port>
    ```
    Replace `<port>` with your chosen number (e.g., 20001).

2.  **Test with a Browser:**
    After launching, open a web browser and visit:
    ```
    http://localhost:<port>/<filename>
    ```
    (e.g., http://localhost:20001/index.html)

---

### Questions

**1. What is the difference between http_server (what you wrote) and Apache?**


**2. Some web sites allow only certain browsers (e.g., Chrome) to download content from them. How can you write http_server to support this feature? Be specific about where/what code is needed.**
