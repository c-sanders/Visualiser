class ObjectDirectory:

    def __init__(self):

        settings_config = None

        # Short convenient aliases for popular widgets.

        main_window          = None  # self
        panel_frame_terminal = None  # self.panel_frame_terminal
        terminal             = None  # self.panel_frame_terminal.panel_terminal.terminal


# Create one shared global instance of this object.

object_directory = ObjectDirectory()