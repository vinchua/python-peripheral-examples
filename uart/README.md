# uart python 
Sample program to demonstrate UART connection between Arduino Uno and Atlas 200 DK board using the `python-periphery` python library.

## Prerequisites
- Atlas 200 DK board, PCB type IT21DMDA
- Arduino Uno R3

## Wired Connection Setup
- Connect Atlas board Tx (pin 16) to Arduino Rx. This sets up the connection to send from Atlas to Arduino.
- Connect Atlas board Rx (pin 18) to Arduino Tx. This requires a voltage divider circuit to step down 5V Arduino Tx to 3.5V Atlas board Rx. 
- Connect Atlas GND to Arduino GND. 

## Run
1. Upload sketch.ino to Arduino Uno board. Open the serial monitor. 
2. On the Atlas board, run `python3 uart.py`. If the UART connection works, you will see the following output on the Atlas board terminal:

```
uart connection test
Write to UART
Reply: Arduino: Hello from Arduino

```
4. To close the program, ctrl+c. 



