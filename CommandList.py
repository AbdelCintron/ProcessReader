'''
Author: Abdel Cintron

Function Definitions and Standard Uses: 
    TaskList - Runs "tasklist" command
'''

import subprocess

class CommandList: 
    
    def TaskList():
        Command = "tasklist"
        Run = subprocess.run(Command, shell=True, check=True, capture_output=True, text=True)
        return Run