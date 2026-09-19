'''
Author: Abdel Cintron

Function Definitions and Standard Uses: 
    TaskList - Runs "tasklist" command
'''

import subprocess

class CommandList:
    def TaskList():
        Command = "tasklist"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run

    def SystemInfo():
        Command = "systeminfo"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run

    def IpConfig():
        Command = "ipconfig"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run

    def Netstat():
        Command = "netstat"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run