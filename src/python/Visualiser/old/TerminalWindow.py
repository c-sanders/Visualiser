from   pathlib import Path
import time
import json

from   PySide6.QtCore \
import (
        Qt,
        QThread
       )
from   PySide6.QtWidgets \
import (
        QWidget,
        QMainWindow,
        QGroupBox,
        QDockWidget,
        QTextEdit,
        QLabel,
        QFrame,
        QVBoxLayout,
        QHBoxLayout,
        QFormLayout,
        QCheckBox,
        QLineEdit,
        QPushButton,
       )
from  PySide6.QtNetwork import QTcpServer, QHostAddress

from   PySide6.QtGui \
import (
        QPixmap,
        QFont,
        QAction,
        QActionGroup
       )

from PlotDataPanel import PlotDataPanel

from PanelTerminal import PanelTerminal


class MyThread(QThread):

    # def __init__(self):

    #     pass


    def set_terminal_window(self, terminal_window):

        self.terminal_window = terminal_window


    def run(self):

        # Pause for a few seconds (maybe two) and then start running the rotation code in a loop.

        time.sleep(2)

        index = 1

        while index <= 3 :

            print(index)
            time.sleep(1)

            # Invoke the Python script which calls the Haskell code.
            #
            #   - Invoke the Haskell code to calculate the new rotation.
            #   - Invoke the Python code to generate the plot for this new rotation.
            #   - Update the Qt GUI with the new plot and its data.

            # Invoke the Python script which runs the Haskell code.

            self.terminal_window.terminal.sendText("echo \"Have slept for : " + str(index) + " seconds\"\n")
            # self.terminal.sendText("python -m pip list\n")
            index += 1

        # self.terminal_window.run_command_activate_venv()


class TerminalWindow(QMainWindow, QThread):

    def __import_settings(self) :

        self.ip_address          = QHostAddress("127.0.0.1")
        self.tcp_port            = 5000

        self.run_diagnostic_code = True

        self.json_config_file    = "./settings.json"
        self.title_window        = "My custom terminal (Implemented using Python and PySide)"
        self.dimensions_window   = (1024, 768)


    # --------------------------------------------------
    # Initialisation
    # --------------------------------------------------

    def __init__(self):

        super().__init__()

        self.scheme_custom = Path.home() / "local/source_code/python/Quternion_rotation_visuaiser/MyTerminal.colorscheme"

        print(self.scheme_custom)
        print("=====")

        self.__import_settings()

        self.__setup_port_connection()

        self.__configure_window()

        self.__create_gui_components()

        self.__configure_settings()

        self.__configure_gui_components()

        if self.run_diagnostic_code:

            self.__run_diagnostics()


    def __setup_port_connection(self):

        self.server = QTcpServer(self)

        # Listen for incoming connections.

        if not self.server.listen(self.ip_address, self.tcp_port):

            print("Failed to start server:",
                  self.server.errorString())

            return

        print(f"Listening on {self.ip_address.toString()}:{self.tcp_port}")

        # Connect the signal to our handler.
        self.server.newConnection.connect(

            self.handle_new_connection
        )

    # --------------------------------------------------
    # Configure the window
    # --------------------------------------------------

    def __configure_window(self):

        self.setWindowTitle(self.title_window)
        # self.resize(*self.dimensions_window)
        self.showMaximized()


    def handle_new_connection(self):

        while self.server.hasPendingConnections():
            client = self.server.nextPendingConnection()

            print(
                "Client connected:",
                client.peerAddress().toString()
            )

            # Receive data when the client sends something.
            client.readyRead.connect(
                lambda socket=client:
                self.read_data(socket)
            )

            # Detect when the client disconnects.
            client.disconnected.connect(
                lambda socket=client:
                print("Client disconnected")
            )


    def read_data(self, socket):

        data = bytes(socket.readAll())
        print("Received:", data.decode("utf-8", errors="replace"))

        self.message.setText(data.decode("utf-8", errors="replace"))

    # --------------------------------------------------
    # Settings
    # ========
    #
    #   - Read the configuration settings in from the
    #     JSON file.
    # --------------------------------------------------

    def __configure_settings(self):

        self.__read_config_file()

        self.__configure_checkbox_components()

        # Update the related GUI components.

        self.settings_font_size = int(
            self.settings["font_size"].split()[0]
        )
        self.settings_colour_scheme = self.settings["colour_scheme"]


    def __configure_checkbox_components(self):

        # Checkbox :save_settings_on_exit

        if self.settings["save_settings_on_exit"]:

            self.save_settings_on_exit.setChecked(True)

        # Checkbox : read_only

        if self.settings["read_only"]:

            # The terminal should be read only.

            self.read_only.setChecked(True)

        self.read_only.toggled.connect(self.__action_read_only_toggled)

        # self.read_only.toggled.connect(
        #     lambda checked:
        #         self.terminal.setEnabled(not checked)
        # )


    def __action_read_only_toggled(self, checked):

        self.terminal.setEnabled(not checked)


    def __read_config_file(self):

        self.settings_path = Path(self.json_config_file)

        # Get the settings from the file and then display them.

        if self.settings_path.is_file():

            print("settings.json found")

            with self.settings_path.open(
                "r", encoding="utf-8"
            ) as file_handle:

                self.settings = json.load(file_handle)

        else:

            # The JSON config file doesn't seem to exist.

            print("settings.json not found")

            self.settings = {
                "save_settings_on_exit": True,
                "read_only": False,
                "font_size": "16 pt",
                "colour_scheme": "Linux",
            }

        print("settings = ", self.settings)


    def save_settings(self):

        if self.save_settings_on_exit.isChecked() :

            settings = {
                "save_settings_on_exit": self.save_settings_on_exit.isChecked(),
                "read_only": self.read_only.isChecked(),
                "font_size": self.font_size.text(),
                "colour_scheme": self.colour_scheme.text(),
            }

            with self.settings_path.open(
                "w", encoding="utf-8"
            ) as file_handle:

                json.dump(settings, file_handle, indent=4)

            print("Settings saved.")


    def __create_gui_components(self):

        # self.dock                  = QDockWidget("<<< Dockable panel >>>", self)
        # self.panel_dockable        = PlotDataPanel.PlotDataPanel()

        self.frame_top_level     = QFrame()
        self.layout_top_level    = QHBoxLayout(self.frame_top_level)

        self.panel_plot_data     = PlotDataPanel(self)
        self.panel_plot_terminal = PanelPlotTerminal(self)

        self.layout_top_level.addWidget(self.panel_plot_data)
        self.layout_top_level.addWidget(self.panel_plot_terminal)


    def __create_buttons_checkboxes_lineedits(self):

        self.button_exit           = QPushButton("Exit")

        # Checkboxes and line edits.

        self.read_only             = QCheckBox()
        self.save_settings_on_exit = QCheckBox()
        self.font_size             = QLineEdit()
        self.colour_scheme         = QLineEdit()
        self.message               = QLineEdit()


    def __run_diagnostics(self):

        print("??????????")
        print(hasattr(QTermWidget, "addCustomColorSchemeDir"))
        print("??????????")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print([name for name in dir(self.terminal)
               if "scroll" in name.lower()])
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        print(self.terminal.scroll.__module__)
        print(self.terminal.scrollToEnd.__module__)

        print([
               name for name in dir(self.terminal)
               if any(term in name.lower()
                   for term in ("scroll", "bar", "history", "line"))
               ]
        )

        print("History lines:", self.terminal.historyLinesCount())
        print("History size:", self.terminal.historySize())
        print("Visible lines:", self.terminal.screenLinesCount())

        print(type(self.terminal))
        print(type(self.terminal).__module__)
        print(type(self.terminal).__mro__)


    def run_thread(self):

        self.thread = MyThread()
        self.thread.start()


    def run_command_activate_venv(self):

        # Run this method in its own thread.

        self.terminal.sendText("source /home/craig/.venvs/.venv/bin/activate\n")
        self.terminal.sendText("python -m pip list\n")


    # --------------------------------------------------
    # Central widget and layouts
    # --------------------------------------------------

    def __configure_gui_components(self):

        # self.dock.setWidget(self.panel_dockable)
        # self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

        self.create_menu_bar()

        self.frame_top_level.setLayout(self.layout_top_level)

        self.configure_settings_panel()

        self.setCentralWidget(self.frame_top_level)


    def configure_settings_panel(self):

        # Settings display

        self.colour_scheme.setText(self.settings_colour_scheme)
        self.colour_scheme.setReadOnly(True)

        self.font_size.setText(
            f"{self.settings_font_size} pt"
        )

        self.font_size.setReadOnly(True)

        # Form layout

        self.form.addRow(
            "Save settings on exit  :  ",
            self.save_settings_on_exit
        )

        self.form.addRow(
            "Make terminal read only  :  ",
            self.read_only,
        )

        self.form.addRow(
            "Terminal colour scheme  :  ",
            self.colour_scheme,
        )

        self.form.addRow(
            "Terminal font size  :  ",
            self.font_size,
        )

        self.form.addRow(
            "Message  :  ",
            self.message,
        )

        # Exit button

        self.button_exit.setToolTip(
            "Exit the terminal - Ctrl + Q"
        )
        self.button_exit.setFixedSize(120, 30)
        self.button_exit.clicked.connect(self.close)

        self.frame_buttons.setObjectName("frameButtons")

        self.layout_buttons.addWidget(self.button_exit)


    # --------------------------------------------------
    # Menu bar
    # --------------------------------------------------

    def create_menu_bar(self):

        menubar = self.menuBar()

        menubar.setStyleSheet("""
            QMenuBar {
                border-bottom: -10px solid #606060;
                padding-bottom: 10px;
            }
        """)

        # File menu

        file_menu = menubar.addMenu("&File")

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        # View menu

        view_menu = menubar.addMenu("&View")

        self.create_font_menu(view_menu)
        self.create_colour_menu(view_menu)

    # --------------------------------------------------
    # Font-size menu
    # --------------------------------------------------

    def create_font_menu(self, view_menu):

        font_menu = view_menu.addMenu("&Font Size")

        self.font_group = QActionGroup(self)
        self.font_group.setExclusive(True)

        font_sizes = [10, 12, 14, 16, 18, 20, 24]

        for size in font_sizes:

            action = QAction(f"{size} pt", self)
            action.setCheckable(True)
            action.setChecked(
                size == self.settings_font_size
            )

            self.font_group.addAction(action)
            font_menu.addAction(action)

            action.triggered.connect(
                lambda checked=False, size=size:
                    self.change_font_size(size)
            )

    def change_font_size(self, size):

        font = QFont("Monospace", size)

        self.terminal.setTerminalFont(font)
        self.font_size.setText(f"{size} pt")

    # --------------------------------------------------
    # Colour-scheme menu
    # --------------------------------------------------

    def create_colour_menu(self, view_menu):

        colour_menu = view_menu.addMenu("&Colour Scheme")

        self.colour_group = QActionGroup(self)
        self.colour_group.setExclusive(True)

        for scheme in self.panel_plot_terminal.terminal.availableColorSchemes():

            action = QAction(scheme, self)
            action.setCheckable(True)
            action.setChecked(
                scheme == self.settings_colour_scheme
            )

            self.colour_group.addAction(action)
            colour_menu.addAction(action)

            action.triggered.connect(
                lambda checked=False, scheme=scheme:
                    self.change_colour_scheme(scheme)
            )


    def change_colour_scheme(self, scheme):

        self.terminal.setColorScheme(scheme)
        self.colour_scheme.setText(scheme)
