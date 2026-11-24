class Settings_Scripts:

    def __init__(self):

        self.file_generate_plot_frames    = "./src/python/PlotGenerators/QuaternionRotation/python/quaternion_rotation_over_unit_sphere.py"

        # self.command_run_script = "source /home/craig/local/source_code/python/sine_wave/venv/bin/activate && " + \
        #                           "python3 " + \
        #                           "./src/python/PlotGenerators/QuaternionRotation/python/quaternion_rotation_over_unit_sphere.py "

        self.command_generate_plot_frames = "source /home/craig/local/source_code/python/sine_wave/venv/bin/activate && " + \
                                            "python3 " + \
                                            self.file_generate_plot_frames + " "

        self.arguments_generate_plot_frames = "False rotation 0.577350 0.577350 0.577350 720 1 0 0"


settings_scripts = Settings_Scripts()