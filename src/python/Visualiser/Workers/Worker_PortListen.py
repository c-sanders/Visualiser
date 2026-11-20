import os
import socket

from   PySide6.QtCore \
import (
        QThread,
        Signal
       )

import Config.ObjectDirectory


class Worker_PortListen(QThread):

    # Define the signals that this class can emit.

    processing_new_file = Signal(str)


    def __init__(self, host, port, parent=None):

        if parent is None:

            raise Exception("Parent object is None")

        super().__init__(parent)

        self.parent = parent

        self.host = host
        self.port = port

        print("IP address  = " + self.host)
        print("Port number = " + str(self.port))


    def run(self):

        nameMethod = "Worker_PortListen::run"


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

            server.bind((self.host, self.port))
            server.listen()

            print(f"Listening on port {self.port}...")

            while True:
                conn, addr = server.accept()

                with conn:

                    print(f"Connection from {addr}")

                    while True:

                        data = conn.recv(4096)

                        if not data:

                            break

                        value = data.decode("utf-8", errors="replace")

                        print(f"Received: {value!r}")
                        print("Length of received value = " + str(len(value)))

                        if value.strip() == "q":

                            print("Query")

                            print("Label size                = ", self.parent.panel_display_terminal.panel_display.label.size())
                            print("Label contents size       = ", self.parent.panel_display_terminal.panel_display.label.contentsRect())
                            print("PanelDisplay.label.pixmap = ", self.parent.panel_display_terminal.panel_display.label.pixmap().size())
                            print("PanelDisplay              = ", self.parent.panel_display_terminal.panel_display.size())
                            print("PanelTerminal             = ", self.parent.panel_display_terminal.panel_terminal.size())
                            print("PanelDisplayTerminal      = ", self.parent.panel_display_terminal.size())

                            # print("Label size:", self.label.size())
                            # print("Label contents:", self.label.contentsRect())
                            # print("Image size:", image.size())

                        elif value == "q\n":

                            print("Query with newline")

                        elif (value == "complete\n") or \
                             (value == "complete"):

                            # The frame generation operation appears to have completed.

                            Config.ObjectDirectory.object_directory.panel_run_script.button_file_stop_script.setEnabled(False)
                            Config.ObjectDirectory.object_directory.panel_run_script.button_file_run_script.setEnabled(True)

                        else:

                            # Assuming that the received data is a filename.

                            filename = value

                            if os.path.exists(filename) :

                                print("   Filename actually exists")

                                # Maybe instruct;
                                #
                                #   - the GUI to load the frame
                                #   - the GUI to take a screenshot of itself

                                # Config.ObjectDirectory.object_directory.

                                filename_base       = os.path.basename(filename)
                                filename_screenshot = "./slides/screenshot_" + filename_base

                                print(nameMethod + " : filename            = " + filename)
                                print(nameMethod + " : filename_base       = " + filename_base)
                                print(nameMethod + " : filename_screenshot = " + filename_screenshot)

                                self.processing_new_file.emit(filename)

                                pixmap = Config.ObjectDirectory.object_directory.main_window.grab()
                                pixmap.save(filename_screenshot)

                            else :

                                print("   Warning. Filename doesn't seem to exist")