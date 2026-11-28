import sys
import time
import logging

# from    ...Visualiser.Config     import SettingsConfig
import DisplayUsage
from   QuaternionManipulator      import QuaternionManipulator
# from   ..Logging.RootLoggerConfig import RootLoggerConfig


logger_root   = logging.getLogger()
logger_module = logging.getLogger(__name__)


# main
#   |- VectorManipulator::run
#        |- VectorManipulator::set_values_from_command_line_args
#        |- VectorManipulator::generate_plots
#           |- VectorManipulator::perform_quaternion_operations
#           |- VectorManipulator::update_plotting_agent
#           |- VectorManipulator::generate_plot
#                |- PlotAgent::generate_plot

# This main function is invoked in a QTermWidget from the following method;
#
#   Worker_GenerateFrames_QuaternionRotation::run
#
# using the following command;
#
#   Config.ObjectDirectory.object_directory.terminal.sendText(command)

def main() :

    nameMethod             = str(sys._getframe().f_code.co_name)
    quaternion_manipulator = QuaternionManipulator()

    try :

        setup_loggers()
        display_config_loggers()

        print(nameMethod + " : Enter")
        print(nameMethod + " : Python search path : ")

        for dirname in sys.path:

            logger_root.debug(nameMethod + " :    - " + dirname)

        print(nameMethod + " : Number of arguments: " + str(len(sys.argv)))
        print(nameMethod + " : Arguments = " + str(sys.argv))

        if len(sys.argv) != 11 :

            DisplayUsage.display_usage()

            raise ValueError("Exactly 11 arguments were not passed to this program from the command line.")

        # Configure the root logger.

        level_logging = int(sys.argv[1])

        configure_loggers(level_logging)

        # logger_root.debug(nameMethod + " : About to sleep for 10 seconds - C")
        # time.sleep(10)

        quaternion_manipulator.set_logging_level(level_logging)

        print(nameMethod + " : About to invoke : quaternion_manipulator.run")

        quaternion_manipulator.run(
            sys.argv[2],
            sys.argv[3],
            sys.argv[4],
            sys.argv[5],
            sys.argv[6],
            sys.argv[7],
            sys.argv[8],
            sys.argv[9],
            sys.argv[10],
        )

    except Exception as e :

        DisplayUsage.display_exception(e)

    print(nameMethod + " : <<<<< Exit >>>>>")


def setup_loggers() :

    nameMethod = str(sys._getframe().f_code.co_name)


    # Set up the root logger and the module logger for this module/file.

    # handler = logging.FileHandler(Config.SettingsConfig.settings.stdout)

    handler_file = logging.FileHandler(
        filename="application.log",
        mode="a",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        fmt="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
        datefmt="%H:%M:%S"
    )

    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(formatter)

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler_file],
        # format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        format="%(asctime)s :  %(message)s",
        datefmt="%H:%M:%S",
        force=True
    )


def display_config_loggers() :

    nameMethod = str(sys._getframe().f_code.co_name)


    print(nameMethod + " : Root logger level             = %s", logger_root.level)
    print(nameMethod + " : Module logger level           = %s", logger_module.level)

    print(nameMethod + " : Root logger effective level   = %s", str(logger_root.getEffectiveLevel()))
    print(nameMethod + " : Module logger effective level = %s", str(logger_module.getEffectiveLevel()))


def configure_loggers(level_logging) :

    nameMethod = "::" + str(sys._getframe().f_code.co_name)


    logger_root.setLevel(level_logging)

    level_logging = logger_root.getEffectiveLevel()

    print(nameMethod + " : New root logger logging level = " + str(level_logging))


if __name__ == "__main__":

    main()