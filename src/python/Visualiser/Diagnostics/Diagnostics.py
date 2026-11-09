import Config.ObjectDirectory


class Diagnostics():

    def __init__(self):

        pass


    # def set_terminal(self, terminal):

        # self.terminal = terminal


    def run_diagnostics(self):

        print(Config.ObjectDirectory.object_directory.terminal.scroll.__module__)
        print(Config.ObjectDirectory.object_directory.terminal.scrollToEnd.__module__)

        print([
            name for name in dir(Config.ObjectDirectory.object_directory.terminal)
            if any(term in name.lower()
                   for term in ("scroll", "bar", "history", "line"))
        ]
        )

        print("History lines:", Config.ObjectDirectory.object_directory.terminal.historyLinesCount())
        print("History size:",  Config.ObjectDirectory.object_directory.terminal.historySize())
        print("Visible lines:", Config.ObjectDirectory.object_directory.terminal.screenLinesCount())

        print(type(Config.ObjectDirectory.object_directory.terminal))
        print(type(Config.ObjectDirectory.object_directory.terminal).__module__)
        print(type(Config.ObjectDirectory.object_directory.terminal).__mro__)


    def list_terminal_methods_scroll(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(Config.ObjectDirectory.object_directory.terminal)
               if "scroll" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_scheme(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(Config.ObjectDirectory.object_directory.terminal)
               if "scheme" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_history(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(Config.ObjectDirectory.object_directory.terminal)
               if "history" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_bar(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(Config.ObjectDirectory.object_directory.terminal)
               if "scrollbar" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
