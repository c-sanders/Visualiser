import sys
import logging

from   Logging.Filter_LogLevel           import Filter_LogLevel
from   Logging.Filter_ModuleNameEndsWith import Filter_ModuleNameEndsWith
from   Logging.Filter_ModuleNameEquals   import Filter_ModuleNameEquals


logger_root = logging.getLogger()
logger = logger_root


# This class is responsible for configuring the root logger.
#
#

class RootLoggerConfig():

    def __init__(self, log_level = logging.NOTSET):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._configure_root_logger(log_level)

        print(nameMethod + " : Exit")


    def print_message(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        logger_module = logging.getLogger(self.__class__.__name__)

        level_logging = logger.getEffectiveLevel()

        # logging.basicConfig(
        #     level=logging.DEBUG,
        #     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        #     datefmt="%H:%M:%S",
        #     force=True
        # )

        print("Root logger name                  : ", logger.name)
        print("Root logger current logging level : ", level_logging)
        print("Root logger level                 : ", logging.getLevelName(logger.level))
        print("Root logger effective level       : ", logging.getLevelName(logger.getEffectiveLevel()))
        print("Root logger disabled              : ", logger.disabled)
        print("Root logger Propagation           : ", logger.propagate)
        print("Number of handlers                = ", len(logger.handlers))

        for filter in logger.filters:

            print("    ------------------------------------------------------------")
            print("    Filter            : ", filter)
            print("    Filter name       : ", filter.name)
            # s print("        Accepts record    : ", filter.filter(record))
            print("    Filter class      : ", type(filter))
            print("    Filter class      : ", type(filter).__name__)
            print("    Filter dict       : ", vars(filter))
            print("    Filter attributes : ", dir(filter))

        for handler in logger.handlers:

            print("    ------------------------------------------------------------")
            print("    Handler           :", handler)
            print("    Handler level     :", logging.getLevelName(handler.level))

            for filter in handler.filters:

                record = "Test"

                print("        ------------------------------------------------------------")
                print("        Filter            : ", filter)
                print("        Filter name       : ", filter.name)
                #s print("        Accepts record    : ", filter.filter(record))
                print("        Filter class      : ", type(filter))
                print("        Filter class      : ", type(filter).__name__)
                print("        Filter dict       : ", vars(filter))
                print("        Filter attributes : ", dir(filter))

        print(nameMethod + " : Exit")


    def get_logger_root(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")
        print(nameMethod + " : Exit")

        return logger_root


    def get_logger_module(self, module_name):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")
        print(nameMethod + " : Exit")

        return logging.getLogger(module_name)


    def set_root_logger_log_level(self, log_level):

        logger_root.setLevel(log_level)


    def _configure_root_logger(self, log_level):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._add_handlers_to_logger()

        logger_root.setLevel(log_level)

        print(nameMethod + " : Exit")


    def _add_handlers_to_logger(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # Create handlers and register them with the root logger.

        handler   = MyLoggingHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Register the handler with the root logger.

        logger_root.addHandler(handler)

        # logger_root.addFilter(Filter_ModuleNameEndsWith())
        # logger_root.addFilter(Filter_LogLevel())

        print(nameMethod + " : Exit")


class MyLoggingHandler(logging.Handler):

    def __init__(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        super().__init__()

        # Create a filter and register it with this handler.

        self.addFilter(Filter_ModuleNameEndsWith())
        self.addFilter(Filter_LogLevel())

        print(nameMethod + " : Exit")


    def emit(self, record):

        try:

            message = self.format(record)

            print("MyLoggingHandler: " + message)

        except Exception:

            self.handleError(record)