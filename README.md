### Responsibilities

1. Creating the socket
   We can split the work out evenly, or such, but everyone must know what is going on
2. Testing the code

3. Updating the README accordingly for everyone to understand

4. Answering the questions in the README section

### README

This repository contains the solution for CSCI 4406 - Homework 3: HTTP Server.

The assignment implements a basic web server using sockets that serves static files using the HTTP/1.0 GET method. The server is designed to compile and execute on a Linux machine.

---

### Files

- `http_server.py`: The HTTP server implementation.

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

Our HTTP server is far less customizable and complex than the Apache HTTP Web Server. For example, Apache supports server-side programming languages, such as PHP, whereas our server is limited to serving pre-determined files (such as static HTML). Apache also features dozens of other practical capabilities, including user and session tracking, rate limiting, load balancing, and more.

**2. Some websites allow only certain browsers (e.g., Chrome) to download content from them. How can you write http_server to support this feature? Be specific about where/what code is needed.**

This feature is achieved by parsing each incoming request’s User Agent header. This header includes the browser name, its version number, and system details to the server.

To serve content only to certain browsers, we can check the request’s User Agent on our server and conditionally serve content. In our program, we check the user agent and don’t serve to users using `curl`:

```python
# def handle_client(client_socket):
...
# 1. Get the requested file path and User-Agent (ex. Mozilla/5.0 (Windows NT 10.0; Win64; x64)).
method, path, user_agent = parse_request(request_data)
if not method or not path:
    return

# 2. If the browser is not allowed, send a 403 Forbidden response
if user_agent and "curl" in user_agent.lower():
    body = "<html><body><h1>403 Forbidden</h1></body></html>"
    response = build_response(403, "text/html", body)
    client_socket.sendall(response)
    return
```
