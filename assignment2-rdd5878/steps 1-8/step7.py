import socket
target_host = "hw2.csec380.fun"
target_port =380

CRLF = "\r\n"
def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    #firstline = "GET /getLogin, getSecurePage HTTP/1.1" + CRLF
    url = "POST /jsonLogin HTTP/1.1" + CRLF
    userAgent = "User-Agent:CSEC-380" + CRLF
    contentType="Content-Type: application/x-www-form-urlencoded" + CRLF
    contentlength="Content-Length:42" + CRLF
    body =  "username=alice&password=SecretPassword123!" +CRLF
    secure = "POST /jsonSecurePage HTTP/1.1" +CRLF
    host = "Host:hw2.csec380.fun" + CRLF
    accept="Accept: application/json" +CRLF
    #this is request #1
    request = url +host+userAgent+contentType+contentlength+accept+CRLF+body+CRLF#+host+userAgent+accept+acceptLang+acceptEncoding+userAgent+contentType+contentlength+ CRLF
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    httpresponse = client.recv(8192)
    response = response +httpresponse.decode()
    token=(httpresponse.decode())
    print(response)
    #Gets the response
    #this grabs the token that is needed for authentication
    print(token[33:65])
    client.close()



    
    #generates a new socket to connect to the server
    client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client1.connect((target_host,target_port))
    #This calculates the Content length needed for the request
    user="apikey=" +str(token[33:65])+CRLF
    length = len(user)-2
    contentlength="Content-Length: "+ str(length) + CRLF
    #this parses for the cookie needed for the next request
    response1 = response.split("\n")
    cook=response1[5].split(":")
    cookie = cook[1].split(";")
    Cookie = str("Cookie:"+ str(cookie[0])) + CRLF
    #this is the request2
    request2= secure+host+userAgent+contentType+contentlength+Cookie+CRLF+user+CRLF
    client1.send(request2.encode())
    httpresponse2 = client1.recv(8192)
    response2 = httpresponse2.decode()
    httpresponse2 = client1.recv(8192)
    response2 = response2 + httpresponse2.decode()
    print(response2)
    #Gets the response 
    client.close()


def main():
    calibrate()





if __name__ == '__main__':
    main()