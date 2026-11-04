import sys
from   pathlib \
import (
        Path
       )
import subprocess
import json
import time

shared_dir = Path(__file__).resolve().parent.parent.parent / "PlotGenerators/QuaternionRotation/python"
print("shared_dir = " + str(shared_dir))
sys.path.append(str(shared_dir))

from   PySide6.QtCore \
import (
        QSettings,
        QThread,
        Signal,
        Slot
       )
from   PySide6.QtGui \
import (
        QFont
       )
from   PySide6.QtWidgets \
import (
        QMainWindow,
        QFrame,
        QHBoxLayout,
        QVBoxLayout,
        QGroupBox,
        QLineEdit,
        QLabel,
        QPlainTextEdit
       )
from   PySide6.QtNetwork \
import (
        QHostAddress
       )

from   pyside6_qtermwidget \
import (
        QTermWidget
       )
from   pyside6_scintilla \
import (
        ScintillaEdit
       )


from PIL import Image

import Config.ServiceObjects
import Config.SettingsConfig
import Workers.Worker_PortListen
import Workers.Worker_UpdatePanels
from   Panels.PanelData_Slide        import PanelData_Slide
from   Panels.PanelData_Plot         import PanelData_Plot
from   Panels.PanelFrameTerminal     import PanelFrameTerminal
from   Panels.PanelSettings          import PanelSettings
from   Panels.PanelRunScript         import PanelRunScript
from   Panels.MenuBar_MainWindow     import MenuBar_MainWindow

import Diagnostics.Diagnostics

import QuaternionManipulator


class \
MainWindow \
(
 QMainWindow
):

    def __init__(self, parent=None):

        if Config.ServiceObjects.main_window is not None:

            raise Exception("It looks like a main window already exists.")

        else:

            Config.ServiceObjects.main_window = self

        super().__init__(parent)

        self.diagnostics = Diagnostics.Diagnostics.Diagnostics()

        self.settings = QSettings("GravitasToolWorks", "Quaternion_rotation_visualiser")

        self._import_settings()

        self._read_settings_from_config_file()

        self._create_gui_components()
        self._configure_gui_components()

        self._configure_terminal()

        self.diagnostics.set_terminal(self.panel_frame_terminal.panel_terminal.terminal)

        if self.run_diagnostic_code:

            self.diagnostics.run_diagnostics()

        self.worker = None


    def startup(self):

        print("Quaternion_rotation_visualiser::startup : Enter")

        self.panel_frame_terminal.panel_terminal.terminal.setFocus()

        print("Quaternion_rotation_visualiser::startup : Exit")


    def _configure_terminal(self):

        font         = Config.ServiceObjects.settings_config.font_size
        color_scheme = Config.ServiceObjects.settings_config.color_scheme

        self.panel_frame_terminal.panel_terminal.terminal.setTerminalFont(QFont("Monospace", font))
        self.panel_frame_terminal.panel_terminal.terminal.setColorScheme(color_scheme)


    def closeEvent(self, event):

        nameMethod = self.__class__.__name__


        print(nameMethod + " : Enter")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("save_settings_on_exit                                = " + str(self.settings.value("save_settings_on_exit", True, type=bool)))
        print("font_size                                            = " + str(self.settings.value("font_size", 14, type=int)))
        print("color_scheme                                         = " + str(self.settings.value("color_scheme", "Linux", type=str)))
        print("----------------------------------------")
        print("ServiceObjects.settings_config.save_settings_on_exit = " + str(Config.ServiceObjects.settings_config.save_settings_on_exit))
        print("ServiceObjects.settings_config.font_size             = " + str(Config.ServiceObjects.settings_config.font_size))
        print("ServiceObjects.settings_config.color_scheme          = " + str(Config.ServiceObjects.settings_config.color_scheme))
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        self.settings.setValue("save_settings_on_exit", ServiceObjects.settings_config.save_settings_on_exit)
        self.settings.setValue("font_size",             ServiceObjects.settings_config.font_size)
        self.settings.setValue("color_scheme",          ServiceObjects.settings_config.color_scheme)

        self.settings.sync()

        print(nameMethod + " : Exit")

        # Accept the close event.

        event.accept()


    def _import_settings(self) :

        self.ip_address          = "127.0.0.1"
        self.tcp_port            = 5000

        self.run_diagnostic_code = True

        self.json_config_file    = "./settings.json"
        self.title_window        = "My custom terminal (Implemented using Python and PySide)"
        self.dimensions_window   = (1024, 768)


    def _read_settings_from_config_file(self):

        Config.ServiceObjects.settings_config = Config.SettingsConfig.SettingsConfig()


        print("MainWindow::_read_settings_from_config_file : Enter")

        Config.ServiceObjects.settings_config.save_settings_on_exit = str(self.settings.value("save_settings_on_exit", True, type=bool))
        Config.ServiceObjects.settings_config.font_size             = int(self.settings.value("font_size", 14, type=int))
        Config.ServiceObjects.settings_config.color_scheme          = str(self.settings.value("color_scheme", "Linux", type=str))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("save_settings_on_exit                                = " + str(self.settings.value("save_settings_on_exit", True, type=bool)))
        print("font_size                                            = " + str(self.settings.value("font_size", 14, type=int)))
        print("color_scheme                                         = " + str(self.settings.value("color_scheme", "Linux", type=str)))
        print("----------------------------------------")
        print("Config.ServiceObjects.settings_config.save_settings_on_exit = " + str(Config.ServiceObjects.settings_config.save_settings_on_exit))
        print("Config.ServiceObjects.settings_config.font_size             = " + str(Config.ServiceObjects.settings_config.font_size))
        print("Config.ServiceObjects.settings_config.color_scheme          = " + str(Config.ServiceObjects.settings_config.color_scheme))
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def _create_gui_components(self):

        self.menu_builder = MenuBar_MainWindow()
        self.menu_builder.set_parent(self)

        self.frame_top = QFrame(self)
        self.layout_top = QVBoxLayout(self.frame_top)

        self.layout    = QHBoxLayout()

        self.groupbox_file_current = QGroupBox()
        self.layout_file_current = QHBoxLayout()
        self.groupbox_file_current.setLayout(self.layout_file_current)
        self.label_file_current = QLabel("Current frame file :")
        self.file_current = QLineEdit()
        self.layout_file_current.addWidget(self.label_file_current)
        self.layout_file_current.addWidget(self.file_current)

        self.layout_top.addLayout(self.layout)
        self.layout_top.addWidget(self.groupbox_file_current)

        self.panel_display_data_slide = PanelData_Slide()
        self.panel_display_data_plot  = PanelData_Plot()
        self.panel_frame_terminal     = PanelFrameTerminal()
        self.panel_display_code       = ScintillaEdit()

        # Populate the editor with some Python code.
        self.panel_display_code.setText(
            'import sys\n\n'
            'def main():\n'
            '    print("Hello, Scintilla!")\n\n'
            'if __name__ == "__main__":\n'
            '    main()\n'
        )

        self.panel_run_script = PanelRunScript(self)

        self.menu_builder.create_menu_bar()

        self.panel_settings   = PanelSettings(self)


    def _configure_gui_components(self):

        self.setCentralWidget(self.frame_top)

        self.frame_top.setLayout(self.layout)

        self.layout.addWidget(self.panel_display_data_slide, 1)
        self.layout.addWidget(self.panel_frame_terminal,   5)

        self._frame_type_current = "Slide"


    def get_host(self):

        return self.ip_address


    def startWorkerThread(self):

        if (self.worker is not None) and (self.worker.isRunning()):

            return

        self.worker_port_listen = Workers.Worker_PortListen.Worker_PortListen(self.ip_address, self.tcp_port, self)
        self.worker             = Workers.Worker_UpdatePanels.Worker_UpdatePanels()

        # Connect the appropriate signals to the appropriate slots.

        self.worker.processing_new_file.connect \
        (
         self._display_filename_in_field
        )

        self.worker.configure_for_slide.connect \
        (
         self._configure_for_slide
        )

        self.worker.configure_for_plot.connect \
        (
         self._configure_for_plot
        )

        if False:

            # Update the panel which displays the plot, i.e. PanelPlot.

            self.worker.update_panel_display.connect \
            (
                self.panel_frame_terminal.panel_display.update_plot
            )

            # Update the side panel which displays the data associated with the plot, i.e. PanelDisplayData.

            self.worker.update_panel_display_data.connect \
            (
                    self._update_panel_display_data
            )

            self.worker.update_panel_display_slide.connect \
            (
                self.panel_display_data_slide.update_panel
            )

        # self.worker.update_angle.connect(
        #     lambda value:
        #     self.panel_display_data.angle_rotation.setText(value)
        # )

        self.worker_port_listen.start()
        self.worker.start()


    @Slot()
    def panel_settings_display(self):

        print("Quaternion_rotation_visualiser::_panel_settings_display : Enter")

        # Create the appropriate panel and display it.

        if self.panel_settings is None:

            self.panel_settings = PanelSettings(self)
            # self.panel_settings.set_main_window(self)

        print("Quaternion_rotation_visualiser::_panel_settings_display : About to show panel.")

        self.panel_settings.show()
        self.panel_settings.raise_()
        self.panel_settings.activateWindow()

        print("Quaternion_rotation_visualiser::_panel_settings_display : Exit")


    @Slot()
    def build_frames_quaternion_rotation(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Exit")

        self.generate_frames_quaternion_rotation()

        print(nameMethod + " : Exit")


    @Slot()
    def panel_run_script_display(self):

        print("Quaternion_rotation_visualiser::_panel_settings_display : Enter")

        # Create the appropriate panel and display it.

        if self.panel_run_script is None:

            self.panel_run_script = PanelRunScript(self)
            # self.panel_settings.set_main_window(self)

        print("Quaternion_rotation_visualiser::_panel_settings_display : About to show panel.")

        self.panel_run_script.show()
        self.panel_run_script.raise_()
        self.panel_run_script.activateWindow()

        print("Quaternion_rotation_visualiser::_panel_settings_display : Exit")


    @Slot(str)
    def _display_filename_in_field(self, filename):

        nameMethod = "Visualiser_MainWindow::_display_filename_on_terminal (Slot)"


        print(nameMethod + " : Enter")

        # self.panel_display_terminal.panel_terminal.terminal.sendText("date +\"%H:%M:%S\" && echo \"Next file = " + filename + "\"\n")
        # self.panel_frame_terminal.panel_terminal.terminal.sendText(filename + " &> /dev/null\n")
        self.file_current.setText(filename)
        print(nameMethod + " : Exit")


    def _configure_for_slide(self, filename):

        nameMethod = "Visualiser_MainWindow::_configure_for_slide"


        print(nameMethod + " : Enter")

        print(nameMethod + " : filename = " + filename)

        # Inform the following panels that the signal has been received;
        #
        #   - PanelDisplayData_Slide
        #   - PanelDisplayTerminal / PanelDisplay

        self.panel_display_data_slide.update_panel(filename)
        self.panel_frame_terminal.update_panel(filename)

        print(nameMethod + " : Exit")


    def _configure_for_plot(self, filename):

        nameMethod = "MainWindow::_configure_for_plot"


        print(nameMethod + " : Enter")

        print(nameMethod + " : filename = " + filename)

        # Inform the following panels that the signal has been received;
        #
        #   - PanelDisplayData_Slide
        #   - PanelDisplayTerminal / PanelDisplay

        self.panel_display_data_plot.update_panel(filename)
        self.panel_frame_terminal.update_panel(filename)

        self.layout.replaceWidget(self.panel_display_data_slide, self.panel_display_data_plot)

        self.panel_display_data_slide.hide()

        print(nameMethod + " : Exit")


    # @Slot()
    def build_latex_slides(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : Config.SettingsConfig.SettingsConfig.command_build_latex_slides = " + str(Config.ServiceObjects.settings_config.command_build_latex_slides))

        self.panel_frame_terminal.panel_terminal.terminal.sendText(Config.ServiceObjects.settings_config.command_build_latex_slides)

        print(nameMethod + " : Exit")


    def build_uml_class_diagrams(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        command = "pyreverse \
                   -c Visualiser \
                   -a 1 \
                   -s 1 \
                   -f ALL \
                   -o html \
                   src/python/Visualiser"

        result = subprocess.run(
            [
             "pwd"
            ],
            capture_output=True,
            text=True
        )

        print("result = " + str(result.stdout))

        if True:

            files = [
                     "./src/python/Visualiser/Visualiser.py",
                     "./src/python/Visualiser/Panels/MenuBar_MainWindow.py",
                     "./src/python/Visualiser/Panels/MainWindow.py"
                     ]

            # "pyreverse",
            # "--verbose",
            # "--source-roots=./src/python/Visualiser",
            # "-c Visualiser",
            # "-a 1",
            # "-s 1",
            # "-f ALL",
            # "src/python/Visualiser"

            # "pyreverse",
            # "-o svg",
            # "-c MenuBar_MainWindow",
            # "./src/python/Visualiser/Panels/MenuBar_MainWindow.py"

            for filename in files:

                print("filename = " + filename)

                result = subprocess.run(
                    [
                        "pyreverse",
                        "-o", "html",
                        # "-c", "MenuBar_MainWindow",
                        filename
                    ],
                    capture_output=True,
                    text=True
                )

                print("result stdout = " + str(result.stdout))
                print("result stderr = " + str(result.stderr))

        print(nameMethod + " : Exit")


    def build_uml_sequence_diagrams(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : Exit")


    # TODO : Run this method in a separate worker thread.

    def generate_frames_quaternion_rotation(self):

        nameMethod = "MainWindow::run_script"


        print(nameMethod + " : Enter")

        # print(nameMethod + " : Config.SettingsConfig.SettingsConfig.command_build_latex_slides = " + str(Config.ServiceObjects.settings_config.command_build_latex_slides))

        # self.panel_frame_terminal.panel_terminal.terminal.sendText(Config.ServiceObjects.settings_config. command_run_script)

        self.panel_frame_terminal.panel_terminal.terminal.sendText("echo \"In method : MainWindow::run_script\"")

        # Invoke the Python class which runs the rotations.
        #
        # Instruct the following code to write certain messages to this program's terminal.
        #
        #   - QuaternionManipulator
        #   -

        # >>>>>>>>>>

        quaternion_manipulator = QuaternionManipulator.QuaternionManipulator()

        try:

            # if len(sys.argv) != 10:
            #     DisplayUsage.display_usage()
            #
            #     raise ValueError("Exactly 10 arguments were not passed to this program from the command line.")

            quaternion_manipulator.run("False", "rotation", "0.577350", "0.577350", "0.577350",  "720",  "1", "0", "0")

        except Exception as e:

            # DisplayUsage.display_exception(e)

            print("Received the exception: " + str(e))

        # <<<<<<<<<<

        print(nameMethod + " : Exit")
