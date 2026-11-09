import sys
from   pathlib \
import (
        Path
       )

from   PySide6.QtCore \
import (
        QThread
       )

shared_dir = Path(__file__).resolve().parent.parent.parent / "PlotGenerators/QuaternionRotation/python"
print("shared_dir = " + str(shared_dir))
sys.path.append(str(shared_dir))

import Config.ObjectDirectory
import QuaternionManipulator


class Worker_GenerateFrames_QuaternionRotation(QThread):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.parent = parent


    def run(self):

        nameMethod = "Worker_GenerateFrames_QuaternionRotation::run"


        thread_current = QThread.currentThread()

        print(nameMethod + " : Current thread = " + str(thread_current))
        print(nameMethod + " : Current thread = " + thread_current.objectName())

        # No!
        #
        # Run the Python code as a script from within the QTermWidget.

        # Invoke the Python class which runs the rotations.
        #
        # Instruct the following code to write certain messages to this program's terminal.
        #
        #   - QuaternionManipulator
        #   -

        if True:

            command = "False", "rotation", "0.577350", "0.577350", "0.577350",  "720",  "1", "0", "0"

            command = "cd ./src/python/PlotGenerators/QuaternionRotation && ./generate_plot_frames.sh\n"

            # Config.ObjectDirectory.object_directory.terminal.sendText("echo \"BLAH!!!\"\n")
            # Config.ObjectDirectory.object_directory.terminal.sendText("pwd\n")
            Config.ObjectDirectory.object_directory.terminal.sendText(command)

        else:

            quaternion_manipulator = QuaternionManipulator.QuaternionManipulator()
            quaternion_manipulator.set_terminal(Config.ObjectDirectory.object_directory.terminal)

            try:

                # if len(sys.argv) != 10:
                #     DisplayUsage.display_usage()
                #
                #     raise ValueError("Exactly 10 arguments were not passed to this program from the command line.")

                quaternion_manipulator.run("False", "rotation", "0.577350", "0.577350", "0.577350",  "720",  "1", "0", "0")

            except Exception as e:

                # DisplayUsage.display_exception(e)

                print("Received the exception: " + str(e))
