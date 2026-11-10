import sys
import logging

from   PySide6.QtCore \
import (
       Qt,
       QThread,
       Slot
       )
from   PySide6.QtGui \
import (
       QFont
       )
from   PySide6.QtWidgets \
import (
       QWidget,
       QVBoxLayout,
       QHBoxLayout,
       QGroupBox,
       QLabel,
       QCheckBox,
       QComboBox,
       QLineEdit,
       QTextEdit,
       QPushButton,
       QFileDialog
       )

# import Config.ObjectDirectory
import Workers.Worker_GenerateFrames_QuaternionRotation


class PanelRunScript(QWidget):

    def __init__(self, parent=None):

        super().__init__(None)

        self._create_gui_components()
        self._configure_gui_components()

        self.setWindowTitle("Run script panel")
        self.resize(1200, 500)

        self._connect_signals_to_slots()


    def _create_gui_components(self):

        self.layout_top          = QVBoxLayout(self)

        self.group_box           = QGroupBox("Script")
        self.layout_group_box    = QVBoxLayout()

        self.label_overview      = QLabel("Overview of script")

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(
            "Method : PanelRunScript::_connect_signals_to_slots\n"
            "==================================================\n"
            "\n"
            "self.button_file_run_script.clicked.connect(Config.ObjectDirectory.main_window.generate_frames_quaternion_rotation)\n"
            "\n"
            "Method : MainWindow::generate_frames_quaternion_rotation\n"
            "========================================================\n"
            "\n"
            "self.worker_thread = Workers.Worker_GenerateFrames_QuaternionRotation.Worker_GenerateFrames_QuaternionRotation()\n"
            "self.worker_thread.run()\n"
            "\n"
            "Method : Worker_GenerateFrames_QuaternionRotation::run\n"
            "======================================================\n"
            "\n"
            "quaternion_manipulator = QuaternionManipulator.QuaternionManipulator()\n"
            "quaternion_manipulator.run(\"False\", \"rotation\", \"0.577350\", \"0.577350\", \"0.577350\", \"720\", \"1\", \"0\", \"0\")\n"
            "\n"    
            "Class : QuaternionManipulator\n"
            "===================================\n"
            "\n"
            "QuaternionManipulator::run\n"
            "  |-QuaternionManipulator::_generate_plots\n"
            "      |- while self.azimuth_view <= 720 :\n"
            "           |- self._perform_quaternion_operations()\n"
            "                |- self._preMultiplyVectorUsingQuaternion()\n"
            "                |    |- subprocess.run(...)   ### This is where the Haskell code gets called.\n"
            "                |- self._rotateVectorUsingQuaternion()\n"
            "                     |- subprocess.run(...)   ### This is where the Haskell code gets called.\n"
        )
        font = QFont("Monospace", 10)
        self.text_edit.setFont(font)

        self.text_edit.setReadOnly(True)

        self.script_combobox     = QComboBox()
        self.debug_combobox      = QComboBox()

        self.label_file_list     = QLabel("Frame generating script")
        self.label_logging_level = QLabel("Script logging level")
        self.layout_file_list    = QHBoxLayout()
        self.file_list           = QLineEdit()
        self.button_file_select  = QPushButton("Select")

        self.button_file_run_script  = QPushButton("Run script")
        self.button_file_stop_script = QPushButton("Stop script")

        self.layout_buttons_top  = QHBoxLayout()
        self.layout_buttons      = QHBoxLayout()
        self.button_exit         = QPushButton("Exit")


    def _configure_gui_components(self):

        self.setLayout(self.layout_top)

        self.layout_top.addWidget(self.group_box)

        self.group_box.setLayout(self.layout_group_box)

        self.layout_group_box.addWidget(self.label_file_list)
        self.layout_group_box.addWidget(self.script_combobox)
        self.layout_group_box.addWidget(self.label_logging_level)
        self.layout_group_box.addWidget(self.debug_combobox)

        self.script_combobox.addItem("Quaternion rotation  :  ./src/python/PlotGenerators/QuaternionRotation/generate_plot_frames.sh")
        self.script_combobox.addItem("Euler's formula flyaround")
        self.script_combobox.addItem("Euler's formula flyaround for varying base")

        self.debug_combobox.addItems(["DEBUG",
                                      "INFO",
                                      "WARNING",
                                      "ERROR",
                                      "CRITICAL",
                                      "NOTSET"])

        self.layout_group_box.addLayout(self.layout_buttons_top)

        self.layout_buttons_top.addStretch(1)
        self.layout_buttons_top.addWidget(self.button_file_run_script,  Qt.AlignCenter)
        self.layout_buttons_top.addWidget(self.button_file_stop_script, Qt.AlignCenter)
        self.layout_buttons_top.addStretch(1)

        self.layout_group_box.addWidget(self.label_overview)
        self.layout_group_box.addWidget(self.text_edit)
        self.button_file_run_script.setFixedSize(120, 35)
        self.button_file_run_script.setShortcut("Ctrl+R")
        self.button_file_run_script.setToolTip("Press Ctrl+R to run the selected script")
        self.button_file_stop_script.setFixedSize(120, 35)
        # self.button_file_stop_script.setShortcut("Ctrl+R")
        self.button_file_stop_script.setToolTip("Stop a script if one is currently running")

        # self.layout_file_list.addWidget(self.file_list)
        # self.layout_file_list.addWidget(self.button_file_select)
        # self.button_file_select.setFixedSize(120, 35)

        # self.layout_group_box.addStretch(1)

        self.layout_top.addLayout(self.layout_buttons)

        self.layout_buttons.addStretch(1)
        # self.layout_buttons.addStretch(1)
        self.layout_buttons.addWidget(self.button_exit, Qt.AlignCenter)
        self.layout_buttons.addStretch(1)

        self.button_exit.setFixedSize(120, 35)

        self.button_exit.setShortcut("Ctrl+X")


    def _select_file(self):

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            "Select a file",
            "./conf/",
            "Text files (*.txt);;All files (*)"
        )

        if filename:

            print(f"Selected file: {filename}")

            self.file_list.setText(filename)


    def generate_frames_quaternion_rotation(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        thread_current = QThread.currentThread()
        print(nameMethod + " : Current thread = " + str(thread_current))
        print(nameMethod + " : Current thread = " + thread_current.objectName())

        # self.panel_frame_terminal.panel_terminal.terminal.sendText("echo \"In method : MainWindow::generate_frames_quaternion_rotation\"")

        # Create a worker thread for this task and then start it running.

        self.worker_thread = Workers.Worker_GenerateFrames_QuaternionRotation.Worker_GenerateFrames_QuaternionRotation()
        self.worker_thread.start()

        print(nameMethod + " : Exit")


    def _update_logging_level(self, level_logging):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        logger = logging.getLogger()

        logger.setLevel(level_logging)
        level_logging = logger.getEffectiveLevel()

        print(nameMethod + " : Current logging level = " + str(level_logging))

        print(nameMethod + " : Exit")


    def _debug_combobox_changed(self, index):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : Index = " + str(index))

        # 0 = DEBUG
        # 1 = INFO
        # 2 = WARNING
        # 3 = ERROR
        # 4 = CRITICAL
        # 5 = NOTSET

        if index == 0:

            print(nameMethod + " : Index = " + str(index) + " = DEBUG")
            level_logging = logging.DEBUG

        elif index == 1:

            print(nameMethod + " : Index = " + str(index) + " = INFO")
            level_logging = logging.INFO

        elif index == 2:

            print(nameMethod + " : Index = " + str(index) + " = WARNING")
            level_logging = logging.WARNING

        elif index == 3:

            print(nameMethod + " : Index = " + str(index) + " = ERROR")
            level_logging = logging.ERROR

        elif index == 4:

            print(nameMethod + " : Index = " + str(index) + " = CRITICAL")
            level_logging = logging.CRITICAL

        elif index == 5:

            print(nameMethod + " : Index = " + str(index) + " = NOTSET")
            level_logging = logging.NOTSET

        else:

            raise Exception("Invalid QComboBox index : " + str(index))

        self._update_logging_level(level_logging)

        print(nameMethod + " : Exit")


    def _connect_signals_to_slots(self):

        self.button_file_select.clicked.connect(self._select_file)
        # self.button_apply.clicked.connect(self._apply_settings)
        # self.button_file_run_script.clicked.connect(Config.ObjectDirectory.object_directory.main_window.generate_frames_quaternion_rotation)
        self.button_file_run_script.clicked.connect(self.generate_frames_quaternion_rotation)
        self.button_exit.clicked.connect(self.close)

        self.debug_combobox.currentIndexChanged.connect(self._debug_combobox_changed)
