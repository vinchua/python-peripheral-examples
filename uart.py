import serial
import time

def main():
    print("uart connection test")

    # initialize serial, 
    ser = serial.Serial("/dev/ttyAMA1", 115200)

    while True:
        print("Write to UART")
        ser.write(b"Hello from Atlas 200 DK\n")
        time.sleep(2)
        
        readdata = ser.readline().decode('utf-8')
        print(f'Reply: {readdata}')


if __name__ == "__main__":
    main()
