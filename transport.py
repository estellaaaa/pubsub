# import socket

# HOST = '127.0.0.1'
# PORT = 11341

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))
#         s.sendall(json_message.encode())
#         json_response = s.recv(1024).decode()


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#     server.bind((HOST, PORT))
#     server.listen()
#     print(f"Server listening on {HOST}:{PORT}")
#     while True:
#         co, ad = server.accept()
#         with co:
#             print(f"Connected by {ad}")
#             json_request = co.recv(1024).decode()
#             if json_request == 'close':
#                 break
#             obj = rpc.unmarshall(json_request)
#             a = obj['a']
#             b = obj['b']
#             result = add(a, b)
#             co.sendall(result.encode())