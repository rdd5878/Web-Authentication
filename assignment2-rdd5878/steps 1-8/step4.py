import socket
target_host = "hw2.csec380.fun"
target_port =380
import base64

CRLF = "\r\n"
def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    #firstline = "GET /getLogin, getSecurePage HTTP/1.1" + CRLF
    url = "GET /getLogin?username=alice&password=SecretPassword123! HTTP/1.1" + CRLF
    userAgent = "User-Agent:CSEC-380" + CRLF
    contentType="Content-Type: application/x-www-form-urlencoded" + CRLF
    secure = "GET /getSecurePage" +CRLF
    accept= "Accept=*/*" + CRLF
    host = "Host:hw2.csec380.fun:380" + CRLF
    connection= "Connection=keep-alive" +CRLF
    #this is the first request to the server
    request = url +host+contentType+ userAgent + connection+ CRLF 
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    response=response + httpresponse.decode()
    print(response)
    #Gets the response 
    client.close()



    
    #generates a new socket to connect to the server
    client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client1.connect((target_host,target_port))
    response1 = response.split("\n")
    cook=response1[5].split(":")
    cookie = cook[1].split(";")
    #this parses for the cookie needed for the next request
    Cookie = str("Cookie:"+ str(cookie[0])) + CRLF
    request2= secure + host+ userAgent + Cookie+ CRLF
    client1.send(request2.encode())
    httpresponse2= client1.recv(8192)
    response2 = httpresponse2.decode()
    print(response2)
    #Gets the response 
    client.close()
    







      


def main():
    calibrate()





if __name__ == '__main__':
    main()