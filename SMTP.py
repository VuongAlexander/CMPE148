from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#mailport = 7890
#mailserver = 'localhost'

mailserver = ("mail.smtp2go.com", 2525)

# Create socket called clientSocket and establish a TCP connection with mailserver
SMTPClientSocket = socket(AF_INET, SOCK_STREAM)
SMTPClientSocket.connect(mailserver)

recv = SMTPClientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alex\r\n'
SMTPClientSocket.send(heloCommand.encode())
recv1 = SMTPClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Info for username and password
username =  "username" #the username for your server
password = "password" #the password for your server, changed here
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
SMTPClientSocket.send(authMsg)
recv_auth = SMTPClientSocket.recv(1024)
print(recv_auth.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'Mail From:<Alexander.Vuong@sjsu.edu>\r\n' #Change Mail
SMTPClientSocket.send(mailFromCommand.encode())
recv2 = SMTPClientSocket.recv(1024)
print(recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "Mail To: <Alexander.Vuong@sjsu.edu> \r\n" #Change Mail
SMTPClientSocket.send(rcptTo.encode())
recv3 = SMTPClientSocket.recv(1024)
print(recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
print(dataCommand)
SMTPClientSocket.send(dataCommand.encode())
recv4 = SMTPClientSocket.recv(1024)
print(recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
subject = "Subject: SMTP Testing \r\n\r\n"
SMTPClientSocket.send(subject.encode())

message = input("Enter your message:\r\n")

# Message ends with a single period.
SMTPClientSocket.send(message.encode())
SMTPClientSocket.send(endmsg.encode())
recv_msg = SMTPClientSocket.recv(1024)

print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print(quitCommand)
SMTPClientSocket.send(quitCommand.encode())
message = SMTPClientSocket.recv(1024)
print(message)
SMTPClientSocket.close()
