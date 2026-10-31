from   PySide6.QtGui \
import (
        QAction,
        QActionGroup,
        QFont
       )


class MenuBuilder_MainWindow():

    def __init__(self):

        pass


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

        # Settings menu

        settings_menu = menubar.addMenu("&Settings")

        self.create_settings_menu(settings_menu)

        # Debug menu

        settings_debug = menubar.addMenu("&Debug")

        self.create_debug_menu(settings_debug)


    def create_settings_menu(self, settings_menu):

        action = QAction("&Settings", self)


        settings_menu = settings_menu.addAction(action)

        action.triggered.connect(self._panel_settings_display)


    def create_debug_menu(self, debug_menu):

        action_0 = QAction("Method : Visualiser_MainWindow::_run_diagnostics",               self)
        action_1 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_scroll",  self)
        action_2 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_scheme",  self)
        action_3 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_history", self)
        action_4 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_bar",     self)

        debug_menu.addAction(action_0)
        debug_menu.addAction(action_1)
        debug_menu.addAction(action_2)
        debug_menu.addAction(action_3)
        debug_menu.addAction(action_4)

        action_0.triggered.connect(self.diagnostics.run_diagnostics)
        action_1.triggered.connect(self.diagnostics.list_terminal_methods_scroll)
        action_2.triggered.connect(self.diagnostics.list_terminal_methods_scheme)
        action_3.triggered.connect(self.diagnostics.list_terminal_methods_history)
        action_4.triggered.connect(self.diagnostics.list_terminal_methods_bar)
