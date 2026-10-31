import sys

from   matplotlib.lines  import Line2D

import GlobalSettings
import Utils


class LabelAgent :

    def __init__(self,

        plotting_agent : PlottingAgent,
        axis_plot
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self.plotting_agent = plotting_agent
        self._axis          = axis_plot

        self._plot_handle_title                     = None
        self._plot_handle_text                      = None
        self._plot_handle_legend                    = None

        self._label_quaternion_axis_rotation        = ""
        self._label_quaternion_to_rotate            = ""
        self._label_quaternion_pre_multiply         = ""
        self._label_quaternion_pre_multiply_min     = ""
        self._label_quaternion_pre_multiply_max     = ""
        self._label_quaternion_rotated              = ""
        self._label_angle_rotation                  = ""
        self._label_spacer                          = ""
        self._label_heading                         = ""
        self._label_viewing_angle_azimuth_initial   = ""
        self._label_viewing_angle_azimuth           = ""
        self._label_viewing_angle_azimuth_delta     = ""
        self._label_viewing_angle_elevation_initial = ""
        self._label_viewing_angle_elevation         = ""
        self._label_viewing_angle_elevation_delta   = ""

        print(nameMethod + " : Exit")


    # Invoked by : _add_labels_to_plot

    def _generate_labels_legend(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        label_quaternion_axis_rotation = Utils.generate_string(self.plotting_agent.quaternion_data.quaternion_axis_rotation.w,
                                                               self.plotting_agent.quaternion_data.quaternion_axis_rotation.x,
                                                               self.plotting_agent.quaternion_data.quaternion_axis_rotation.y,
                                                               self.plotting_agent.quaternion_data.quaternion_axis_rotation.z)

        print(nameMethod + " : MARKER 0")

        label_quaternion_to_rotate     = Utils.generate_string(self.plotting_agent.quaternion_data.quaternion_to_rotate.w,
                                                               self.plotting_agent.quaternion_data.quaternion_to_rotate.x,
                                                               self.plotting_agent.quaternion_data.quaternion_to_rotate.y,
                                                               self.plotting_agent.quaternion_data.quaternion_to_rotate.z)

        print(nameMethod + " : MARKER 1")

        label_quaternion_pre_multiply  = Utils.generate_string(self.plotting_agent.quaternion_data.quaternion_pre_multiply.w,
                                                               self.plotting_agent.quaternion_data.quaternion_pre_multiply.x,
                                                               self.plotting_agent.quaternion_data.quaternion_pre_multiply.y,
                                                               self.plotting_agent.quaternion_data.quaternion_pre_multiply.z)

        print(nameMethod + " : MARKER 2")

        label_quaternion_rotated       = Utils.generate_string(self.plotting_agent.quaternion_data.quaternion_rotated.w,
                                                               self.plotting_agent.quaternion_data.quaternion_rotated.x,
                                                               self.plotting_agent.quaternion_data.quaternion_rotated.y,
                                                               self.plotting_agent.quaternion_data.quaternion_rotated.z)

        # self.check_min_max_values()

        label_quaternion_pre_multiply_min = Utils.format_component("", False, self.plotting_agent.quaternion_data.quaternion_pre_multiply_min)
        label_quaternion_pre_multiply_max = Utils.format_component("", False, self.plotting_agent.quaternion_data.quaternion_pre_multiply_max)

        print(nameMethod + " : MARKER 2")

        self._label_quaternion_axis_rotation        = f"Axis of rotation (q)      : " + label_quaternion_axis_rotation
        self._label_quaternion_to_rotate            = f"Quaternion to rotate (v)  : " + label_quaternion_to_rotate
        self._label_quaternion_pre_multiply         = f"Pre multiplication (qv)   : " + label_quaternion_pre_multiply
        self._label_quaternion_pre_multiply_min     =  "  - qv scalar value : min : " + label_quaternion_pre_multiply_min
        self._label_quaternion_pre_multiply_max     =  "  - qv scalar value : max : " + label_quaternion_pre_multiply_max
        self._label_quaternion_rotated              = f"Quaternion rotated (qvq$^{{*}}\,$) : " + label_quaternion_rotated
        self._label_angle_rotation                  = f"Angle of rotation         = {self.plotting_agent._angle_rotation:8.3f} degrees"
        self._label_spacer                          = ""
        self._label_heading                         = f"Viewing angle"
        self._label_viewing_angle_azimuth_initial   = f"  - Azimuth initial       =  {self.plotting_agent._azimuth_view_initial:4.1f} degrees"
        self._label_viewing_angle_azimuth           = f"  - Azimuth               =  {self.plotting_agent._azimuth_view:4.1f} degrees"
        self._label_viewing_angle_azimuth_delta     = f"  - Azimuth $\Delta\;\:$            =  {self.plotting_agent._azimuth_view_delta:4.1f} degrees"
        self._label_viewing_angle_elevation_initial = f"  - Elevation initial     =   {self.plotting_agent._elevation_view:4.1f} degrees"
        self._label_viewing_angle_elevation         = f"  - Elevation             =   {self.plotting_agent._elevation_view:4.1f} degrees"
        self._label_viewing_angle_elevation_delta   = f"  - Elevation $\Delta\;\:$          =   {self.plotting_agent._elevation_view_delta:4.1f} degrees"

        print(nameMethod + " : Exit")


    # Invoked by : generate_plot

    def _set_legend(self,

        raise_if_set
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # If exceptions are enabled for this method and the plot title is already set, then have this method raise an
        # exception.

        if (
            (raise_if_set) and
            (self._plot_handle_title is not None)
        ) :

            raise Exception("Attribute _plot_handle_title : Trying to set this attribute whilst it is already set.")

        self._generate_labels_legend()

        if (GlobalSettings.display_legend_subplot_1) :

            # Configure the individual elements which will comprise the legend.

            legend_elements = [

                # Line2D([0], [0], color='red',             lw=1, label=self.label_quaternion_axis_rotation),
                # Line2D([0], [0], color='green',           lw=1, label=self.label_quaternion_to_rotate),
                Line2D([0], [0], color='none',     lw=1,        label=self._label_quaternion_pre_multiply),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_quaternion_pre_multiply_min),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_quaternion_pre_multiply_max),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_spacer),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_quaternion_rotated),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_spacer),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_angle_rotation),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_spacer),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_heading),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_azimuth_initial),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_azimuth),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_azimuth_delta),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_spacer),

                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_elevation_initial),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_elevation),
                Line2D([0], [0], linestyle='None', marker=None, label=self._label_viewing_angle_elevation_delta)
            ]

            # ####################################
            # Work out where to put the following.
            # ####################################

            self._legend1 = self.plotting_agent._fig.add_subplot(self.plotting_agent._gs[1, 0])
            self._legend1.axis('off')

            # handles1, labels1 = self._ax1.get_legend_handles_labels()

            # Configure the legend itself and set the subplot to use it.

            # self.plot_handle_legend = self.plotting_agent._ax1.legend(
            #
            #     handles=legend_elements,
            #     prop={
            #         "family": "Liberation Mono",
            #         "size": 10
            #     },
            #     loc='lower center',
            #     fontsize=10
            # )

            # self.plot_handle_legend = self.plotting_agent._ax1.legend(

            self._plot_handle_legend = self._legend1.legend(

                handles=legend_elements,
                prop={
                    "family": "Liberation Mono",
                    "size": 14
                },
                loc='upper center',
                bbox_to_anchor=(0.5, 1.0),
                fontsize=10
            )

            #####

            if False :

                self._legend1 = self._ax1.legend(
                    handles,
                    labels,
                    loc="upper center",
                    bbox_to_anchor=(0.5, -0.05)
                )

            #####

            # hue_value = ((self.plotting_agent.quaternion_pre_multiply.w) * 0.5) + 0.5

            # rgb_value_local = colorsys.hsv_to_rgb(
            #
            #     hue_value,  # hue (0–1)
            #     1.0,  # saturation
            #     1.0  # value
            # )

            # print(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(nameMethod + f" : About to set legend color to = <{hue_value:f}, 1.0, 1.0>")
            # print(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(nameMethod + " : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            # self._plot_handle_legend.get_texts()[1].set_color(self.plotting_agent.color_agent.get_rgb_value_minimum)
            # self._plot_handle_legend.get_texts()[2].set_color(self.plotting_agent.color_agent.get_rgb_value_maximum)

        print(nameMethod + " : Exit")


    # Invoked by :

    def _add_labels_to_plot(self,

        axis,
        name_client
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._generate_labels_legend()

        print(nameMethod + " : MARKER 0")

        self._generate_labels_vector_tips()

        print(nameMethod + " : MARKER 1")

        self._add_axis_labels_to_plot()

        # ax.text(
        #     quaternion_to_rotate[0], quaternion_to_rotate[1], quaternion_to_rotate[2],
        #     label_quaternion_to_rotate_tip,
        #     color="green"
        # )

        # ax.text(
        #     quaternion[1], quaternion[2], quaternion[3],
        #     label_vector_c_tip,
        #     color="blue"
        # )

        # ax.text(
        #     quaternion_rotated[0], quaternion_rotated[1], quaternion_rotated[2],
        #     label_quaternion_rotated_tip,
        #     color="magenta"
        # )

        print(nameMethod + " : Exivt")


    # Invoked by : _add_labels_to_plot

    def _generate_labels_vector_tips(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # Label vector tip

        # label_vector_a_tip = "<" + str(vector_a[0])   + ", " + str(vector_a[1])   + ", " + str(vector_a[2]) + ">"
        # label_quaternion_to_rotate_tip = "<" + str(quaternion_to_rotate[0])   + ", " + str(quaternion_to_rotate[1])   + ", " + str(quaternion_to_rotate[2]) + ">"
        # label_vector_c_tip = "<" + str(quaternion[1]) + ", " + str(quaternion[1]) + ", " + str(quaternion[2]) + ", " + str(quaternion[2]) + ">"
        # label_vector_d_tip = "<" + str(vector_d[0])   + ", " + str(vector_d[1])   + ", " + str(vector_d[2]) + ">"

        # label_vector_a_tip = f"Axis       : 0.000 + i{vector_a[0]:.3f} + j{vector_a[1]:.3f} + k{vector_a[2]:.3f}"
        # label_quaternion_to_rotate_tip = f"Vector     : 0.000 + i{quaternion_to_rotate[0]:.3f} + j{quaternion_to_rotate[1]:.3f} + k{quaternion_to_rotate[2]:.3f}"
        # label_vector_c_tip = f"Partial    : {quaternion[0]:.3f} + i{quaternion[1]:.3f} + j{quaternion[2]:.3f} + k{quaternion[3]:.3f}"

        print(nameMethod + " : Exit")


    # Invoked by : _add_labels_to_plot

    def _add_axis_labels_to_plot(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._axis.text(
            1.3, 0, 0,
            "x",
            color="black"
        )

        self._axis.text(
            0, 1.3, 0,
            "y",
            color="black"
        )

        self._axis.text(
            0, 0, 1.3,
            "z",
            color="black"
        )

        print(nameMethod + " : Exit")


    # Invoked by : generate_plot

    def _set_title(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # if (
        #     (raise_if_set) and
        #     (self._plot_handle_title is not None)
        # ) :

        #     raise Exception("Attribute _plot_handle_title : Trying to set this attribute whilst it is already set.")

        # self._plot_handle_title = plot_handle_title

        w = Utils.format_component("", False, self.plotting_agent.quaternion_data.quaternion_pre_multiply.w)

        print(nameMethod + " : MARKER 0")

        # local_string = f"Hue = {self._hue_value:.3f}"

        # title_sub_plot = f"$qv$ in $S^{{3}}$\n$w={w}$"

        if self.plotting_agent._w_difference < 0 :

            title_sub_plot = f"$w={w} \\downarrow$"

        elif self.plotting_agent._w_difference > 0 :

            title_sub_plot = f"$w={w} \\uparrow$"

        else :

            title_sub_plot = f"$w={w} -$"

        print(nameMethod + " : MARKER 1")

        radius = 1 - (self.plotting_agent.quaternion_data.quaternion_pre_multiply.w ** 2)

        self._axis.set_title(f"Sphere with radius = {radius:.3f}")

        # self._axis.set_title(
        #     f"Plot of $qv$ onto the surface of $S^{{3}}$",
        #     fontsize=14
        # )

        print(nameMethod + " : MARKER 2")

        self._plot_handle_text = self._axis.text2D(
                                                   0.5, -0.12,
                                                   title_sub_plot,
                                                   transform=self._axis.transAxes,
                                                   ha="center",
                                                   va="top",
                                                   fontsize=14
                                                  )

        print(nameMethod + " : Exit")


    def delete_artifacts(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : Enter")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

        if self._plot_handle_title is not None :

            self._plot_handle_title.remove()
            self._plot_handle_title = None

        if self._plot_handle_text is not None :

            self._plot_handle_text.remove()
            self._plot_handle_text = None

        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : Exit`")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(nameMethod + " : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(nameMethod + " : &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

