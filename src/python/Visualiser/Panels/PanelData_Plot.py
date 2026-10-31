import json

from   PySide6.QtCore \
import (Qt, Slot)

from   PySide6.QtWidgets \
import (
        QWidget,
        QGroupBox,
        QFrame,
        QHBoxLayout,
        QVBoxLayout,
        QGridLayout,
        QFormLayout,
        QLineEdit,
        QLabel,
        QCheckBox
       )

from PIL import Image

import Widgets.ColorBar


class PanelData_Plot(QWidget):

    @Slot(str)
    def update_panel(self, filename):

        nameMetod = "PanelDisplayData_Plot::update_panel (Slot) "

        plot_frame  = False
        slide_frame = False


        print("Method : (Slot) update_panel")
        print(filename)

        # Open the file and retrieve the metadata from it.
        #
        # From this metadata, we should be able to ascertain which panel needs to be displayed.

        image = Image.open(filename)

        print(image.info)

        metadata = image.info

        # >>>>>

        # Check if the specified data resides within JSON metadata.

        if "com.example.simulation" not in metadata:

            # Maybe filename contains a slide frame.

            print("No animation metadata was found in the file.")

            slide_frame = True

        else:

            # Maybe filename contains a plot frame.

            try:

                self.metadata_json = json.loads(metadata["com.example.simulation"])

                plot_frame = True

            except (json.JSONDecodeError, TypeError) as e:

                print(f"Invalid simulation metadata: {e}")

        if plot_frame:

            azimuth        = self.metadata_json["view"]["azimuth"]
            elevation      = self.metadata_json["view"]["elevation"]
            angle_rotation = self.metadata_json["rotation"]["angle"]

            self.azimuth.setText(str(azimuth))
            self.elevation.setText(str(elevation))
            self.angle_rotation.setText(str(angle_rotation))

            self.update_quaternion_pre_multiply()
            self.update_quaternion_rotated()

            print(azimuth)

        else:

            self.angle_rotation.setText("*** Slide frame ***")


    def update_quaternion_pre_multiply(self):

        quaternion_pre_multiply_scalar = self.metadata_json["quaternion_pre_multiply"]["scalar"]
        quaternion_pre_multiply_x      = self.metadata_json["quaternion_pre_multiply"]["x"]
        quaternion_pre_multiply_y      = self.metadata_json["quaternion_pre_multiply"]["y"]
        quaternion_pre_multiply_z      = self.metadata_json["quaternion_pre_multiply"]["z"]

        update_field = False

        if quaternion_pre_multiply_scalar > self.pre_w_max:

            self.pre_w_max = quaternion_pre_multiply_scalar
            update_field = True

        if quaternion_pre_multiply_scalar < self.pre_w_min:

            self.pre_w_min = quaternion_pre_multiply_scalar
            update_field = True

        if update_field:

            print("***** Updating min/max *****")

            # min_max_string = f"{(float(self.pre_w_min)):0.4f) || (float(self.pre_w_max)):0.4f)}"
            min_max_string = f"{float(self.pre_w_min):0.3f} <> {float(self.pre_w_max):0.3f}"

            print(min_max_string)

            self.pre_w_min_max.setText(min_max_string)

        if quaternion_pre_multiply_scalar >= 0:

            self.pre_w.setText("+" + str(quaternion_pre_multiply_scalar))

        else:

            self.pre_w.setText(str(quaternion_pre_multiply_scalar))

        if quaternion_pre_multiply_x >= 0:

            self.pre_x.setText("+" + str(quaternion_pre_multiply_x))

        else:

            self.pre_x.setText(str(quaternion_pre_multiply_x))

        if quaternion_pre_multiply_y >= 0:

            self.pre_y.setText("+" + str(quaternion_pre_multiply_y))

        else:

            self.pre_y.setText(str(quaternion_pre_multiply_y))

        if quaternion_pre_multiply_z >= 0:

            self.pre_z.setText("+" + str(quaternion_pre_multiply_z))

        else:

            self.pre_z.setText(str(quaternion_pre_multiply_z))

        self.colorbar_pre_w.set_value(quaternion_pre_multiply_scalar)
        self.colorbar_pre_x.set_value(quaternion_pre_multiply_x)
        self.colorbar_pre_y.set_value(quaternion_pre_multiply_y)
        self.colorbar_pre_z.set_value(quaternion_pre_multiply_z)

        if ((not self.pre_min.text()) or (quaternion_pre_multiply_scalar < float(self.pre_min.text()))):

            self.pre_min.setText(str(quaternion_pre_multiply_scalar))

        if ((not self.pre_max.text()) or (quaternion_pre_multiply_scalar > float(self.pre_max.text()))):

            self.pre_max.setText(str(quaternion_pre_multiply_scalar))

        # Pre : w / scalar

        if quaternion_pre_multiply_scalar < 0:

            # line_edit.setStyleSheet("QLineEdit { color: white; }")

            self.pre_w.setStyleSheet("color: red;")
            # self.checkbox_pre_w.setStyleSheet("background-color: red;")

        elif quaternion_pre_multiply_scalar > 0:

            self.pre_w.setStyleSheet("color: lightgreen;")
            # self.checkbox_pre_w.setStyleSheet("background-color: green;")

        else :

            self.pre_w.setStyleSheet("")
            # self.checkbox_pre_w.setStyleSheet("")

        # Pre : x

        if quaternion_pre_multiply_x < 0:

            self.pre_x.setStyleSheet("color: red;")
            # self.checkbox_pre_x.setStyleSheet("background-color: red;")

        elif quaternion_pre_multiply_x > 0:

            self.pre_x.setStyleSheet("color: lightgreen;")
            # self.checkbox_pre_x.setStyleSheet("background-color: green;")

        else :

            self.pre_x.setStyleSheet("")
            # self.checkbox_pre_x.setStyleSheet("")

        # Pre : y

        if quaternion_pre_multiply_y < 0:

            self.pre_y.setStyleSheet("color: red;")
            # self.checkbox_pre_y.setStyleSheet("background-color: red;")

        elif quaternion_pre_multiply_y > 0:

            self.pre_y.setStyleSheet("color: lightgreen;")
            # self.checkbox_pre_y.setStyleSheet("background-color: green;")

        else :

            self.pre_y.setStyleSheet("")
            # self.checkbox_pre_y.setStyleSheet("")

        # Pre : z

        if quaternion_pre_multiply_z < 0:

            self.pre_z.setStyleSheet("color: red;")
            # self.checkbox_pre_z.setStyleSheet("background-color: red;")

        elif quaternion_pre_multiply_z > 0:

            self.pre_z.setStyleSheet("color: lightgreen;")
            # self.checkbox_pre_z.setStyleSheet("background-color: green;")

        else :

            self.pre_z.setStyleSheet("")
            # self.checkbox_pre_z.setStyleSheet("")

        # Pre : max

        if float(self.pre_max.text()) < 0:

            self.checkbox_pre_max.setStyleSheet("background-color: red;")

        elif float(self.pre_max.text()) > 0:

            self.checkbox_pre_max.setStyleSheet("background-color: green;")

        else :

            self.checkbox_pre_max.setStyleSheet("")

        # Pre : min

        if float(self.pre_min.text()) < 0:

            self.checkbox_pre_min.setStyleSheet("background-color: red;")

        elif float(self.pre_min.text()) > 0:

            self.checkbox_pre_min.setStyleSheet("background-color: green;")

        else :

            self.checkbox_pre_min.setStyleSheet("")


    def update_quaternion_rotated(self):

        quaternion_rotated_scalar = self.metadata_json["quaternion_rotated"]["scalar"]
        quaternion_rotated_x      = self.metadata_json["quaternion_rotated"]["x"]
        quaternion_rotated_y      = self.metadata_json["quaternion_rotated"]["y"]
        quaternion_rotated_z      = self.metadata_json["quaternion_rotated"]["z"]

        self.rotated_w.setText(str(quaternion_rotated_scalar))
        self.rotated_x.setText(str(quaternion_rotated_x))
        self.rotated_y.setText(str(quaternion_rotated_y))
        self.rotated_z.setText(str(quaternion_rotated_z))

        if quaternion_rotated_scalar < 0:

            self.checkbox_rotated_w.setStyleSheet("background-color: red;")

        elif quaternion_rotated_scalar > 0:

            self.checkbox_rotated_w.setStyleSheet("background-color: green;")

        else :

            self.checkbox_rotated_w.setStyleSheet("")

        if quaternion_rotated_x < 0:

            self.checkbox_rotated_x.setStyleSheet("background-color: red;")

        elif quaternion_rotated_x > 0:

            self.checkbox_rotated_x.setStyleSheet("background-color: green;")

        else :

            self.checkbox_rotated_x.setStyleSheet("")

        if quaternion_rotated_y < 0:

            self.checkbox_rotated_y.setStyleSheet("background-color: red;")

        elif quaternion_rotated_y > 0:

            self.checkbox_rotated_y.setStyleSheet("background-color: green;")

        else :

            self.checkbox_rotated_y.setStyleSheet("")

        if quaternion_rotated_z < 0:

            self.checkbox_rotated_z.setStyleSheet("background-color: red;")

        elif quaternion_rotated_z > 0:

            self.checkbox_rotated_z.setStyleSheet("background-color: green;")

        else :

            self.checkbox_rotated_z.setStyleSheet("")


    def __init__(self, parent=None):

        super().__init__(parent)

        self._create_data_components()

        self._create_gui_components()

        self._configure_gui_components()

        # self.showMaximized()


    def _create_data_components(self):

        self.pre_w_min = 0
        self.pre_w_max = 0

        self.pre_x_min = 0
        self.pre_x_max = 0

        self.pre_y_min = 0
        self.pre_y_max = 0

        self.pre_z_min = 0
        self.pre_z_max = 0


    def _create_gui_components(self):

        self.layout = QVBoxLayout()

        self.group_box_plot_data = QGroupBox("Plot data : ")

        self.layout_plot_data = QVBoxLayout()

        self._create_gui_components_angle_rotation()
        self._create_gui_components_multiplication_pre()
        self.__create_gui_components_multiplication_full()
        self.__create_gui_components_viewing_angle()


    def _create_gui_components_angle_rotation(self):

        self.group_box_angle_rotation = QGroupBox("Angle of rotation : ")
        self.layout_angle_rotation    = QHBoxLayout()

        self.angle_rotation           = QLineEdit()


    def _create_gui_components_multiplication_pre(self):

        self.group_box_pre = QGroupBox("Quaternion (qv) : ")
        self._grid_pre      = QGridLayout()

        self.pre_w         = QLineEdit("0")
        self.pre_x         = QLineEdit("0")
        self.pre_y         = QLineEdit("0")
        self.pre_z         = QLineEdit("0")

        self.pre_w_min_max = QLineEdit("")
        self.pre_x_min_max = QLineEdit("")
        self.pre_y_min_max = QLineEdit("")
        self.pre_z_min_max = QLineEdit("")

        self.pre_min       = QLineEdit("0")
        self.pre_max       = QLineEdit("0")

        self.colorbar_pre_w = Widgets.ColorBar.ColorBarWidget()
        self.colorbar_pre_x = Widgets.ColorBar.ColorBarWidget()
        self.colorbar_pre_y = Widgets.ColorBar.ColorBarWidget()
        self.colorbar_pre_z = Widgets.ColorBar.ColorBarWidget()

        self.checkbox_pre_w   = QCheckBox()
        self.checkbox_pre_x   = QCheckBox()
        self.checkbox_pre_y   = QCheckBox()
        self.checkbox_pre_z   = QCheckBox()
        self.checkbox_pre_max = QCheckBox()
        self.checkbox_pre_min = QCheckBox()

        self.checkbox_rotated_w = QCheckBox()
        self.checkbox_rotated_x = QCheckBox()
        self.checkbox_rotated_y = QCheckBox()
        self.checkbox_rotated_z = QCheckBox()


    def __create_gui_components_multiplication_full(self):

        self.group_box_rotated = QGroupBox("Quaternion (qvq') : ")
        self._grid_rotated      = QGridLayout()

        self.rotated_w         = QLineEdit()
        self.rotated_x         = QLineEdit()
        self.rotated_y         = QLineEdit()
        self.rotated_z         = QLineEdit()


    def __create_gui_components_viewing_angle(self):

        self.group_box_viewing_angle = QGroupBox("Viewing angle : ")
        self.form_viewing_angle      = QFormLayout()

        self.azimuth_initial         = QLineEdit()
        self.azimuth                 = QLineEdit()
        self.azimuth_delta           = QLineEdit()

        self.separator_widget        = QWidget()
        self.separator_layout        = QVBoxLayout(self.separator_widget)
        self.separator_horizontal    = QFrame()

        self.elevation_initial       = QLineEdit()
        self.elevation               = QLineEdit()
        self.elevation_delta         = QLineEdit()


    def _configure_gui_components(self):

        # Set the layout for this widget.

        self.setLayout(self.layout)

        self.layout.addWidget(self.group_box_plot_data)

        self.group_box_plot_data.setLayout(self.layout_plot_data)

        self.layout_plot_data.addWidget(self.group_box_angle_rotation)
        self.layout_plot_data.addWidget(self.group_box_pre)
        self.layout_plot_data.addWidget(self.group_box_rotated)
        self.layout_plot_data.addWidget(self.group_box_viewing_angle)
        self.layout_plot_data.addStretch()


        self.__configure_gui_components_angle_rotation()
        self.__configure_gui_components_multiplication_pre()
        self.__configure_gui_components_multiplication_full()
        self.__configure_gui_components_viewing_angle()


    def __configure_gui_components_angle_rotation(self):

        self.group_box_angle_rotation.setLayout(self.layout_angle_rotation)

        self.layout_angle_rotation.addWidget(self.angle_rotation)

        self.angle_rotation.setReadOnly(True)
        self.angle_rotation.setAlignment(Qt.Alignment.AlignRight)


    def __configure_gui_components_multiplication_pre(self):

        self.group_box_pre.setLayout(self._grid_pre)

        self.pre_w.setReadOnly(True)
        self.pre_x.setReadOnly(True)
        self.pre_y.setReadOnly(True)
        self.pre_z.setReadOnly(True)

        self.pre_w_min_max.setReadOnly(True)
        self.pre_x_min_max.setReadOnly(True)
        self.pre_y_min_max.setReadOnly(True)
        self.pre_z_min_max.setReadOnly(True)

        self.pre_w_min_max.setAlignment(Qt.Alignment.AlignRight)
        self.pre_x_min_max.setAlignment(Qt.Alignment.AlignRight)
        self.pre_y_min_max.setAlignment(Qt.Alignment.AlignRight)
        self.pre_z_min_max.setAlignment(Qt.Alignment.AlignRight)

        self.pre_min.setReadOnly(True)
        self.pre_max.setReadOnly(True)


    def __configure_gui_components_multiplication_full(self):

        self.group_box_rotated.setLayout(self._grid_rotated)

        self.rotated_w.setReadOnly(True)
        self.rotated_x.setReadOnly(True)
        self.rotated_y.setReadOnly(True)
        self.rotated_z.setReadOnly(True)


    def __configure_gui_components_viewing_angle(self):

        self.group_box_viewing_angle.setLayout(self.form_viewing_angle)

        self.separator_layout.setContentsMargins(0, 10, 0, 10)
        self.separator_layout.setSpacing(0)

        self.separator_layout.addWidget(self.separator_horizontal)

        self.separator_horizontal.setFrameShape(QFrame.Shape.HLine)
        self.separator_horizontal.setFrameShadow(QFrame.Shadow.Sunken)

        self.azimuth_initial.setReadOnly(True)
        self.azimuth.setReadOnly(True)
        self.azimuth_delta.setReadOnly(True)

        self.elevation_initial.setReadOnly(True)
        self.elevation.setReadOnly(True)
        self.elevation_delta.setReadOnly(True)

        # Put the form layout within a frame

        # self.checkbox_pre_w.setEnabled(False)
        # self.checkbox_pre_x.setEnabled(False)
        # self.checkbox_pre_y.setEnabled(False)
        # self.checkbox_pre_z.setEnabled(False)

        # w / scalar

        self._grid_pre.addWidget(QLabel("w  :  "),            0, 0)
        self._grid_pre.addWidget(self.pre_w_min_max,          0, 1)
        self._grid_pre.addWidget(self.pre_w,                  1, 0)
        # self._grid_pre.addWidget(self.checkbox_pre_w,         0, 2)

        self._grid_pre.addWidget(self.colorbar_pre_w,         1, 1)
        self.colorbar_pre_w.set_value(float(self.pre_w.text()))

        # x

        self._grid_pre.addWidget(QLabel("ib  :  "),            2, 0)
        self._grid_pre.addWidget(self.pre_x,                  3, 0)
        # self._grid_pre.addWidget(self.checkbox_pre_x,         2, 2)

        self._grid_pre.addWidget(self.colorbar_pre_x,         3, 1)
        self.colorbar_pre_x.set_value(float(self.pre_x.text()))

        # y

        self._grid_pre.addWidget(QLabel("jc  :  "),            4, 0)
        self._grid_pre.addWidget(self.pre_y,                  5, 0)
        # self._grid_pre.addWidget(self.checkbox_pre_y,         4, 2)

        self._grid_pre.addWidget(self.colorbar_pre_y,         5, 1)
        self.colorbar_pre_y.set_value(float(self.pre_y.text()))

        # z

        self._grid_pre.addWidget(QLabel("kd  :  "),            6, 0)
        self._grid_pre.addWidget(self.pre_z,                  7, 0)
        # self._grid_pre.addWidget(self.checkbox_pre_z,         6, 2)

        self._grid_pre.addWidget(self.colorbar_pre_z,         7, 1)
        self.colorbar_pre_z.set_value(float(self.pre_z.text()))

        # self._grid_pre.addWidget(QLabel("Max  :  "),          8, 0)
        # self._grid_pre.addWidget(self.pre_max,                8, 1)
        # self._grid_pre.addWidget(self.checkbox_pre_max,       8, 2)

        # self._grid_pre.addWidget(QLabel("Min  :  "),          9, 0)
        # self._grid_pre.addWidget(self.pre_min,                9, 1)
        # self._grid_pre.addWidget(self.checkbox_pre_min,       9, 2)

        self._grid_rotated.addWidget(QLabel("w  :  "),        0, 0)
        self._grid_rotated.addWidget(self.rotated_w,          0, 1)
        # self._grid_rotated.addWidget(self.checkbox_rotated_w, 0, 2)

        self._grid_rotated.addWidget(QLabel("x  :  "),        1, 0)
        self._grid_rotated.addWidget(self.rotated_x,          1, 1)
        # self._grid_rotated.addWidget(self.checkbox_rotated_x, 1, 2)

        self._grid_rotated.addWidget(QLabel("y  :  "),        2, 0)
        self._grid_rotated.addWidget(self.rotated_y,          2, 1)
        # self._grid_rotated.addWidget(self.checkbox_rotated_y, 2, 2)

        self._grid_rotated.addWidget(QLabel("z  :  "),        3, 0)
        self._grid_rotated.addWidget(self.rotated_z,          3, 1)
        # self._grid_rotated.addWidget(self.checkbox_rotated_z, 3, 2)


        self.form_viewing_angle.addRow(
            "Azimuth  :  ",
            self.azimuth
        )

        self.form_viewing_angle.addRow(
            "Azimuth initial  :  ",
            self.azimuth_initial
        )

        self.form_viewing_angle.addRow(
            "Azimuth delta  :  ",
            self.azimuth_delta
        )

        self.form_viewing_angle.addRow(self.separator_widget)

        self.form_viewing_angle.addRow(
            "Elevation  :  ",
            self.elevation
        )

        self.form_viewing_angle.addRow(
            "Elevation initial  :  ",
            self.elevation_initial
        )

        self.form_viewing_angle.addRow(
            "Elevation delta  :  ",
            self.elevation_delta
        )
