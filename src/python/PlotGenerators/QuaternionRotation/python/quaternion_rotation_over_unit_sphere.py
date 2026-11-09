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

    nameMethod = "main"

    quaternion_manipulator = QuaternionManipulator()


    logger.debug(nameMethod + " : Enter")

    try :

        logger.debug(nameMethod + " : Number of arguments: " + str(len(sys.argv)))
        logger.debug(nameMethod + " : Arguments = " + str(sys.argv))

        if len(sys.argv) != 10 :

            DisplayUsage.display_usage()

            raise ValueError("Exactly 10 arguments were not passed to this program from the command line.")

        quaternion_manipulator.run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])

    except Exception as e :

        DisplayUsage.display_exception(e)

    logger.debug(nameMethod + " : Exit")


if __name__ == "__main__":

    main()