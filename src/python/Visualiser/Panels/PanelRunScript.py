from   PySide6.QtCore \
import (
       Qt,
       Slot
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
       QPushButton,
       QFileDialog
       )

import Config.ServiceObjects


class PanelRunScript(QWidget):

    def __init__(self, parent=None):

        super().__init__(None)

        self._create_gui_components()
        self._configure_gui_components()

        self.setWindowTitle("Run script panel")
        self.resize(600, 500)

        self._connect_signals_to_slots()


    def _create_gui_components(self):

        self.layout_top          = QVBoxLayout(self)

        self.group_box           = QGroupBox("Script")
        self.layout_group_box    = QVBoxLayout()

        self.label_file_list     = QLabel("File list")
        self.layout_file_list    = QHBoxLayout()
        self.file_list           = QLineEdit()
        self.button_file_select  = QPushButton("Select")

        self.layout_buttons      = QHBoxLayout()
        self.button_exit         = QPushButton("Exit")


    def _configure_gui_components(self):

        self.setLayout(self.layout_top)

        self.layout_top.addWidget(self.group_box)

        self.group_box.setLayout(self.layout_group_box)

        self.layout_group_box.addWidget(self.label_file_list)
        self.layout_group_box.addLayout(self.layout_file_list)

        self.layout_file_list.addWidget(self.file_list)
        self.layout_file_list.addWidget(self.button_file_select)
        self.button_file_select.setFixedSize(120, 35)

        self.layout_group_box.addStretch(1)

        self.layout_top.addLayout(self.layout_buttons)

        self.layout_buttons.addStretch(1)
        # self.layout_buttons.addStretch(1)
        self.layout_buttons.addWidget(self.button_exit,  Qt.AlignCenter)
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


    def _connect_signals_to_slots(self):

        self.button_file_select.clicked.connect(self._select_file)
        # self.button_apply.clicked.connect(self._apply_settings)
        self.button_exit.clicked.connect(self.close)
