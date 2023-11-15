from machine import UART
import time

uart = UART(2, baudrate=9600, tx=33, rx=25)

def send_at_command(command):
    uart.write(command + b'\r\n')
    time.sleep(1)  # Wait for the command to be sent
    response = uart.read()
    print("Response: ", response.decode('utf-8'))

def Lte_setup():
    print("Sending AT command..."); send_at_command(b'AT')
    print("Sending command for SIM card check..."); send_at_command(b'AT+CPIN?')
    print("Sending command for Signal Quality..."); send_at_command(b'AT+CSQ')
    print("Sending command for Network Registration..."); send_at_command(b'AT+CREG?')
    print("Registering the Network..."); send_at_command(b'AT+CREG=1') 
    print("Network Registering status ..."); send_at_command(b'AT+CGREG?')
    print("Registering the Network..."); send_at_command(b'AT+CREG=1')
    print("CHECK UE INFORMATION..."); send_at_command(b'AT+CPSI?') 
    print("Setting Up APN ..."); send_at_command(b'AT+CGDCONT=1,"IP","airtelgprs"')
    print("Registering the Network..."); send_at_command(b'AT+CGACT=1,1')
    print("Display IP..."); send_at_command(b'AT+CIPSRIP=1')
    print("Registering the Network..."); send_at_command(b'AT+CGACT=1,1')
    
    print("Initial setup done...")
    
def set_gprs():
    print("Initiating HTTP Service..."); send_at_command(b'AT+HTTPINIT')
    print("SSL Check..."); send_at_command(b'AT+HTTPSSL?')
    print("Sending URL..."); send_at_command(b'AT+HTTPPARA="URL",https://WWW.GOOGLE.COM/')
    time.sleep(5) 
    print("Action of HTTP..."); send_at_command(b'AT+HTTPACTION=0')
    print("Read the Head of HTTP response..."); send_at_command(b'AT+HTTPHEAD')  # Read the Head of HTTP response
    print("Read and print the HTTP response..."); send_at_command(b'AT+HTTPREAD?')  # Read and print the HTTP response
    print("Close the HTTP connection..."); send_at_command(b'AT+HTTPTERM')
    print("GPRS SETUP DONE...")
    
if __name__ == '__main__':
    Lte_setup()
    while 1:
        set_gprs()

        

