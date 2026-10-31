import sys
import numpy as np
# from matplotlib.patches import Polygon

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


class ColorBarWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        # Taller figure to fit the bar and arrow

        self.figure = Figure(figsize=(2.0, 0.15), dpi=100)
        self.figure.patch.set_visible(False)

        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setStyleSheet("background: transparent;")
        self.canvas.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.canvas)

        # Gradient
        # gradient = np.linspace(0, 1, 512).reshape(1, -1)
        gradient = np.linspace(1, 0, 512).reshape(1, -1)

        ax = self.figure.add_axes([0, 0, 1, 1])
        ax.imshow(
            gradient,
            aspect="auto",
            cmap="turbo",
            interpolation="nearest",
            extent=[0, 1, 0.85, 1]
        )

        # Reserve space below the bar for the arrow

        # Colourbar occupies y = 0.55 to 1.0
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        self.current_value = 0.25
        x = (self.current_value + 1.0) / 2.0

        # Upward-pointing triangle marker
        (self.arrow,) = ax.plot(
            x, 0.48,
            marker="|",
            markersize=10,
            color="lightgray",
            markeredgewidth=1,
            clip_on=False
        )
        # ax.add_patch(self.arrow)

        ax.set_axis_off()
        self.canvas.draw()

        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(20)

    def set_value_old(self, value):

        # Clamp value to the range [-1, 1]
        value = max(-1.0, min(1.0, value))
        self.current_value = value
        x = (value + 1.0) / 2.0

        self.arrow.set_xy([
            (x, 0.0),
            (x - 0.035, -0.5),
            (x + 0.035, -0.5),
        ])

        self.canvas.draw_idle()


    def set_value(self, value):

        value = max(-1.0, min(1.0, value))
        self.current_value = value

        x = (value + 1.0) / 2.0

        # Keep the marker fully inside the horizontal bounds

        margin = 0.02
        x = max(margin, min(1.0 - margin, x))

        # Update the marker position

        self.arrow.set_data([x], [0.48])

        self.canvas.draw_idle()
