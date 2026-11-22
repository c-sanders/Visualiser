import inspect
import sys
import time
import subprocess
from   pathlib \
import (
        Path
       )
import logging

from   PySide6.QtCore \
import (
        QThread,
        Signal
       )

shared_dir = Path(__file__).resolve().parent.parent.parent / "PlotGenerators/QuaternionRotation/python"
print("shared_dir = " + str(shared_dir))
sys.path.append(str(shared_dir))

import Config.ObjectDirectory
import QuaternionManipulator


logger = logging.getLogger(__file__)


class Worker_Generate_UML_class_diagrams(QThread):

    signal_terminal_command = Signal(str)


    def __init__(self, parent=None, run_in_terminal=False):

        super().__init__(parent)

        self.parent = parent

        self.run_in_terminal = run_in_terminal


    def run(self):

        nameMethod = f"{self.__class__.__name__}::{inspect.currentframe().f_code.co_name}"


        thread_current = QThread.currentThread()

        print(nameMethod + " : Current thread = " + str(thread_current))
        print(nameMethod + " : Current thread = " + thread_current.objectName())

        print(nameMethod + " : Enter")

        excludes = [
            "./src/python/Visualiser/Visualiser.py",
            "./src/python/PlotGenerators/QuaternionRotation/docs/conf.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/quaternion_rotation_over_unit_sphere.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/SubPlotAgent_Quaternion_PreMultiply.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/PlottingAgent.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/PlotHandleAgent_SubPlot_2.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/QuaternionManipulator.py",
            "./src/python/PlotGenerators/QuaternionRotation/python/Utils.py",
        ]

        command = [
            "find", "./",
            "-type", "d", "-path", "./src/python/Visualiser/old", "-prune",
            "-o",
            "-type", "f", "-name", "*.py",
            "-print",
        ]

        # for path in excludes:

            # command += ["!", "-path", path]

        # command.append("-print0")

        print(nameMethod + " : command = " + str(command))

        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print("result = " + str(result.stdout))

        time.sleep(1)

        # self.signal_terminal_command.emit("exec 4>&2\n")
        # self.signal_terminal_command.emit("exec 2> /dev/null\n")

        # self.signal_terminal_command.emit("cat > files.txt\n")

        time.sleep(1)

        # self.signal_terminal_command.emit("\n")
        # self.signal_terminal_command.emit("\n")

        for filename in result.stdout.strip().split("\n"):

            filename_base = Path(filename).name

            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # print(nameMethod + " : filename = " + filename)

            print("filename_base = " + str(filename_base))

            self.signal_terminal_command.emit("--> " + filename + "\n")
            self.signal_terminal_command.emit(filename_base + "\n")

            time.sleep(1)

            result = subprocess.run(
                       [
                         "./scripts/generate_uml_class_diagram_for_python_file.sh",
                         filename
                       ],
                       capture_output=True,
                       text=True
                     )

            # print("Have run the BASH script")
            # print("result = " + str(result.stdout))
            # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

            # End of the for loop.

        self.signal_terminal_command.emit("\x04")


        print(nameMethod + " : Exit")




