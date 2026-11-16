import sys
import logging


class Filter_ModuleNameEndsWith(logging.Filter):

    def filter(self, record):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : record          = " + str(record.name))
        print(nameMethod + " : record pathname = " + str(record.pathname))
        print(nameMethod + " : level number    = " + str(record.levelno))

        if record.pathname.endswith("PanelRunScript.py"):

            print(nameMethod + " : record ends with : PanelRunScript.py")

        else:

            print(nameMethod + " : record does not end with : PanelRunScript.py")

        print(nameMethod + " : Exit")

        return record.pathname.endswith("PanelRunScript.py")
        # return record.levelno >= logging.DEBUG
        # logger_root.setLevel(logging.INFO)
        # return record.name == "Panels.PanelRunScript"
