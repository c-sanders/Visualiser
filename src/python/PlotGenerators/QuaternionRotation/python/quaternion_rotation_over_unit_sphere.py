import sys
import logging

import GlobalSettings
import DisplayUsage
from   QuaternionManipulator import QuaternionManipulator


logger = logging.getLogger(__name__)


# main
#   |- VectorManipulator::run
#        |- VectorManipulator::set_values_from_command_line_args
#        |- VectorManipulator::generate_plots
#           |- VectorManipulator::perform_quaternion_operations
#           |- VectorManipulator::update_plotting_agent
#           |- VectorManipulator::generate_plot
#                |- PlotAgent::generate_plot

def main() :

    nameMethod             = "::" + str(sys._getframe().f_code.co_name)
    quaternion_manipulator = QuaternionManipulator()


    # logger.debug(nameMethod + " : Enter")

    try :

        print(nameMethod + " : Number of arguments: " + str(len(sys.argv)))
        print(nameMethod + " : Arguments = " + str(sys.argv))

        logger.debug(nameMethod + " : Number of arguments: " + str(len(sys.argv)))
        logger.debug(nameMethod + " : Arguments = " + str(sys.argv))

        if len(sys.argv) != 11 :

            DisplayUsage.display_usage()

            raise ValueError("Exactly 11 arguments were not passed to this program from the command line.")

        level_logging = int(sys.argv[1])

        # logger = logging.getLogger()

        logger.setLevel(level_logging)
        level_logging = logger.getEffectiveLevel()

        print(nameMethod + " : Current logging level = " + str(level_logging))

        quaternion_manipulator.set_logging_level(level_logging)

        quaternion_manipulator.run(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])

    except Exception as e :

        DisplayUsage.display_exception(e)

    logger.debug(nameMethod + " : Exit")


if __name__ == "__main__":

    main()