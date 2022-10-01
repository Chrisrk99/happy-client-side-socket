## CS 4392 Socket Programming Read Me

### Required Environment 
Any Python 3.2+ Environment

### Adopted Libraries 
argparse: Default Python library used for parsing CLS arguments for the script

socket: Default Python library used for creating and using sockets

logging: Default Python library used for log generation

### Flow of Execution
1. Script imports required libraries 
2. Argument parsing is set up for each option
3. User argument's are read and checked
4. Logger is set up
5. Create socket object using TCP 
6. Try to connect to IP and socket
7. Read a message from user
8. Send this message to server
9. Receive message from server
10. Display message
11. Gracefully exit


### Commands
Example help:
python3 client.py -h 
usage: This script is a client-side socket which connects to a host,
sends a string, receives a packet, and stops.

optional arguments:
  -h, --help            show this help message and exit
  --server <server_ip>, -s <server_ip>
                        The IP address of the the server
  --port <port_#>, -p <port_#>
                        The port the server listens on
  --logfile <log_file_location>, -l <log_file_location>
                        The location to keep the record of packets received.

Example Execution: 
python3 client.py -s <server_ip> -p <port_#> -l <log_file_location>
