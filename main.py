from machine import UART
import time
import utime

uart = UART(2, baudrate=9600, tx=33, rx=25)

Setup_at_commands = [
    ("Sending AT command", b'AT'),
    ("Sending command for SIM card check", b'AT+CPIN?'),
    ("Sending command for Signal Quality", b'AT+CSQ'),
    ("Sending command for Network Registration", b'AT+CREG?'),
    ("Registering the Network", b'AT+CREG=1'),
    ("Network Registering status", b'AT+CGREG?'),
    ("Registering the Network (CGREG)", b'AT+CGREG=1'),
    ("CHECK UE INFORMATION", b'AT+CPSI?'),
    ("Setting Up APN", b'AT+CGDCONT=1,"IP","airtelgprs"'),
    ("Registering the Network (CGACT)", b'AT+CGACT=1,1'),
    ("Get time",b'AT+CCLK?')]

gprs_commands = [
    ("Initiating HTTP Service", b'AT+HTTPINIT'),
    ("SSL Check", b'AT+CCHSTART'),
    ("Open SSL", b'AT+CCHOPEN'),
    ("Print IP Address", b'AT+CCHADDR'),
    ("Sending URL", b'AT+HTTPPARA="URL","http://www.linkedin.com/"'),
    ("Action of HTTP", b'AT+HTTPACTION=0'),
    ("Read the Head of HTTP response", b'AT+HTTPHEAD'),
    ("Read and print the HTTP response", b'AT+HTTPREAD?')]

def get_time():
    current_time = utime.time()
    formatted_time = utime.localtime(current_time)
    print("Current Time:", formatted_time)
    return

def send_at_command(command):
    uart.write(command + b'\r\n')
    time.sleep(1)
    response = b''
    while uart.any():
        response += uart.read(1)
    return response.decode('utf-8')

def run_command(commands):
    for label, command in commands:
        print(f"Command sent: {label}...")
        res = send_at_command(command)
        print("Response:", res)
    print("Setup done...")
    time.sleep(3)

if __name__ == '__main__':
    run_command(Setup_at_commands)
    run_command(gprs_commands)
    run_command(gprs_commands)
