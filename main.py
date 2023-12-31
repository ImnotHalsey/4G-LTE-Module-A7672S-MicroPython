from machine import UART
import time

uart = UART(2, baudrate=9600, tx=33, rx=25)

def send_at_command(command):
    uart.write(command + b'\r\n')
    time.sleep(1)
    response = b''
    while uart.any():
        response += uart.read(1)
    return response.decode('utf-8')

def set_time_using_ntp():
    # Enable NTP
    send_at_command(b'AT+CNTPCID=1')  # Set context ID for NTP
    send_at_command(b'AT+CNTP="pool.ntp.org"')  # Set NTP server
    send_at_command(b'AT+CNTP')  # Start NTP synchronization
    time.sleep(10)  # Wait for NTP synchronization to complete

    # Read and print the current time (optional)
    current_time_response = send_at_command(b'AT+CNTP?')
    print("Current Time:", current_time_response)

if __name__ == '__main__':
    set_time_using_ntp()
