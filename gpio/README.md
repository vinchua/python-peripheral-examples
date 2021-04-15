# gpio python sample 
Sample program to demonstrate driving a GPIO port on the Atlas 200 DK board using the `python-periphery` python library. The python program will turn on and off the GPIO0 pin every 2 seconds.

## Prerequisites
- Atlas 200 DK board, PCB type IT21DMDA

## Setup
- No setup circuit required, can test with LED
- This sample uses GPIO0 (pin 7), which has the file descriptor of GPIO504

## Run
1. On the Atlas board, run `python3 gpio.py`. If the UART connection works, you will see the following output on the Atlas board terminal:

```
gpio connection test
Set gpio504 to True
Set gpio504 to False
Set gpio504 to True
Set gpio504 to False
...
```

2. To close the program, ctrl+c. 



