import sys

from   matplotlib.colors import LinearSegmentedColormap
from   matplotlib.colors import Normalize
from   matplotlib.cm     import ScalarMappable

import GlobalSettings


my_colormap = LinearSegmentedColormap.from_list(
    "my_rainbow",
    [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
    ]
)


class ColorMapAgent :

    def __init__(self,

        plotting_agent : PlottingAgent,
        axis_plot
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        self._plotting_agent = plotting_agent
        self._axis           = axis_plot

        # Set the following attributes;
        #
        #   - colormap and its associated arrow
        #   - vector and history of vector points

        self._plot_handle_colormap                        = None
        self._plot_handle_colormap_arrow                  = None
        self._plot_handle_colormap_arrow_min              = None
        self._plot_handle_colormap_arrow_max              = None

        print(nameMethod + " : Exit")


    # Invoked by : External clients

    def add_colormap(self) :

        nameMethod  = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        # Place a color scale on the right hand side of this sub-plot.

        norm = Normalize(vmin=-0.6, vmax=0.6)

        sm = ScalarMappable(
                            norm=norm,
                            cmap=my_colormap
                           )
        sm.set_array([])

        self._plot_handle_colormap = self._plotting_agent._fig.colorbar(
                                                                        sm,
                                                                        ax=self._axis,
                                                                        location="left",
                                                                        pad=0.05,
                                                                        shrink=0.75
                                                                       )

        self._plot_handle_colormap.set_label(GlobalSettings.title_colormap)


    # Invoked by : External clients

    def _clear_plot_handle_colormap_arrows(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : Enter")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        if self._plot_handle_colormap_arrow is not None :

            print(nameMethod + " : self._plot_handle_colormap_arrow is not None")

            self._plot_handle_colormap_arrow.remove()
            self._plot_handle_colormap_arrow = None

        self._plot_handle_colormap_arrow_min.remove()
        self._plot_handle_colormap_arrow_max.remove()

        self._plot_handle_colormap_arrow_min = None
        self._plot_handle_colormap_arrow_max = None

        print(nameMethod + " : self._plot_handle_colormap_arrow is None")

        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : Exit")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nameMethod + " : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    # Invoked by : generate_plot

    def _update_colorbar(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # If an arrow currently points to the colorbar, then remove it.
        # Then place a new updated arrow next to the colorbar.

        # self.clear_plot_handle_colormap_arrow()

        current_value     = self._plotting_agent.quaternion_data.quaternion_pre_multiply.w
        current_value_min = self._plotting_agent.quaternion_data.quaternion_pre_multiply_min
        current_value_max = self._plotting_agent.quaternion_data.quaternion_pre_multiply_max

        print(nameMethod + " : MARKER 2")

        # Plot the arrows which are associated with the color bar.
        #
        # - The arrow associated with the current value.
        # - The arrow associated with the minimum value.
        # - The arrow associated with the maximum value.

        self._plot_handle_colormap_arrow = self._plot_handle_colormap.ax.annotate(
            "",
            xy=(1.0, current_value),  # Arrow tip
            xytext=(1.5, current_value),  # Arrow tail
            xycoords=("axes fraction", "data"),
            textcoords=("axes fraction", "data"),
            arrowprops=dict(
                arrowstyle="simple",
                color="black",
                lw=2
            )
        )

        self._plot_handle_colormap_arrow_min = self._plot_handle_colormap.ax.annotate(
            "",
            xy=(1.0, current_value_min),  # Arrow tip
            xytext=(1.5, current_value_min),  # Arrow tail
            xycoords=("axes fraction", "data"),
            textcoords=("axes fraction", "data"),
            arrowprops=dict(
                arrowstyle="simple",
                color="red",
                lw=2
            )
        )

        self._plot_handle_colormap_arrow_max = self._plot_handle_colormap.ax.annotate(
            "",
            xy=(1.0, current_value_max),  # Arrow tip
            xytext=(1.5, current_value_max),  # Arrow tail
            xycoords=("axes fraction", "data"),
            textcoords=("axes fraction", "data"),
            arrowprops=dict(
                arrowstyle="simple",
                color="green",
                lw=2
            )
        )

        print(nameMethod + " : Exit")