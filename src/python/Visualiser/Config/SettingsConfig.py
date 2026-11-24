class SettingsConfig:

    def __init__(self):

        self.stdout                   = None
        self.stdin                    = None
        self.stderr                   = None

        self.raise_exception_on_error = True
        self.save_settings_on_exit    = None
        self.terminal_is_read_only    = True
        self.font_size                = None
        self.color_scheme             = None

        self.command_build_latex_slides = "pwd && " + \
                                          "pdflatex -output-directory=./slides/pdf ./src/latex/slides/slide.tex && " + \
                                          "pdftoppm -progress -png -f 2 -l 2 -r 1440 -singlefile ./slides/pdf/slide.pdf ./slides/png/slide_2\n"


settings = SettingsConfig()
