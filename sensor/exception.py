import sys
import os

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message =f"error occer in the file[{filename}] and the line no is [{exc_tb.tb_lineno}] and the error is [{str(error)}]"
    return error_message


class sensorException(Exception):
    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message)
    
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
        