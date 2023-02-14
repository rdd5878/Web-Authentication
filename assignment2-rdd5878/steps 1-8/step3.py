import socket
target_host = "hw2.csec380.fun"
target_port =380
import base64

CRLF = "\r\n"
def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    username= "alice"
    password= "SecretPassword123!"
    pair = username + ":" + password
    #this was just harded coded but thius would be the way I would have done it.
    bytes =  pair.encode("ascii")
    base = base64.b64encode(bytes)
    string64 = base.decode("ascii")
    userAgent = "User-Agent: CSEC-380" + CRLF
    firstline = "GET /basic HTTP/1.1" + CRLF
    authorization = "Authorization: Basic YWxpY2U6U2VjcmV0UGFzc3dvcmQxMjMh"+CRLF
    #this is the first request
    request = firstline + userAgent + authorization + CRLF
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