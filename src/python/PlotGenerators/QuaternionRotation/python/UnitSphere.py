import sys

import numpy as np
import matplotlib.pyplot as plt


class UnitSphere :

    def __init__(self,

        sub_plot_agent : SubPlotAgent,
        axis_plot
    ) :

        self._sub_plot_agent          = sub_plot_agent
        self._ax                      = axis_plot


        self._x                       = None
        self._y                       = None
        self._z                       = None

        self._radius                  = 1
        self._color_sphere_surface    = None

        self._surface_resolution      = None
        self._grid_resolution         = None

        self._surface_color           = None
        self._handle_surface          = None

        self._num_latitudes           = None
        self._num_longitudes          = None

        self._handle_wireframe        = None

        self._handles_lines_latitude  = []
        self._handles_lines_longitude = []

        self._plot_handle_sphere_wire_frame = None
        self._plot_handle_sphere_surface    = None

        self._filename                = None


    def configure(self,

        num_latitudes      = 9,
        num_longitudes     = 12,
        surface_resolution = 100,
        grid_resolution    = 200
    ) :

        self._num_latitudes      = num_latitudes
        self._num_longitudes     = num_longitudes
        self._surface_resolution = surface_resolution
        self._grid_resolution    = grid_resolution


    # Invoked by : plot_sphere

    def __setup_values(self) :

        u = np.linspace(0, 2 * np.pi, self._surface_resolution)
        v = np.linspace(0, np.pi,     self._surface_resolution)

        u, v = np.meshgrid(u, v)

        self._x = self._radius * np.sin(v) * np.cos(u)
        self._y = self._radius * np.sin(v) * np.sin(u)
        self._z = self._radius * np.cos(v)


    def __plot_surface_and_grid_lines(self) :

        self.__plot_surface()

        # self.__plot_latitude_lines_on_sphere()
        # self.__plot_longitude_lines_on_sphere()

        self._handle_wireframe = self._ax.plot_wireframe(

            self._x,
            self._y,
            self._z,
            color='black',
            linewidth=0.4,
            rstride=4,
            cstride=4
        )


    #

    def __plot_surface(self) :

        self._handle_surface = self._ax.plot_surface(

            self._x,
            self._y,
            self._z,
            color       = self._color_sphere_surface,
            alpha       = 0.2,
            shade       = True,
            linewidth   = 0,
            antialiased = True
        )


    def __plot_latitude_lines_on_sphere(self) :

        longitude = np.linspace(0, 2 * np.pi, self._grid_resolution)

        latitudes = np.linspace(

                        -np.pi / 2,
                        np.pi / 2,
                        self._num_latitudes + 2
                    )[1:-1]

        for latitude in latitudes:

            x_line = self._radius * np.cos(latitude) * np.cos(longitude)
            y_line = self._radius * np.cos(latitude) * np.sin(longitude)
            z_line = self._radius * np.full_like(
                longitude,
                np.sin(latitude)
            )

            self._handles_lines_latitude.append(

                self._ax.plot(

                    x_line,
                    y_line,
                    z_line,
                    color="black",
                    linewidth=0.8
                )
            )


    def __plot_longitude_lines_on_sphere(self) :

        latitude = np.linspace(
            -np.pi / 2,
            np.pi / 2,
            self._grid_resolution
        )

        longitudes = np.linspace(
            0,
            2 * np.pi,
            self._num_longitudes,
            endpoint=False
        )

        for longitude_value in longitudes:

            x_line = self._radius * np.cos(latitude) * np.cos(longitude_value)
            y_line = self._radius * np.cos(latitude) * np.sin(longitude_value)
            z_line = self._radius * np.sin(latitude)

            self._handles_lines_longitude.append(

                self._ax.plot(

                    x_line,
                    y_line,
                    z_line,
                    color="black",
                    linewidth=0.8
                )
            )


    def __setup_plot_environment(self) :

        # -------------------------------------------------
        # 4. Set the coordinate system
        # -------------------------------------------------

        self._ax.set_xlim([-1, 1])
        self._ax.set_ylim([-1, 1])
        self._ax.set_zlim([-1, 1])

        self._ax.set_box_aspect([1, 1, 1])

        self._ax.set_xticks([])
        self._ax.set_yticks([])
        self._ax.set_zticks([])


    def delete_artifacts(self) :

        # Remove the following artifacts from the plot;
        #
        #   - lines of longitude
        #   - lines of latitude
        #   - surface of spherve

        if self._handle_wireframe is not None :

            self._handle_wireframe.remove()
            self._handle_wireframe = None

        for handles_list in self._handles_lines_longitude :

            for handle in handles_list :

                handle.remove()

        self._handles_lines_longitude.clear()

        for handles_list in self._handles_lines_latitude :

            for handle in handles_list :

                handle.remove()

        self._handles_lines_latitude.clear()

        if self._handle_surface is not None:

            self._handle_surface.remove()
            self._handle_surface = None


    # Invoked by : External clients
    #
    #   > This is a public method.

    def plot(self,

        radius,
        color_sphere_surface
    ) :

        """
        Plot a shaded sphere with latitude and longitude grid lines
        and save the result as a PNG file.

        Parameters
        ----------
        radius : float
            Radius of the sphere.

        surface_color : str
            Matplotlib-compatible color for the sphere surface.

        filename : str
            Name of the PNG file to create.

        num_latitudes : int
            Number of horizontal (latitude) grid lines.

        num_longitudes : int
            Number of vertical (longitude) grid lines.

        surface_resolution : int
            Resolution of the shaded sphere surface.

        grid_resolution : int
            Number of points used to draw each grid line.
        """

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self._radius               = radius
        self._color_sphere_surface = color_sphere_surface

        print(nameMethod + "////////////////////////////////////////")
        print(nameMethod + "////////////////////////////////////////")
        print(nameMethod + " : radius = " + str(radius))
        print(nameMethod + "////////////////////////////////////////")
        print(nameMethod + "////////////////////////////////////////")

        # Only proceed if all the necessary attributes are set.

        if (
            (self._radius             == None) or
            (self._surface_resolution == None) or
            (self._grid_resolution    == None) or
            (self._num_latitudes      == None) or
            (self._num_longitudes     == None)
        ) :

            raise Exception("Not all attributes are set.")

        # - Create the shaded surface of the sphere
        # - Draw horizontal latitude lines
        # - Draw vertical longitude lines
        # - Set the coordinate system
        # - Save the figure

        self.__setup_values()
        self.__plot_surface_and_grid_lines()
        self.__setup_plot_environment()


    # Invoked by : _configure

    def _plot_unit_sphere(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        # ----------------------------
        # Plot the unit sphere.
        # ----------------------------

        u = np.linspace(0, 2 * np.pi, 100)
        v_sphere = np.linspace(0, np.pi, 100)

        x = np.outer(np.cos(u), np.sin(v_sphere))
        y = np.outer(np.sin(u), np.sin(v_sphere))
        z = np.outer(np.ones_like(u), np.cos(v_sphere))

        # ax.plot_surface(
        #     x, y, z,
        #     alpha=0.25,
        #     linewidth=0,
        #     antialiased=True
        # )

        # ax.plot_wireframe(
        #     x, y, z,
        #     color='gray',
        #     linewidth=0.5,
        #     alpha=0.5,
        #     rstride=5,
        #     cstride=5
        # )

        hue_value = 0.5

        rgb_value = colorsys.hsv_to_rgb(

            hue_value,  # hue (0–1)
            1.0,  # saturation
            1.0  # value
        )

        self._axis.plot_surface(
            x, y, z,
            color=rgb_value,
            alpha=0.2,
            linewidth=0
        )

        if True :

            self._axis.plot_wireframe(
                x, y, z,
                color='black',
                linewidth=0.4,
                rstride=4,
                cstride=4
            )

        print(nameMethod + " : Exit")


    def _clear_sphere_wire_frame(self) :

        if self._plot_handle_sphere_wire_frame is not None :

            self._plot_handle_sphere_wire_frame.remove()
            self._plot_handle_sphere_wire_frame = None


    # Invoked by : PlottingAgent::_plot_unit_sphere_quaternion_pre_multiply

    def _clear_sphere_surface(self):

        if self._plot_handle_sphere_surface is not None :

            self._plot_handle_sphere_surface.remove()
            self._plot_handle_sphere_surface = None

