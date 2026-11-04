from   PySide6.QtCore \
import (
        Qt,
        QSize,
        Slot
       )
from PySide6.QtWidgets \
import (
        QFrame,
        QHBoxLayout,
        QLabel,
        QSizePolicy
       )
from   PySide6.QtGui \
import (
        QPixmap
       )


class PanelFrame(QFrame):

    @Slot(str)
    def update_panel(self, filename):

        nameMethod = "PanelFrame::update_panel"


        print(nameMethod + " : Enter")

        print(nameMethod + " : filename = " + str(filename))

        self.load_image_into_panel(filename)

        print(nameMethod + " : Exit")


    def __init__(self, parent=None):

        super().__init__(parent)

        self.__create_gui_components()
        self.__configure_gui_components()


    def __create_gui_components(self):

        self.layout_top = QHBoxLayout(self)

        self.label  = QLabel()


    def __configure_gui_components(self):

        self.setLayout(self.layout_top)

        self.layout_top.addWidget(self.label, stretch=1)

        self.label.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Ignored
        )
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_image_into_panel("./images/my_image.png")


    def load_image_into_panel(self, filename_image):

        image                = QPixmap(filename_image)
        self.original_pixmap = image


        if image.isNull():

            raise Exception("Image is null")

        print("Image is not null")

        print("image = " + str(image))

        print("(width, height) = (" + str(image.width()) + ", " + str(image.height()) + ")")

        print(">>>>>>>>>>")
        print(">>>>>>>>>>")
        print(self.label.size())
        print("<<<<<<<<<<")
        print("<<<<<<<<<<")

        self.label.setPixmap(
            image.scaled(
                self.label.size(),
                # QSize(1480, 730),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        # self.label.setPixmap(
        # self.original_pixmap.scaled(
        #   self.label.contentsRect().size(),
        #   Qt.AspectRatioMode.KeepAspectRatio,
        #   Qt.TransformationMode.SmoothTransformation,
        # )
        # )

        print("Displayed image:", self.label.pixmap().size())


    def resizeEvent(self, event):

        super().resizeEvent(event)

        if not self.original_pixmap.isNull():

            self.label.setPixmap(
                self.original_pixmap.scaled(
                    self.label.contentsRect().size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )