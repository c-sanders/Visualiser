class Diagnostics():

    def __init__(self):

        pass


    def set_terminal(self, terminal):

        self.terminal = terminal


    def run_diagnostics(self):

        print(self.terminal.scroll.__module__)
        print(self.terminal.scrollToEnd.__module__)

        print([
            name for name in dir(self.terminal)
            if any(term in name.lower()
                   for term in ("scroll", "bar", "history", "line"))
        ]
        )

        print("History lines:", self.terminal.historyLinesCount())
        print("History size:",  self.terminal.historySize())
        print("Visible lines:", self.terminal.screenLinesCount())

        print(type(self.terminal))
        print(type(self.terminal).__module__)
        print(type(self.terminal).__mro__)


    def list_terminal_methods_scroll(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(self.terminal)
               if "scroll" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_scheme(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(self.terminal)
               if "scheme" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_history(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(self.terminal)
               if "history" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def list_terminal_methods_bar(self):

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(self.terminal)
               if "scrollbar" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
