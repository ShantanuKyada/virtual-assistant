
import os
from assitant_detail import *
from output_module import output
from process_module import process
from input_module import take_input
os.system('cls')


# speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    i = take_input()
    o = process(i)
    output(o)