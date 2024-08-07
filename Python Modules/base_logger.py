import logging
from datetime import datetime
import os

def get_logger(name, log_dir, log_level, custom_name='default'):
    '''
    Set up a logger with the given name, log level, and custom log file name.
    '''
    _logs = logging.getLogger(name)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    filename = f'{datetime.now().strftime("%Y%m%d_%H%M%S")}_{custom_name}.log'
    f_handler = logging.FileHandler(os.path.join(log_dir, filename))
    f_format = logging.Formatter('%(asctime)s, %(name)s, %(filename)s, %(lineno)d, %(funcName)s, %(levelname)s, %(message)s')
    f_handler.setFormatter(f_format)
    _logs.addHandler(f_handler)
    
    s_handler = logging.StreamHandler()
    s_format = logging.Formatter('%(asctime)s, %(filename)s, %(lineno)d, %(levelname)s, %(message)s')
    s_handler.setFormatter(s_format)
    _logs.addHandler(s_handler)
    
    _logs.setLevel(log_level)
    return _logs