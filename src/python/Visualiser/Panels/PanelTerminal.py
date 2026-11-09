from   pathlib import Path

from   PySide6.QtWidgets \
import (
        QFrame,
        QVBoxLayout
       )
from   PySide6.QtGui \
import (
        QFont,
       )

from   pyside6_qtermwidget \
import (
        QTermWidget
       )

import Config.ObjectDirectory


class PanelTerminal(QFrame):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.initial_resize_performed = False

        self.__create_gui_components()
        self.__configure_gui_components()


    def __create_gui_components(self):

        # Frame that places padded space around the bordered terminal.

        self.layout_top            = QVBoxLayout(self)

        # Frame that places padding

        # self.frame_outer = QFrame()
        # self.layout_outer = QVBoxLayout(self)

        # Frame that places a thin border around the terminal.

        self.frame_terminal        = QFrame(self)
        self.layout_terminal       = QVBoxLayout(self.frame_terminal)

        self.terminal              = QTermWidget(self.frame_terminal)


    def __configure_gui_components(self):

        # Set the top level layout for this widget and add the necessary child widgets to it.

        self.setLayout(self.layout_top)
        self.layout_top.addWidget(self.frame_terminal)

        self.frame_terminal.setLayout(self.layout_terminal)
        self.layout_terminal.addWidget(self.terminal)

        # Configure the frame around the terminal.

        self.frame_terminal.setObjectName("terminalFrame")
        self.frame_terminal.setStyleSheet("""
            QFrame#terminalFrame {
                border: 1px solid #606060;
                border-radius: 8px;
            }
        """)

        self.layout_terminal.setContentsMargins(5, 5, 5, 5)
        self.layout_terminal.setSpacing(0)

        self.__configure_terminal()


    # --------------------------------------------------
    # Terminal widget
    # --------------------------------------------------

    def __configure_terminal(self):

        scheme_dir = str(Path(__file__).parent) + "/"

        print(scheme_dir)
        print("=====")

        self.terminal.addCustomColorSchemeDir(scheme_dir)

        self.terminal.setHistorySize(1000)
        # self.terminal.setScrollBarPosition \
        # (
        #  QTermWidget.ScrollBarPosition.ScrollBarRight
        # )

        self.terminal.setColorScheme(
            # self.settings_colour_scheme
            Config.ObjectDirectory.object_directory.settings_config.color_scheme
        )

        # font = QFont("Monospace", self.settings_font_size)
        # self.terminal.setTerminalFont(font)

        print("Available colour schemes:")
        print(self.terminal.availableColorSchemes())

        # self.terminal.setEnabled(not self.read_only.isChecked())

        font = QFont("Monospace")
        font.setStyleHint(QFont.StyleHint.Monospace)

        self.terminal.setTerminalFont(font)


    def resizeEvent(self, event):

        super().resizeEvent(event)

        if not self.initial_resize_performed:

            # When the showMaximized method is invoked on this program's main window, it can leave the prompt in the
            # QTermWidget looking a bit garbled. We can work around this by instructing the terminal to run the clear
            # command in order to try and fix this.

            # self.terminal.sendText("clear\n")

            pass