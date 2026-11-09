import sys
import colorsys
import logging

import numpy as np

from   matplotlib.ticker import MultipleLocator

import PlottingAgent
import UnitSphere


logger = logging.getLogger(__name__)


# This class is inherited by :
#
#   - PlotHandleAgent_SubPlot_1
#   - PlotHandleAgent_SubPlot_2

class SubPlotAgent_UnitSphere :

    class_name = "SubPlotAgent"


    def __init__(self,

        plotting_agent: PlottingAgent,
        axis_plot
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self.plotting_agent = plotting_agent
        self._axis          = axis_plot

        self._unit_sphere   = UnitSphere.UnitSphere(self, axis_plot)

        self._unit_sphere.configure()

        self._counter = 0
        self._counter_hue_value = 0

        # Declare the following attributes;
        #
        #   - axis which this sub-plot belongs to
        #   - title of sub-plot
        #   - RGB color code for the surface of the unit sphere
        #   - unit sphere

        self._plot_handle_title_subplot                   = None

        self._plot_handle_surface                         = None

        self._v                                           = np.array([1.2, 0.8, 0.5])
        self._x                                           = None
        self._y                                           = None
        self._z                                           = None

        logger.debug(nameMethod + " : Exit")


    # Method : _setup_plot_basic

    def _setup_plot_basic(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._plot_axes()

        self._set_aspect_ratios_and_extents()

        self._fill_panes()
        self._configure_grid()
        # self.create_static_labels()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : configure

    def _plot_axes(self) :

        # Plot;
        #
        #   x axis
        #   y axis
        #   z axis

        self._axis.quiver(
            -1.2, 0, 0,
            2.4, 0, 0,
            color='black',
            linewidth=1,
            arrow_length_ratio=0.025
        )

        self._axis.quiver(
            0, -1.2, 0,
            0, 2.4, 0,
            color='black',
            linewidth=1,
            arrow_length_ratio=0.025
        )

        self._axis.quiver(
            0, 0, -1.2,
            0, 0, 2.4,
            color='black',
            linewidth=1,
            arrow_length_ratio=0.025
        )


    def _fill_panes(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._axis.xaxis.pane.fill = False
        self._axis.yaxis.pane.fill = False
        self._axis.zaxis.pane.fill = False

        logger.debug(nameMethod + " : Exit")


    def _configure_grid(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # ax.grid(False)

        self._axis.xaxis.set_major_locator(MultipleLocator(1))
        self._axis.yaxis.set_major_locator(MultipleLocator(1))
        self._axis.zaxis.set_major_locator(MultipleLocator(1))

        logger.debug(nameMethod + " : Exit")


    def delete_artifacts(self) :

        nameMethod = str(self.__class__.__name__) + "(->" + self.class_name + ")::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._unit_sphere._clear_sphere_wire_frame()
        self._unit_sphere._clear_sphere_surface()

        logger.debug(nameMethod + " : Exit")
