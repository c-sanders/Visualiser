import sys
import logging


class Filter_LogLevel(logging.Filter):

    def filter(self, record):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : record          = " + str(record.name))
        print(nameMethod + " : record pathname = " + str(record.pathname))

        print(nameMethod + " : Exit")

        return record.levelno >= logging.DEBUG