import   sys
from     pathlib import Path
from     PySide6.QtCore \
  import (
          QTimer
         )
from     PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

from     PanelPlotData     import PanelPlotData
from     PanelTerminal     import PanelTerminal
from     PanelPlotTerminal import PanelPlotTerminal
from     Quaternion_rotation_visualiser import Quaternion_rotation_visualiser


# --------------------------------------------------
# Run the application
# --------------------------------------------------

app = QApplication(sys.argv)

app.setStyle("Fusion")

stylesheet_path = Path(__file__).with_name("classic.qss")

print("Stylesheet = " + str(stylesheet_path))

app.setStyleSheet(
   str(stylesheet_path.read_text(encoding="utf-8"))
)

window = QWidget()


layout         = QVBoxLayout(window)
button_exit    = QPushButton("Exit")
button_exit.setFixedSize(120, 30)
button_exit.setShortcut("Ctrl+Q")
button_exit.clicked.connect(app.quit)
panel_terminal = PanelPlotTerminal(window)
layout.addWidget(panel_terminal)
layout.addWidget(button_exit)

window.showMaximized()
window.show()

return_code = app.exec()

window.save_settings()

print(
    "About to exit with a return code of "
    + str(return_code)
)

sys.exit(return_code)