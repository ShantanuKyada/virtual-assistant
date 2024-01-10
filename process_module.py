from time_module import get_time
from output_module import output
from input_module import take_input
from database import *

def process(query):
    answer = get_answer_from_memory(query)
    if answer == "get time detail":
        return get_time()
    else:
        print("I don't know what it means?")
        ans=take_input()
        if "it means" in ans:
            ans=ans.replace("it means","")
            ans= ans.strip()
            value=get_answer_from_memory(ans)
            if value == "":
                return "Can't help with this one."
            else:
                insert_questions_and_answer(ans,value)
                return"Thanks,I will remember"
            
            