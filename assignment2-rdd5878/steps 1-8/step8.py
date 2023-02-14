import socket
target_host = "hw2.csec380.fun"
target_port =380
import base64
import json
import time

CRLF = "\r\n"



def contentLength(string):
        num=len(string)
        return num

def calibrate():
    #generates a new socket to connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target_host,target_port))
    #firstline = "GET /getLogin, getSecurePage HTTP/1.1" + CRLF
    url = "POST /captchaLogin HTTP/1.1" + CRLF
    userAgent = "User-Agent:CSEC-380" + CRLF
    contentType="Content-Type: application/x-www-form-urlencoded" + CRLF
    contentlength="Content-Length:42" + CRLF
    body =  "username=alice&password=SecretPassword123!" +CRLF
    validate = "POST /captchaValidate HTTP/1.1" +CRLF
    secure= "POST /captchaSecurePage HTTP/1.1" +CRLF
    host = "Host:hw2.csec380.fun" + CRLF
    accept="Accept: application/json" +CRLF
    connection= "Connection:keep-alive" +CRLF
    #this is the first request to the server 
    request = url +host+userAgent+contentType+contentlength+CRLF+body+CRLF#+host+userAgent+accept+acceptLang+acceptEncoding+userAgent+contentType+contentlength+ CRLF
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    httpresponse = client.recv(8192)
    response = response +httpresponse.decode()
    print(response)
    #this checks to see which values are integers or operation for math
    string =" "
    for i in httpresponse.decode():
        if i.isdigit() or i=="+" or i=="-" or i=="*" or i=="/":
            string= string+i
    #gets the value of the operation for the next request
    value = eval(string)
    client.close()




    #generates a new socket to connect to the server
    client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client1.connect((target_host,target_port))
    #this is to evaluate the content-length header
    value= "solution="+str(value) +CRLF
    length=len(value)-2
    contentlength="Content-Length: "+str(length) +CRLF
    #this parses for the cookie needed for the next request
    response1 = response.split("\n")
    cook=response1[5].split(":")
    cookie = cook[1].split(";")
    Cookie = str("Cookie:"+ str(cookie[0])) + CRLF
    #this is the second request to the server to validate the math done
    request2= validate+host+userAgent+contentType+contentlength+Cookie+CRLF+str(value)+CRLF
    client1.send(request2.encode())
    httpresponse2 = client1.recv(8192)
    response2 = httpresponse2.decode()
    httpresponse2 = client1.recv(8192)
    response2 = response2 + httpresponse2.decode()
    print(response2)
    client.close()

    #generates a new socket to connect to the server
    client2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client2.connect((target_host,target_port))
    #there is no body being sent we just need the cookie from the previous response
    contentlength="Content-Length: 0" +CRLF
    #this parses the cookie that is needed
    response2 = response.split("\n")
    cook=response2[5].split(":")
    cookie = cook[1].split(";")
    Cookie = str("Cookie:"+ str(cookie[0])) + CRLF
    #this is the third request to teh server to login to the secure endpoint
    request3= secure+host+userAgent+contentType+contentlength+Cookie+CRLF
    client2.send(request3.encode())
    httpresponse3 = client2.recv(8192)
    response3 = httpresponse3.decode()
    httpresponse3 = client2.recv(8192)
    response3 = response3 + httpresponse3.decode()
    #this is the response back welcoming alice
    print(response3)
    client.close()


def main():
    calibrate()





if __name__ == '__main__':
    main()