import json

from   PySide6.QtCore \
import (Qt, Slot)

from   PySide6.QtWidgets \
import (
        QWidget,
        QGroupBox,
        QHBoxLayout,
        QVBoxLayout,
        QLineEdit,
        QPushButton
       )


class PanelData_Slide(QWidget):

    @Slot(str)
    def update_panel(self, filename):

        plot_frame  = False
        slide_frame = False

        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print("filename = ", filename)
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

        self.filename.setText(filename)


    def __init__(self, parent=None):

        super().__init__(parent)

        self._create_gui_components()
        self._configure_gui_components()


    def _create_gui_components(self):

        self.layout = QVBoxLayout()


        self.group_box_plot_data      = QGroupBox("Plot data blank : ")
        self.layout_plot_data         = QVBoxLayout()

        self.group_box_filename = QGroupBox("Slide filename : ")
        self.layout_filename    = QHBoxLayout()

        self.filename           = QLineEdit()


    def _configure_gui_components(self):

        # Set the layout for this widget.

        self.setLayout(self.layout)

        self.layout.addWidget(self.group_box_plot_data)

        self.group_box_plot_data.setLayout(self.layout_plot_data)

        # self.layout_plot_data.addWidget(self.group_box_filename)
        self.layout_plot_data.addWidget(self.group_box_filename)
        self.layout_plot_data.addStretch()

        self.group_box_filename.setLayout(self.layout_filename)
        self.layout_filename.addWidget(self.filename)
