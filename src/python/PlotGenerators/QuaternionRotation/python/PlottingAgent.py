import sys
import numpy             as np
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from   matplotlib.lines  import Line2D
# from   matplotlib.ticker import MultipleLocator
import json
import logging

# Import the Python Image Library, aka PIL.

from PIL import Image
from PIL.PngImagePlugin import PngInfo

import colorsys

import GlobalSettings
# import Utils

import QuaternionData
import ColorAgent
import SubPlotAgent_Quaternion_PreMultiply
import PlotHandleAgent_SubPlot_2


logger = logging.getLogger(__name__)
show_plots = False


class PlottingAgent :

    """
    Implements a class which is responsible for generating plots.

    The plots which this class generates, will be of the terms which are involved in a quaternionic rotation. Each plot
    will be composed of two sub-plots, where each of the two sub-plots is handled by its own class within this class.

    The terms which are involved in the quaternionic rotation - along with the viewing angle information, need to be
    passed into this class before it can generate a plot. Upon receiving all of this information, the class will store
    its own copies of it. By doing this, the information is then available to its two subclasses.
    """

    def __init__(

            self,
            title_plot
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._initialise_attributes(title_plot)
        self._initialise_plot()

        # We can create the sub-plots now that the main plot has been fully initialised.

        self._create_subplots()
        self._initialise_subplots()

        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        logger.debug(nameMethod + " : Exit")
        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


    def _initialise_attributes(self,

        title_plot
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Attributes which pertain to the layout of the plot.

        self._fig                         = None
        self._gs                          = None
        self._ax1                         = None
        self._ax2                         = None

        self._handle_title_plot           = None

        self.quaternion_data              = QuaternionData.QuaternionData()

        # Attributes which pertain to the quaternion rotation.
        #
        # These are local copies of externally generated data.

        self._angle_rotation              = None

        self._w_difference                = 0

        # Handle RGB values.

        self.color_agent                = ColorAgent.ColorAgent()

        # Attributes which pertain to the plot's viewing angle.

        self._azimuth_view_initial        = None
        self._elevation_view_initial      = None

        self._azimuth_view                = None
        self._elevation_view              = None

        self._radius                      = None

        self._subPlot_1                   = None
        self._subPlot_2                   = None

        logger.debug(nameMethod + " : Exit")


    # Invoked by : __init__

    def _initialise_plot(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._create_figure_and_axes()

        logger.debug(nameMethod + " : Exit")


    def _create_subplots(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._subPlot_1 = SubPlotAgent_Quaternion_PreMultiply.SubPlotAgent_Quaternion_PreMultiply(self)
        self._subPlot_2 = PlotHandleAgent_SubPlot_2.PlotHandleAgent_SubPlot_2(self)

        logger.debug(nameMethod + " : Exit")


    def _initialise_subplots(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._subPlot_1.setup_plot_basic()
        self._subPlot_2.setup_plot_basic()

        logger.debug(nameMethod + " : Exit")


    def set_radius_for_unit_sphere(self,

        radius
    ) :

        self._radius = radius


    def set_view_initial(self,

        azimuth_view_initial,
        elevation_view_initial
    ) :

        self._azimuth_view_initial   = azimuth_view_initial
        self._elevation_view_initial = elevation_view_initial


    def set_angle_rotation(

            self,
            angle_rotation
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._angle_rotation = angle_rotation

        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        logger.debug(nameMethod + " : self._angle_rotation = " + str(self._angle_rotation))

        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        logger.debug(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        logger.debug(nameMethod + " : Exit")


    # Invoked by : External clients
    #
    #   > QuaternionManipulator._update_plotting_agent

    def set_quaternion_values(

        self,
        quaternion_axis_rotation,
        quaternion_to_rotate,
        quaternion_pre_multiply,
        quaternion_rotated
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self.quaternion_data.set_quaternions_and_min_max_values(

            quaternion_axis_rotation,
            quaternion_to_rotate,
            quaternion_pre_multiply,
            quaternion_rotated
        )

        self.__update_rgb_values()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : _initialise_plot

    def _create_figure_and_axes(self) :

        # self._fig = plt.figure(figsize=(8, 8))

        # self._fig, (self._ax1, self._ax2) = plt.subplots(
        #
        #     2, 1,
        #     figsize=GlobalSettings.image_dimensions,
        #     subplot_kw={'projection': '3d'}
        # )

        # self._fig, axes (
        #     (self._ax1, self._ax2),
        #     (self._ax3, self._ax4)
        # ) = plt.subplots(
        #     2, 2,
        #     figsize=GlobalSettings.image_dimensions,
        #     # subplot_kw={'projection': '3d'}
        # )

        self._fig = plt.figure(figsize=(16, 14))

        self._gs = self._fig.add_gridspec(2, 2)

        self._ax1 = self._fig.add_subplot(self._gs[0, 0], projection='3d')
        self._ax2 = self._fig.add_subplot(self._gs[0, 1], projection='3d')

        # Move the following into : _set_legend

        # self._legend2 = self._fig.add_subplot(self._gs[1, 1])
        # self._legend2.axis('off')

        handles1, labels1 = self._ax1.get_legend_handles_labels()
        handles2, labels2 = self._ax2.get_legend_handles_labels()

    # Invoked by : _plot_quaternion_pre_multiply

    def _plot_unit_sphere_quaternion_pre_multiply(self, name_client) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)

        axis = self._ax1


        logger.debug(nameMethod + " : Enter")

        self._subPlot_1.plot_unit_sphere(axis)

        logger.debug(nameMethod + " : Exit")


    # Invoked by : _generate_subplot_1

    def _plot_quaternion_pre_multiply(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._subPlot_1.plot_quaternion_pre_multiply()
        self._subPlot_2.plot_quaternion_pre_multiply()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : set_quaternions_and_min_max_values

    def __update_rgb_values(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self.color_agent.update_rgb_value_current(self.quaternion_data.quaternion_pre_multiply.w)

        # If the minimum value has been updated, then update its corresponding RGB value.

        if self.quaternion_data.get_min_updated():

            self.color_agent.update_rgb_value_minimum(self.quaternion_data.quaternion_pre_multiply_min)

        # If the maximum value has been updated, then update its corresponding RGB value.

        if self.quaternion_data.get_max_updated():

            self.color_agent.update_rgb_value_current(self.quaternion_data.quaternion_pre_multiply_max)

        logger.debug(nameMethod + " : Exit")


    def _encode_metadata(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self.metadata = {
            "view" : {
                "azimuth"   : self._azimuth_view,
                "elevation" : self._elevation_view
            },
            "rotation" : {
                "angle" : self._angle_rotation,
                "axis" : {
                    "scalar" : self.quaternion_data.quaternion_axis_rotation.w,
                    "x"      : self.quaternion_data.quaternion_axis_rotation.x,
                    "y"      : self.quaternion_data.quaternion_axis_rotation.y,
                    "z"      : self.quaternion_data.quaternion_axis_rotation.z
                },
            },
            "quaternion_to_rotate": {
                "scalar"     : self.quaternion_data.quaternion_to_rotate.w,
                "x"          : self.quaternion_data.quaternion_to_rotate.x,
                "y"          : self.quaternion_data.quaternion_to_rotate.y,
                "z"          : self.quaternion_data.quaternion_to_rotate.z
            },
            "quaternion_pre_multiply": {
                "scalar"     : self.quaternion_data.quaternion_pre_multiply.w,
                "x"          : self.quaternion_data.quaternion_pre_multiply.x,
                "y"          : self.quaternion_data.quaternion_pre_multiply.y,
                "z"          : self.quaternion_data.quaternion_pre_multiply.z
            },
            "quaternion_rotated": {
                "scalar"     : self.quaternion_data.quaternion_rotated.w,
                "x"          : self.quaternion_data.quaternion_rotated.x,
                "y"          : self.quaternion_data.quaternion_rotated.y,
                "z"          : self.quaternion_data.quaternion_rotated.z
            },
        }


    def _display_metadata(

            self,
            filename
        ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        # Check that the JSON was written into the file properly.

        with Image.open(filename) as img:

            metadata = json.loads(img.text["com.example.simulation"])

            w = metadata["quaternion_pre_multiply"]["scalar"]
            x = metadata["quaternion_pre_multiply"]["x"]
            y = metadata["quaternion_pre_multiply"]["y"]
            z = metadata["quaternion_pre_multiply"]["z"]

            quaternion_pre_multiply = np.quaternion(w,x,y,z)

            logger.debug(f"quaternion_pre_multiply = <{quaternion_pre_multiply.w:.03f}, {quaternion_pre_multiply.x:.03f}, {quaternion_pre_multiply.y:.03f}, {quaternion_pre_multiply.z:.03f}>")

            logger.debug("========================================")
            logger.debug("JSON metadata from the file :")
            logger.debug("-----------------------------")
            logger.debug("View azimuth   = " + str(metadata["view"]["azimuth"]))
            logger.debug("View elevation = " + str(metadata["view"]["elevation"]))
            logger.debug("Rotation angle = " + str(metadata["rotation"]["angle"]))
            logger.debug("Rotation axis  = " + str(metadata["rotation"]["axis"]["scalar"]))
            logger.debug("========================================")


    # Invoked by : PlottingAgent::_generate_subplot_1

    def _set_title_and_legend_subplot_1(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # ----------------------------
        # Labels
        # ----------------------------

        # ax.set_xlabel('x')
        # ax.set_ylabel('y')
        # ax.set_zlabel('z')
        # self._fig.set_title("Poop")

        # Set the title for subplot 1.

        self._subPlot_1.set_title(GlobalSettings.title_sub_plot_1, GlobalSettings.raise_exception_if_already_set)

        self._subPlot_1.set_legend()

        logger.debug(nameMethod + " : MARKER A")

        # Set the legend for subplot 1.

        logger.debug(nameMethod + " : Exit")


    # Invoked by : _generate_subplot_2()

    def _set_title_and_legend_subplot_2(self):

        """
        Set the title and legend for the specified plot or sub-plot.

        This method sets the title and legend for the plot or sub-plot which was passed to the argument axis.

        Args:
            axis (matplotlib.axes.Axes):
                The plot or sub-plot which is to be operated on.

        Returns:
            None:
                This method only updates the internal state of the object.
        """

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._ax2.set_title(GlobalSettings.title_sub_plot_2)

        # ----------------------------
        # Labels
        # ----------------------------

        # ax.set_xlabel('x')
        # ax.set_ylabel('y')
        # ax.set_zlabel('z')

        if GlobalSettings.display_legend_subplot_2 :

            legend_elements = [
                Line2D([0], [0], color='red',             lw=1, label=self.label_quaternion_axis_rotation),
                Line2D([0], [0], color='green',           lw=1, label=self.label_quaternion_to_rotate),
                Line2D([0], [0], color='none',            lw=1, label=self.label_quaternion_pre_multiply),
                Line2D([0], [0], linestyle='None', marker=None, label=self.label_quaternion_pre_multiply_min),
                Line2D([0], [0], linestyle='None', marker=None, label=self.label_quaternion_pre_multiply_max),
                Line2D([0], [0], color='magenta',         lw=1, label=self.label_quaternion_rotated),
                Line2D([0], [0], linestyle='None', marker=None, label=self.label_angle_rotation)
            ]

            legend = self._ax2.legend(
                handles=legend_elements,
                prop={
                    "family": "Liberation Mono",
                    "size": 10
                },
                loc='upper right',
                fontsize=10
            )

            # If the scalar part of the quaternion is not close in value to 0, then display its text in red

            # if abs(self.quaternion_pre_multiply.x) > 0.001 :

            hue_value = ((self.quaternion_pre_multiply.w) * 0.5) + 0.5

            rgb_value_local = colorsys.hsv_to_rgb(

                hue_value,  # hue (0–1)
                1.0,  # saturation
                1.0  # value
            )

            logger.debug(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            logger.debug(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            logger.debug(nameMethod + f" : About to set legend color to = <{hue_value:f}, 1.0, 1.0>")
            logger.debug(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            logger.debug(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            legend.get_texts()[2].set_color(rgb_value_local)

        logger.debug(nameMethod + " : Exit")


    def _add_metadata_to_file(

            self,
            filename
    ) :

        with Image.open(filename) as img :

            info = PngInfo()
            info.add_itxt(
                "com.example.simulation",
                json.dumps(self.metadata, indent=2)
            )

            img.save(filename, pnginfo=info)


    def set_titles(

        self,
        title_plot,
        title_sub_plot_1,
        title_sub_plot_2
    ) :

        self.title_plot       = title_plot
        self.title_sub_plot_1 = title_sub_plot_1
        self.title_sub_plot_2 = title_sub_plot_2


    def set_view(

            self,
            azimuth_view,
            elevation_view
    ) :

        self._azimuth_view   = azimuth_view
        self._elevation_view = elevation_view

        self._azimuth_view_delta   = self._azimuth_view   - self._azimuth_view_initial
        self._elevation_view_delta = self._elevation_view - self._elevation_view_initial


    def _save_plot_to_file(

            self,
            filename
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        logger.debug("Saving the figure to file : " + str(filename) + "\n")

        self._fig.savefig(

            filename,
            dpi         = GlobalSettings.image_dpi,
            bbox_inches = GlobalSettings.image_bbox_argument
        )

        with Image.open(filename) as image_handle :

            logger.debug(nameMethod + " : ????????????????????????????????????????")
            logger.debug(nameMethod + " : ????????????????????????????????????????")
            logger.debug(nameMethod + " : Image dimensions = " + str(image_handle.size))
            logger.debug(nameMethod + " : ????????????????????????????????????????")
            logger.debug(nameMethod + " : ????????????????????????????????????????")

        logger.debug(nameMethod + " : Exit")


    def _encode_metadata_into_file(

            self,
            filename
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._encode_metadata()
        self._add_metadata_to_file(filename)
        self._display_metadata(filename)

        logger.debug(nameMethod + " : Exit")


    def _delete_artifacts(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : Enter")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        # Remove artifacts from the sub-plots.

        self._subPlot_2.delete_plot_artifacts()
        logger.debug(nameMethod + " : Have deleted the plot artifacts from subPlot_2")

        self._subPlot_1.delete_plot_artifacts(nameMethod)
        logger.debug(nameMethod + " : Have deleted the plot artifacts from subPlot_1")

        # Remove artifacts from the plot itself.


    def _set_title_plot(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Set the title for the entire plot.

        self._handle_title_plot = self._fig.suptitle(
                                                     GlobalSettings.title_plot,
                                                     fontsize=20
                                                    )

        logger.debug(nameMethod + " : Exit")


    def _show_plot_if_enabled(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        if show_plots :

            plt.show()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : generate_plot

    def _set_rgb_values_for_sphere_surfaces(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self._subPlot_1._set_rgb_value_for_sphere_surface()

        logger.debug(nameMethod + " : MARKER 1")

        self._subPlot_2._set_rgb_value_for_sphere_surface()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : QuaternionManipulator::_generate_plots
    #
    # generate_plot
    #   |- self._set_title_plot()
    #   |- self._set_rgb_values_for_sphere_surfaces()
    #   |- self._generate_subplots()
    #   |    |- self._subPlot_1.generate_plot()
    #   |    |    |- self._set_title()
    #   |    |    |- self._set_legend()
    #   |    |    |- self._update_colorbar()
    #   |    |    |- self._unit_sphere.plot_sphere()
    #   |    |    |- self._axis.view_init()
    #   |    |- self._subPlot_2.generate_plot()
    #   |- self._save_plot_to_file
    #   |- self._encode_metadata_into_file
    #   |- self._delete_artifacts

    def generate_plot(self,

        filename
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : Enter")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.debug(nameMethod + " : self._angle_rotation = " + str(self._angle_rotation))
        logger.debug(nameMethod + " : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        # Plot handles may be created by the following methods.

        self._set_title_plot()

        self._subPlot_1.generate_plot()
        self._subPlot_2.generate_plot()

        # Plot handles shouldn't be created by the following methods.

        self._save_plot_to_file(filename)
        self._encode_metadata_into_file(filename)
        self._show_plot_if_enabled()

        # Destroy those plot handles which aren't required anymore.

        self._delete_artifacts()

        logger.debug(nameMethod + " : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.debug(nameMethod + " : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.debug(nameMethod + " : Exit")
        logger.debug(nameMethod + " : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.debug(nameMethod + " : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


    def _destroy_plot(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Close the figure so that we can free up the memory it is using.

        plt.close(self._fig)

        self._fig = None
        self.ax  = None

        logger.debug(nameMethod + " : Exit")