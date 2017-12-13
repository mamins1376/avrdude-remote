# avrdude-remote

A RPC-based solution to remotely program your AVR microcontroller through avrdude!

## Background

I currently have a Raspberry Pi and don't want to pay for a programmer hardware.
Since using avrdude 6.1+, bitbanging using linuxgpio api can be used as an interface
to get the job done, I do so. But the issue was the pain of sending the hex file
over ssh and calling avrdude is pretty repeatetive and boring, this way I (and now,
also you!) can merge this script in your Makefile to program the shit in one single
command.

## Usage

Set up the server (the machine which programmer is connected to):

```bash
$ ./server.py localhost:8000
Listening on localhost:8000
```

and on you development machine, program your device this way:

```bash
$ ./avrdude.py ras.pi.ip.addr:8000 [AVRDUDE OPTIONS RIGHT HERE (e.g. -?)]
```

you can just forget the setup and program your local files! say we have flash.hex:

```bash
$ ./avrdude.py ras.pi.ip.addr:8000 -p atmega8 -c usbasp -U flash:w:flash.hex:i
```

## Any Ideas? Bugs?

Happy to dig into it!
