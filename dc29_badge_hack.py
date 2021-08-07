#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Sat 07 August 2021 23:15:51 CEST
# Author: Nicolas Flandrois
# Licence: MIT (2021)
# Description: DEFCON 29 (2021) badge's hack.

from secrets import token_hex


def dc29_badge(count: int, prefix: str, isSignalBadge: bool, starttoken: str):
    '''
    This function will automatically generate Defcon 29 (2021) handshares.
    By providing the "req" token (option 4), the output is the "resp" that you
    need to copy and paste in (option 5) the Badge's UI.

    This short hack is based on the work of igloo22225
    https://github.com/igloo22225/dc29-badge-response-generator

    Input Arguments
    -------------------
        count : int
            This will determine the number of outputs displayed (printed) by
            the function.

        prefix : str
            The prefix has something to do with the status of a target/fake
            badge.
            Wheither you get a signal from a Tier 'AA'.
            Or you're sharing the signal 'AB', 'AC'.
            Could this section of information also indicate the kind of badge?

        isSignalBadge : bool
            Defining if the Tier (fake) badge is identified as a "Signal".

        starttoken : str
            This is your 'req' token provided by the option 3
            of the badge's UI.
                - starttoken[2:4]
                    - Second hex set, also a component in the ID?
                - starttoken[8:10]
                    - Fifth hex set
                - starttoken[16:20]
                    - 9th and 10th hex set, the ID of the device

    Output
    ----------
        The function will print/display the 'resp' token to input in badge UI.
        Some text will help identify which are what:
            To get to the signal tier  OR  To spread the signal
        The number of response is determined by 'count' input argument.
    '''
    if isSignalBadge:
        typeofresp = "7F"
    else:
        typeofresp = "01"

    for _ in range(count):
        print(f'{token_hex(1)}{starttoken[2:4]}{token_hex(2)}\
{starttoken[8:10]}{prefix}{token_hex(2)}{starttoken[16:20]}13000100\
{typeofresp}{token_hex(1)}'.upper())


if __name__ == '__main__':
    # starttoken = input("Input one of your request tokens:\t")

    starttoken = '4DF10F76EF35775B0087121A20090748'

    print(f"""Your req token is {starttoken}.
    \nCopy-paste the following strings as the resp token.
    \nTo get to the signal tier: """)
    dc29_badge(10, "AA", True, starttoken)
    print('\nTo spread the signal: ')
    dc29_badge(10, "AB", False, starttoken)
    dc29_badge(10, "AC", False, starttoken)
    dc29_badge(10, "AD", False, starttoken)
    dc29_badge(10, "AE", False, starttoken)
    dc29_badge(10, "AF", False, starttoken)
    dc29_badge(10, "AG", False, starttoken)
