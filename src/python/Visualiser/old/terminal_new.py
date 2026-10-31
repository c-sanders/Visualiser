import   sys
from     pathlib import Path
from     PySide6.QtCore \
  import (
          QTimer
         )
from     PySide6.QtWidgets import QApplication

from     TerminalWindow import TerminalWindow, MyThread


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

window = TerminalWindow()
window.show()

worker_thread = MyThread()
worker_thread.set_terminal_window(window)

# Wait 2 seconds, then run the command.

worker_thread.start()

return_code = app.exec()

window.save_settings()

print(
    "About to exit with a return code of "
    + str(return_code)
)

sys.exit(return_code)