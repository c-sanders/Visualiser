from   PySide6.QtCore \
import (
        Qt,
        Slot
       )
from   PySide6.QtWidgets \
import (
        QFrame,
        QVBoxLayout,
        QFormLayout,
        QLabel
       )
from   PySide6.QtGui \
import (
        QPixmap
       )

from Panels.PanelFrame    import PanelFrame
from Panels.PanelTerminal import PanelTerminal


class PanelFrameTerminal(QFrame):

    # Invoked by : MainWindow::_configure_for_plot

    @Slot(str)
    def update_panel(self, filename):

        nameMethod = "PanelDisplayTerminal::update_panel"

        plot_frame  = False
        slide_frame = False


        print(nameMethod + " : Enter")

        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print("filename = ", filename)
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

        self.panel_frame.update_panel(filename)

        print(nameMethod + " : Exit")


    def __init__(self, parent=None):

        super().__init__(parent)

        self.__create_gui_components()
        self.__configure_gui_components()


    def __create_gui_components(self):

        self.layout_top            = QVBoxLayout(self)

        # self.frame_buttons         = QFrame()
        # self.layout_buttons        = QHBoxLayout(self.frame_buttons)

        # self.form                  = QFormLayout()

        self.panel_frame           = PanelFrame()
        self.panel_terminal        = PanelTerminal()
        # self.image                 = QPixmap("my_image.png")

    def __configure_gui_components(self):

        # self.__configure_terminal()

        self.setLayout(self.layout_top)

        self.layout_top.addWidget(self.panel_frame,  stretch=4)
        self.layout_top.addWidget(self.panel_terminal, stretch=1)

        # self.panel_frame.setPixmap(
        #     self.image.scaled(
        #         900,
        #         787,
        #         aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
        #         mode=Qt.TransformationMode.SmoothTransformation,
        #     )
        # )

        # self.layout_top_right_local.addWidget(label_image)
        # self.layout_top_right_local.addWidget(self.terminal_frame)
