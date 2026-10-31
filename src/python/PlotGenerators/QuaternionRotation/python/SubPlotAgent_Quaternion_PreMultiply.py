import sys
import colorsys

import numpy as np

import GlobalSettings
import Utils
import SubPlotAgent_UnitSphere
import PlottingAgent
import ColorMapAgent
import LabelAgent


# A UML class diagram can be generated for the class which is defined in this file, by using the following commands;
#
#   pyreverse ./SubPlotAgent_Quaternion_PreMultiply.py ./SubPlotAgent_UnitSphere.py ./ColorMapAgent.py ./LabelAgent.py ./UnitSphere.py \
#             -f ALL \
#             -o puml \
#             -p SubPlotAgent_Quaternion_PreMultiply \
#   \
#   &&
#   \
#   plantuml ./packages_PlotHandleAgent_SubPlot_1.puml

class SubPlotAgent_Quaternion_PreMultiply(SubPlotAgent_UnitSphere.SubPlotAgent_UnitSphere) :

    # Only create an instance of this class once an instance of the PlottingAgent class has been fully configures.

    def __init__(self,

        plotting_agent: PlottingAgent.PlottingAgent
    ) :

        super().__init__(

            plotting_agent,
            plotting_agent._ax1
        )

        self._axis_plot                                   = None

        self.color_map_agent                              = ColorMapAgent.ColorMapAgent(plotting_agent, plotting_agent._ax1)
        self.label_agent                                  = LabelAgent.LabelAgent(plotting_agent, plotting_agent._ax1)

        self._plot_handle_quaternion_pre_multiply         = None
        self._plot_handle_quaternion_pre_multiply_history = None

        self._initialise_plot()


    def _initialise_plot(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : Exit")


    # Invoked by : External clients
    #
    #   - PlottingAgent._initialise_subplots
    #
    #   > Public method
    #
    # Just set up the basics for the plot

    def setup_plot_basic(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._axis_plot = self.plotting_agent._ax1

        self.color_map_agent.add_colormap()

        super()._setup_plot_basic()

        # raise Exception("CODE ANALYSIS EXCEPTION!!!")

        print(nameMethod + " : Exit")


    # Invoked by : configure

    def _set_aspect_ratios_and_extents(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # ----------------------------
        # Set equal aspect ratio
        # ----------------------------

        max_extent = max(
                         np.max(np.abs(self._v)),
                         1.0
                        )

        self._axis_plot.set_xlim([-max_extent, max_extent])
        self._axis_plot.set_ylim([-max_extent, max_extent])
        self._axis_plot.set_zlim([-max_extent, max_extent])

        self._axis_plot.set_box_aspect([1, 1, 1])

        print(nameMethod + " : Exit")


    def _clear_plot_handle_quaternion_pre_multiply(self) :

        if self._plot_handle_quaternion_pre_multiply is not None :

            self._plot_handle_quaternion_pre_multiply.remove()
            self._plot_handle_quaternion_pre_multiply = None


    def _delete_artifacts_local(self) :

        self._clear_plot_handle_quaternion_pre_multiply()

        self.label_agent.delete_artifacts()
        self.color_map_agent._clear_plot_handle_colormap_arrows()


    def delete_plot_artifacts(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # Delete artifacts which have been created by this class.

        self._delete_artifacts_local()

        # Delete artifacts which have been created in the base class.

        super().delete_artifacts()

        print(nameMethod + " : Exit")


    # Invoked by : _generate_subplot_1

    def _plot_quaternion_pre_multiply(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)

        sub_plot = self.plotting_agent._ax1


        print(nameMethod + " : Enter")

        if self._plot_handle_quaternion_pre_multiply is not None :

            raise Exception("Attribute _plot_handle_quaternion_pre_multiply : Trying to set this attribute whilst it is already set.")

        self._plot_handle_quaternion_pre_multiply = self._axis_plot.quiver(

            0, 0, 0,
            self.plotting_agent.quaternion_data.quaternion_pre_multiply.x, self.plotting_agent.quaternion_data.quaternion_pre_multiply.y,
            self.plotting_agent.quaternion_data.quaternion_pre_multiply.z,
            color='blue',
            linewidth=1,
            arrow_length_ratio=0.1
        )

        if GlobalSettings.plot_quaternion_pre_multiply_history :

            # Append the current point onto the end of the plot history.

            hue_value = ((self.plotting_agent.quaternion_data.quaternion_pre_multiply.x) * 0.5) + 0.5

            # rgb_value = colorsys.hsv_to_rgb(
            #
            #     hue_value,  # hue (0–1)
            #     1.0,  # saturation
            #     1.0  # value
            # )

            markersize_value = (hue_value * 4) + 2

            if self.plotting_agent.quaternion_data.quaternion_pre_multiply.w < 0 :

                marker_value = 'v'

            else :

                marker_value = '^'

            sub_plot.plot(

                self.plotting_agent.quaternion_data.quaternion_pre_multiply.x,
                self.plotting_agent.quaternion_data.quaternion_pre_multiply.y,
                self.plotting_agent.quaternion_data.quaternion_pre_multiply.z,
                marker=marker_value,
                markersize=markersize_value,
                linestyle='-',
                color=self.plotting_agent.color_agent.get_rgb_value_current()
            )

        print(nameMethod + " : Exit")


    # Invoked by : External clients
    #
    #   > PlottingAgent._generate_subplots

    def generate_plot(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        radius_sphere        = 1 - (self.plotting_agent.quaternion_data.quaternion_pre_multiply.w ** 2)
        color_sphere_surface = self.plotting_agent.color_agent.get_rgb_value_current()

        # - Set the title which is to be used for this sub-plot.
        # - Set the legend which is to be used for this sub-plot.

        self.label_agent._set_title()
        print(nameMethod + " : MARKER 0")
        self.label_agent._set_legend(True)
        print(nameMethod + " : MARKER 1")

        # - Update the arrows which are associated with the color bar.

        self.color_map_agent._update_colorbar()

        self._unit_sphere.plot(

            radius_sphere,
            color_sphere_surface
        )

        self._set_aspect_ratios_and_extents()

        self._fill_panes()
        self._configure_grid()

        # self.add_labels_to_plot(axis)
        # self.label_agent._set_title()
        # self.label_agent._set_legend(True)

        # self._plot_quaternions()

        print(nameMethod + " : About to invoke method : self._unit_sphere.plot_sphere")

        # self._plot_quaternion_pre_multiply()
        # self.add_labels_to_plot(axis)

        print(nameMethod + " : Elevation = " + str(self.plotting_agent._elevation_view))

        self._axis_plot.view_init(

            elev=self.plotting_agent._elevation_view,
            azim=self.plotting_agent._azimuth_view
        )

        print(nameMethod + " : Exit")
