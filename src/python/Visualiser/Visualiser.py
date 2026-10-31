import   sys
from     pathlib import Path
from     PySide6.QtCore \
  import (
          QTimer
         )
from     PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

import   Panels.MainWindow


# --------------------------------------------------
# Run the application
# --------------------------------------------------

app = QApplication(sys.argv)

if False:

    app.setStyle("Fusion")

    stylesheet_path = Path(__file__).with_name("classic.qss")

    print("Stylesheet = " + str(stylesheet_path))

    app.setStyleSheet(
       str(stylesheet_path.read_text(encoding="utf-8"))
    )

# Create a main window object, display it, and then start it running.

window = Panels.MainWindow.MainWindow()
window.showMaximized()

window.startWorkerThread()

window.startup()

return_code = app.exec()

# The GUI has finished executing. Run through the program exit procedure.

print(
    "About to exit with a return code of "
    + str(return_code)
)

sys.exit(return_code)