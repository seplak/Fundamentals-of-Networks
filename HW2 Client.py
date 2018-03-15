import socket # Import socket library

def main():

    serverName = "129.10.33.205" # Assigns server IP
    serverPort = input('Enter port number you would like to connect to: ') # User enters a valid port number


    # Create a connection to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print ("You are connected: IP " + serverName + ", Port " + str(serverPort))

    # Send initial HELLO message
    initialHello = ('ece2540 HELLO 001653770')
    clientSocket.send(initialHello.encode("utf-8")) # Send an encoded hello message

    # Set a boolean for the while loop, determines if loop continues
    continueCycle = True

    # Handle server response
    while (continueCycle):

        #Take received message, decode, and put in list so it can be easily validated
        responseMessage = clientSocket.recv(1024)
        decodedMessage = responseMessage.decode("utf-8")
        message = decodedMessage.split()
        print (message)
        properMessage = validateMessage(message)

        if (properMessage):
            # Error message received, close connection and notify user, exit loop
            if(message[1] == 'Error'):
                print('There was an error.')
                continueCycle = False
            # Status message received, evaluate expression and send back to server    
            elif(message[1] == 'STATUS'):
                mathsSolution = eval(" ".join(message[2:5]))
                clientSocket.send(str(mathsSolution).encode('utf-8'))
                print (mathsSolution)
            # Bye message received, print secret flag and exit loop   
            elif(message[1] == 'BYE'):
                secret_flag = message[2]
                print secret_flag
                continueCycle = False

    # Close the connection once loop ends            
    print('Terminating connection...')
    clientSocket.close()          

# This function validates whether or not the client received a message in the proper form
def validateMessage(message):
    #Assume message is proper until proven false
    validMessage = True

    # First component ece2540?
    if (message[0] != 'ece2540'):
        validMessage = False
    # Second component a message type? 
    if (message[1] != 'HELLO' and message[1] != 'STATUS' and message[1] != 'ERROR' and message[1] != 'BYE'):
        validMessage = False
    # If type is status, we have one of the four operators?
    if (message[1] == 'STATUS'):
        if (message[3] != '+' and message [3] != '*' and message[3] != '/' and message[3] != '-'):
            validMessage = False

    print ('Is my message valid?' + str(validMessage))
    return validMessage
         
if __name__ == '__main__':
    main()
        
		
        
