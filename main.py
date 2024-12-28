from sensor.exception import sensorException
import os
import sys

def test_exception():
    try:
        a=1/0
    except Exception as e:
        #print(e)
        raise sensorException(e,sys)

if __name__ =="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)

