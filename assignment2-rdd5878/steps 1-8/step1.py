import socket
target_host = "hw2.csec380.fun"
target_port =380

CRLF = "\r\n"
def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    #this is the request to the server 
    firstline = "GET /hello HTTP/1.1" + CRLF
    request = firstline + CRLF
    #sends the 
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    httpresponse = client.recv(8192)
    response=response + httpresponse.decode()
    client.close()
    #Gets the response 
    print(response)

def main():
    calibrate()





if __name__ == '__main__':
    main()