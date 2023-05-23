# Exception handling file

import sys

def error_message_details(error, error_detail:sys):
    _,_,errortb = error_detail.exc_info()
    fileName=errortb.tb_frame.f_code.co_filename
    error_message="Error occured in script [{0}], in line [{1}], error meaage is [{2}]".format(
        fileName, errortb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message