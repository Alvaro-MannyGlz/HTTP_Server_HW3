# --- 1. Import Necessary Modules ---                                                                       <- Section 1
# import sys
# import socket
# import os

# --- 2. Define Helper Functions ---                                                                        <- Section 2


# -- function --
# Take raw request data and extracts the essential parts, specifically:
#          1) The requested file path
#          2) The HTTP method
#          3) The 'User-Agent' header

# -- function --
# Based on the file extension (e.g., .html, .png, .pdf), determine the correct
#          Content-Type string for the HTTP response header. <- (Knowing this will help answer Q2 in the README)

# -- function --
# Construct the complete HTTP response message, including headers and the body.
#          It handles two main cases:
#          1) Success
#          2) Failure


# --- 3. Client Connection Handler ---                                                                      <- Section 3


# --- code ---

# 1. Read Request: Read all incoming data from the 'client_socket'.

# 2. Print Debug Info: Print the inbound request message.

# 3. Parse Request: Call 'parse_request' to get the requested file path and User-Agent.

# 4. Security Check: If the browser is not allowed, send a 403 response

# 5. File Handling:
#    a. Check if the file exists on the server's file system
#    b. If the file doesn't exist, build and send a 404 Not Found response.
#    c. If the file exist, read its binary content.

# 6. Build and Send Response:


# 7. Close Connection


# --- 4. Main Server Loop ---                                                                               <- Section 4
# Initialize the server and keeps it running indefinitely.

# 1. Argument Check: Verify the command was run correctly (e.g., `./http_server -p 20001`).

# 2. Socket Creation: Create a TCP socket (`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`).

# 3. Bind and Listen: Bind the socket to the specified port and start listening for incoming connections.

# 4. Infinite Loop: Start a `while True:` loop to handle connections sequentially (per **Requirement 132**).
#    a. Accept: Wait for a new connection (`server_socket.accept()`). This will block until a client connects.
#    b. Handle: Pass the new client socket to the `handle_client` function.

# --- 5. Execution Block ---                                                                                <- Section 5

# if __name__ == "__main__":
#     main()