# import os 
# import sys 


# def get_error_message(error, error_detail:sys):

#     typ,er,er_tb = error_detail.exc_info()
#     file_name = er_tb.tb_frame.f_code.co_filename
#     error_message = f"Error Occured [{file_name}] at Line_no [{er_tb.tb_lineno}], Error Message : [{error}]"

#     return error_message


# class CustomException(Exception):

#     def __init__(self,error_message, error_details:sys):
#         self.error_message = get_error_message(error_message,error_details)


#     def __str__(self):
#         return self.error_message 