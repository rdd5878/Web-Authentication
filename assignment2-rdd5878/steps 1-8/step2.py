import socket
target_host = "hw2.csec380.fun"
target_port =380
import os

CRLF = "\r\n"
def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    userAgent = "User-Agent: CSEC-380" + CRLF
    firstline = "GET /test HTTP/1.1" + CRLF
    #this is the first request to the server
    request = firstline +  userAgent + CRLF
    print(request)
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