"""
Author: Abdel Cintron
Create a program in object oriented fashion, No AI to complete code.book references are permitted. 
    Program Breakdown: 
    Purpose: Program that is able to read processes in a computer.
    Function - Read Processes Running in Computer
    Function - Create Folder in "Documents" Folder Named "Logs"
    Function: take List as text and save as text file in a folder on my documents.
    Final Output: Text file must be named "processes" and have the date and time that data was taken.

    sources: https://docs.python.org/3/library/subprocess.html

            https://www.w3schools.com/python/python_file_handling.asp

            https://learn.microsoft.com/en-us/answers/questions/1114754/extract-text-from-command-prompt-window

"""
import subprocess

class ProcessReader:

    # Run Process runs the command to the cmd
    def RunProcess():
        # Refactored Code: Added command variable
        Command = "echo Run Time: %Date% %TIME% > Process.txt & tasklist >> Process.txt"
        Run = subprocess.run(Command, shell=True, check=True)
        return Run

    #New Function for verifying System Information
    def SystemInfo():
                Command = "echo Run Time: %Date% %TIME% > SystemInfo.txt & systeminfo >> SystemInfo.txt"
                Run = subprocess.run(Command, shell=True, check=True)
                return Run

print("Process Reader:")
SystemInfo = ProcessReader.SystemInfo()
RunCommand = ProcessReader.RunProcess()
print("Process Completed")