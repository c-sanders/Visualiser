class SettingsConfig:

    def __init__(self):

        self.raise_exception_on_error = True
        self.save_settings_on_exit    = None
        self.font_size                = None
        self.color_scheme             = None

        self.command_build_latex_slides = "pwd && " + \
                                          "pdflatex -output-directory=./slides/pdf ./src/latex/slides/slide.tex && " + \
                                          "pdftoppm -progress -png -f 2 -l 2 -r 1440 -singlefile ./slides/pdf/slide.pdf ./slides/png/slide_2\n"

        self.command_run_script = "source /home/craig/local/source_code/python/sine_wave/venv/bin/activate && " + \
                                  "python3 ./src/python/PlotGenerators/QuaternionRotation/python/quaternion_rotation_over_unit_sphere.py False rotation 0.577350 0.577350 0.577350 720 1 0 0\n"
        #
        #


settings = SettingsConfig()
