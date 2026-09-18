'''
Author: Abdel Cintron

Function Definitions and Standard Uses: 

    RunProcess - Runs "tasklist" command
    SystemInfo - Runs "systeminfo" command
'''

import subprocess

class CommandList:
    def TaskList():
        Command = "echo Run Time: %Date% %TIME% > Process.txt & tasklist >> Process.txt"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run

print("Process Reader:")
RunCommand = CommandList.TaskList()
print("Process Completed")