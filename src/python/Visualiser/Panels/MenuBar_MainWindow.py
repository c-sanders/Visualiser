from   PySide6.QtGui \
import (
        QAction,
        QActionGroup,
        QFont
       )


class MenuBar_MainWindow():

    def __init__(self):

        pass


    def set_parent(self, main_window):

        self.main_window = main_window


    # --------------------------------------------------
    # Menu bar
    # --------------------------------------------------

    def create_menu_bar(self):

        # Get a reference to the menubar which is a part of the QMainWindow.
        #
        # Remember that class QMainWindow comes with a menubar.

        menubar = self.main_window.menuBar()

        menubar.setStyleSheet("""
            QMenuBar {
                border-bottom: -10px solid #606060;
                padding-bottom: 10px;
            }
        """)

        # File menu

        self.menu_file = menubar.addMenu("&File")
        self.create_menu_file()

        # Settings menu

        self.menu_settings = menubar.addMenu("&Settings")
        self.create_menu_settings()

        # Debug menu

        self.menu_debug = menubar.addMenu("&Debug")
        self.create_menu_debug()

        # Build menu

        self.menu_build = menubar.addMenu("&Build")
        self.create_menu_build()

        # Run menu

        self.menu_run = menubar.addMenu("&Run")
        self.create_menu_run()


    def create_menu_file(self):

        action = QAction("E&xit", self.menu_file)
        action.setShortcut("Ctrl+Q")
        action.triggered.connect(self.main_window.close)

        self.menu_file.addAction(action)


    def create_menu_settings(self):

        action = QAction("&Settings", self.menu_settings)
        action.triggered.connect(self.main_window.panel_settings_display)

        self.menu_settings.addAction(action)


    def create_menu_debug(self):

        action_0 = QAction("Method : Visualiser_MainWindow::_run_diagnostics",               self.menu_debug)
        action_1 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_scroll",  self.menu_debug)
        action_2 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_scheme",  self.menu_debug)
        action_3 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_history", self.menu_debug)
        action_4 = QAction("Method : Visualiser_MainWindow::_list_terminal_methods_bar",     self.menu_debug)

        self.menu_debug.addAction(action_0)
        self.menu_debug.addAction(action_1)
        self.menu_debug.addAction(action_2)
        self.menu_debug.addAction(action_3)
        self.menu_debug.addAction(action_4)

        action_0.triggered.connect(self.main_window.diagnostics.run_diagnostics)
        action_1.triggered.connect(self.main_window.diagnostics.list_terminal_methods_scroll)
        action_2.triggered.connect(self.main_window.diagnostics.list_terminal_methods_scheme)
        action_3.triggered.connect(self.main_window.diagnostics.list_terminal_methods_history)
        action_4.triggered.connect(self.main_window.diagnostics.list_terminal_methods_bar)


    def create_menu_build(self):

        action_0 = QAction("Build LaTeX slides", self.menu_build)
        action_0.triggered.connect(self.main_window.build_latex_slides)

        action_0a = QAction("Build animation frames : Euler's formula flyaround", self.menu_build)
        # action_1.triggered.connect(self.main_window.build_frames_quaternion_rotation)

        action_0b = QAction("Build animation frames : Euler's formula flyaround - varying base", self.menu_build)
        # action_1.triggered.connect(self.main_window.build_frames_quaternion_rotation)

        action_1 = QAction("Build animation frames : Quaternion rotation", self.menu_build)
        action_1.triggered.connect(self.main_window.build_frames_quaternion_rotation)

        action_2 = QAction("Build UML class diagrams", self.menu_build)
        action_2.triggered.connect(self.main_window.build_uml_class_diagrams)

        action_3 = QAction("Build UML sequence diagrams", self.menu_build)
        action_3.triggered.connect(self.main_window.build_uml_sequence_diagrams)

        self.menu_build.addAction(action_0)
        self.menu_build.addAction(action_0a)
        self.menu_build.addAction(action_0b)
        self.menu_build.addAction(action_1)
        self.menu_build.addAction(action_2)
        self.menu_build.addAction(action_3)


    def create_menu_run(self):

        action = QAction("Run script : Generate quaternion rotation slides", self.menu_run)
        action.triggered.connect(self.main_window.panel_run_script_display)
        # action.triggered.connect(self.main_window.run_script)

        self.menu_run.addAction(action)
