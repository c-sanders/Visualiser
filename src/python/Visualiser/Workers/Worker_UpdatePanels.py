import time
from   pathlib import Path
import os

from   PySide6.QtCore \
import (
        QThread,
        Signal
       )


class Worker_UpdatePanels(QThread):

    # Define the signals that this class can emit.

    processing_new_file = Signal(str)

    configure_for_slide = Signal(str)
    configure_for_plot  = Signal(str)
    configure_for_code  = Signal(str)
    configure_for_html  = Signal(str)


    def __init__(self, parent=None):

        super().__init__(parent)


    def run(self):

        index = 0

        # Open the file which contains the list of files.

        with open("./conf/file_list.txt", "r") as file:

            for next_line in file:

                next_line = next_line.strip()

                if next_line.lstrip().startswith("#"):

                    # The current line appears to be a comment.
                    #
                    # As a result, we should just ignore it and read the next line from the file.

                    continue

                if not next_line.strip():

                    # The current line appears to be empty.
                    #
                    # As a result, we should just ignore it and read the next line from the file.

                    continue

                filename, file_type, duration = next_line.split()

                print("filename  = ", filename)
                print("file_type = ", file_type)
                print("duration  = ", duration)

                file_path = Path(filename)

                if (file_path.is_file()) and (os.access(file_path, os.R_OK)):

                    self.processing_new_file.emit(filename)

                else:

                    raise Exception("Cannot access the file : " + file_path.name)

                # Ascertain what type of content the file contains, that is;
                #
                #   - slide
                #   - plot
                #   - code
                #   - html
                #
                # How can we do this? We could use the metadata from the file_list.txt file, or we could use the JSON
                # encoded metadata which is stored inside the file.

                match file_type.lower():

                    case "slide":

                        # Instruct PanelDisplay to configure itself to display slides, if it isn't doing so already.
                        #
                        # It is recommended practice to use signals and slots to interact with the GUI.

                        self.configure_for_slide.emit(filename)

                    case "plot":

                        # Instruct PanelDisplay to configure itself to display plots, if it isn't doing so already.

                        self.configure_for_plot.emit(filename)

                    case "code":

                        # Instruct PanelDisplay to configure itself to display code, if it isn't doing so already.

                        self.configure_for_code.emit(filename)

                    case "html":

                        print("File content : html")

                        self.configure_for_html.emit(filename)

                    case _:

                        print("Unknown content type.")

                time.sleep(int(duration))