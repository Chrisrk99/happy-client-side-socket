import argparse
from socket import *
import logging

debug = False

def main():
    ## ================= parse user arguments ========================= ## 
    argument_parser = argparse.ArgumentParser(usage='This script is a client-side socket'+
    " which connects to a host, receives a packet, and stops.\n")

    argument_parser.add_argument('--server', '-s', 
                                type=str,
                                metavar='<server_ip>', 
                                nargs=1, 
                                required=True,
                                action='append',
                                help="The IP address of the the server")

    argument_parser.add_argument('--port', '-p', 
                                metavar='<port_#>',
                                type=int,
                                nargs=1, 
                                required=True,
                                action='append',
                                help="The port the server listens on")

    argument_parser.add_argument('--logfile', '-l', 
                                metavar='<log_file_location>', 
                                type=str,
                                nargs=1, 
                                required=True,
                                action='append',
                                help="The location to keep the record of packets received.")

    arguments = argument_parser.parse_args()

    # Sanity check inputs 
    server_port = 0
    server_ip, logfile_loc = '' , ''

    if arguments.logfile:
        logfile_loc = arguments.logfile[0][0]
    else:
        print("Bad Logfile arg")
        exit()
    
    logging.basicConfig( # create automatic logging and printing
        level=logging.INFO,
        format="%(asctime)s[%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler(logfile_loc+'.log'),
            logging.StreamHandler()
        ]
    )  
    
    if arguments.server and len(arguments.server[0]) <= 15:
        server_ip = arguments.server[0][0]
    else:
        logging.error('bad server')
        exit()

    if arguments.port:
        server_port = arguments.port[0][0]
    else:
        logging.error('bad port')
        exit()

    ##========================== Connect to Server ===============================
    logging.info('Command Line Args - IP: {0} Port: {1} Logfile: {2}\n'.format(server_ip, server_port, logfile_loc))

    clientSocket = socket(AF_INET, SOCK_STREAM) # create socket object

    try: 
        logging.info("Trying to connect to {0}:{1}\n".format(server_ip, server_port))
        clientSocket.connect((server_ip, server_port)) # connect to IP
    except Exception as exc: 
        logging.info( "Caught socket exception error: {0}".format(exc))
        exit()

    sentence = input("Send a Message to send to the Server: ") # read message from user
    clientSocket.send(sentence.encode()) # send message to server
    logging.info('Waiting for server reply...\n')

    received_packet = clientSocket.recv(1024) # receive message from server
    logging.info('Received reply from Server.\n')

    logging.info(received_packet.decode()+'\n') # print message

    logging.info('Closing connection.\n')
    clientSocket.close()

main()