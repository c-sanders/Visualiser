import sys
import logging

import numpy as np
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)


# This class contains the following public methods;
#
#   - __init__
#   - configure
#   - delete_artifacts
#   - set_plot_grid_lines
#   - clear_plot_grid_lines
#   - plot


class UnitSphere :

    def __init__(self,

        sub_plot_agent : SubPlotAgent,
        axis_plot
    ) :

        self.file_log                 = open("logs/UnitSphere.log", "w", buffering=1)
        self.file_log_radius          = open("logs/UnitSphere_radius.log", "w", buffering=1)

        self._plot_lines_sphere_surface = True

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

        self._plot_handle_sphere_wire_frame        = None

        self._handles_lines_latitude  = []
        self._handles_lines_longitude = []

        self._plot_handle_sphere_wire_frame = None
        self._plot_handle_sphere_surface    = None

        self._filename                = None


    def configure(self,

        display_plot_lines_sphere_surface = True,

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

    def _setup_values(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        print(nameMethod + " : Enter")

        print(nameMethod + " : ////////////////////////////////////////")
        print(nameMethod + " : ////////////////////////////////////////")
        print(nameMethod + " : self._radius = " + str(self._radius))
        print(nameMethod + " : ////////////////////////////////////////")
        print(nameMethod + " : ////////////////////////////////////////")

        self.file_log_radius.write(nameMethod + " : radius = " + str(self._radius * 0.5) + "\n")

        u = np.linspace(0, 2 * np.pi, self._surface_resolution)
        v = np.linspace(0,     np.pi, self._surface_resolution)

        u, v = np.meshgrid(u, v)

        self._x = self._radius * np.sin(v) * np.cos(u)
        self._y = self._radius * np.sin(v) * np.sin(u)
        self._z = self._radius * np.cos(v)

        print(nameMethod + " : Exit")


    def _plot_sphere_surface(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self.file_log.write(nameMethod + " : self._plot_handle_sphere_wire_frame = " + str(self._plot_handle_sphere_wire_frame) + "\n")

        if self._handle_surface is not None:

            self._handle_surface.remove()
            self._handle_surface = None

        if self._handle_surface is None:

            self.file_log.write(nameMethod + " : About to create a surface for the sphere\n")

            if True:

                self._handle_surface = self._ax.plot_surface(

                    self._x,
                    self._y,
                    self._z,
                    color=self._color_sphere_surface,
                    alpha=0.2,
                    shade=True,
                    linewidth=0,
                    antialiased=True
                )

                self.file_log.write(nameMethod + " : self._handle_surface = " + str(self._handle_surface) + "\n")

                self._handle_surface.set_color(self._color_sphere_surface)


    def _plot_sphere_lines_lat_long(self):

        # The latitude and longitude lines are dependent upon the value of the sphere's radius. As a result, we should
        # delete any of them which are currently associated with the plot.

        if self._handles_lines_latitude:

            for line in self._handles_lines_latitude:

                line.remove()

            self._handles_lines_latitude.clear()

        if self._handles_lines_longitude:

            for line in self._handles_lines_longitude:

                line.remove()

            self._handles_lines_longitude.clear()

        self._plot_latitude_lines_on_sphere()
        self._plot_longitude_lines_on_sphere()


    def _plot_sphere_lines_wireframe(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self.file_log.write(nameMethod + " : self._plot_handle_sphere_wire_frame = " + str(self._plot_handle_sphere_wire_frame) + "\n")

        # The radius of the unit sphere might have changed, so remove the unit sphere wireframe from the plot.

        self._clear_sphere_wire_frame()

        if self._plot_handle_sphere_wire_frame is None:

            if self._plot_lines_sphere_surface:

                self.file_log.write(nameMethod + " : About to create a wireframe for the sphere\n")

                self._plot_handle_sphere_wire_frame = self._ax.plot_wireframe(

                    self._x,
                    self._y,
                    self._z,
                    color='black',
                    linewidth=0.4,
                    rstride=4,
                    cstride=4
                )

            self.file_log.write(nameMethod + " : self._plot_handle_sphere_wire_frame = " + str(self._plot_handle_sphere_wire_frame) + "\n")

        self.file_log_radius.write(nameMethod + " : Exit\n")


    def _plot_sphere_lines(self):

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self._plot_lines_sphere_surface = True

        # Use one or the other of the following; don't use both.
        #
        # I actually think the wireframe looks better.

        if False:

            # self._plot_sphere_lines_lat_long()

            pass

        else:

            self._plot_sphere_lines_wireframe()


    def _plot_sphere_surface_and_lines(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        self.file_log.write(nameMethod + " : Enter\n")
        self.file_log_radius.write(nameMethod + " : Enter\n")

        # self._plot_unit_sphere

        self._plot_sphere_surface()
        self._plot_sphere_lines()

        self.file_log.write(nameMethod + " : Exit\n")


    def _plot_latitude_lines_on_sphere(self) :

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

            self._handles_lines_latitude.extend(

                self._ax.plot(

                    x_line,
                    y_line,
                    z_line,
                    color="black",
                    linewidth=0.8
                )
            )


    def _plot_longitude_lines_on_sphere(self) :

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


        for longitude in longitudes:

            x_line = self._radius * np.cos(latitude) * np.cos(longitude)
            y_line = self._radius * np.cos(latitude) * np.sin(longitude)
            z_line = self._radius * np.sin(latitude)

            self._handles_lines_longitude.extend(

                self._ax.plot(

                    x_line,
                    y_line,
                    z_line,
                    color="black",
                    linewidth=0.8
                )
            )


    def _setup_plot_environment(self) :

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

        pass

        # Remove the following artifacts from the plot;
        #
        #   - lines of longitude
        #   - lines of latitude
        #   - surface of sphere

        # Don't keep deleting the sphere's wireframe. ChatGPT advises against it.

        # if self._plot_handle_sphere_wire_frame is not None :

        #     self._plot_handle_sphere_wire_frame.remove()
        #     self._plot_handle_sphere_wire_frame = None

        # for handles_list in self._handles_lines_longitude:
        #
        #     for handle in handles_list :
        #
        #         handle.remove()

        # self._handles_lines_longitude.clear()

        # for handles_list in self._handles_lines_latitude :
        #
        #     for handle in handles_list :
        #
        #         handle.remove()

        # self._handles_lines_latitude.clear()

        # if self._handle_surface is not None:
        #
        #     self._handle_surface.remove()
        #     self._handle_surface = None


    def set_plot_lines_sphere_surface(self):

        self._plot_lines_sphere_surface = True


    def clear_plot_lines_sphere_surface(self):

        self._plot_lines_sphere_surface = False


    # Invoked by : External clients
    #
    #   > This is a public method.

    def plot(self,

        radius,
        color_sphere_surface
    ) :

        """
        Generate a plot of a shaded sphere with latitude and longitude grid lines.

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

        # The value of the radius may have changed. As a result, we should play it safe and re-calculate the values for;
        #
        #   - self._x
        #   - self._y
        #   - self._z

        self._setup_values()
        self._plot_sphere_surface_and_lines()
        self._setup_plot_environment()


    # Invoked by : _configure

    def _plot_unit_sphere(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

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

        logger.debug(nameMethod + " : Exit")


    def _clear_sphere_wire_frame(self) :

        if self._plot_handle_sphere_wire_frame is not None :

            self._plot_handle_sphere_wire_frame.remove()
            self._plot_handle_sphere_wire_frame = None


    # Invoked by : PlottingAgent::_plot_unit_sphere_quaternion_pre_multiply

    def _clear_sphere_surface(self):

        if self._plot_handle_sphere_surface is not None :

            self._plot_handle_sphere_surface.remove()
            self._plot_handle_sphere_surface = None

