# i2c python sample
Sample program to demonstrate I2C connection between Arduino Uno and Atlas 200 DK board using the `python-periphery` python library.

## Prerequisites
- Atlas 200 DK board, PCB type IT21DMDA
- Arduino Uno R3

## Wired Connection Setup
- The Atlas board is the master and connects to the Arduino slave
- Connect Atlas board I2C2-SDA (pin 3) to Arduino SDA. 
- Connect Atlas board I2C2-SCL (pin 5) to Arduino SCL. 
- Connect Atlas GND to Arduino GND. 

## Run
1. Upload sketch.ino to Arduino Uno board. Open the serial monitor. 
2. On the Atlas board, run `python3 i2c.py`. If the connection works, you will see "Hello from Atlas" on the Arduino serial monitor, and the following output on the Atlas board terminal:

```
i2c connection test
Write to I2C
Read from I2C: Hello from Arduino
```


## pyserial
[pyserial](https://pyserial.readthedocs.io/en/latest/) is a python module encapsulates the access for the serial port.

