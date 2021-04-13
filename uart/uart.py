import serial
import time

def main():
    print("Opening serial port /dev/ttyAMA1 with baudrate 115200")

    # open port /dev/ttyAMA1 with baudrate 115200 
    ser = serial.Serial("/dev/ttyAMA1", 115200)

    while True:
        print("Write to UART")

        # write a string  
        ser.write(b"Hello from Atlas 200 DK\n")

        # read bytes from serial until newline character
        # this will block until newline character is received
        readdata = ser.readline().decode('utf-8')
        print(f'Reply: {readdata}')


if __name__ == "__main__":
    main()
