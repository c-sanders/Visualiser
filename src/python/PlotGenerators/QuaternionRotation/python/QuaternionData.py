import sys
import logging


logger = logging.getLogger(__name__)


class QuaternionData :

    def __init__(self) :

        # Attributes which pertain to the quaternion rotation.
        #
        # These are local copies of externally generated data.

        self.quaternion_axis_rotation    = None
        self.quaternion_to_rotate        = None
        self.quaternion_pre_multiply     = None
        self.quaternion_rotated          = None

        self.quaternion_pre_multiply_min = None
        self.quaternion_pre_multiply_max = None

        # Component arrays to hold the history of the rotated vector.

        self.quaternion_pre_multiply_w_components = []
        self.quaternion_pre_multiply_x_components = []
        self.quaternion_pre_multiply_y_components = []
        self.quaternion_pre_multiply_z_components = []

        self.quaternion_rotated_w_components = []
        self.quaternion_rotated_x_components = []
        self.quaternion_rotated_y_components = []
        self.quaternion_rotated_z_components = []

        self.quaternion_pre_multiply_min_updated = False
        self.quaternion_pre_multiply_max_updated = False


    # Invoked by : External clients

    def set_quaternions_and_min_max_values(

        self,
        quaternion_axis_rotation,
        quaternion_to_rotate,
        quaternion_pre_multiply,
        quaternion_rotated
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Update the quaternion values.

        self.quaternion_axis_rotation = quaternion_axis_rotation
        self.quaternion_to_rotate     = quaternion_to_rotate
        self.quaternion_pre_multiply  = quaternion_pre_multiply
        self.quaternion_rotated       = quaternion_rotated

        self.__update_quaternion_pre_multiply_history()
        self.__update_quaternion_history()
        self.__update_min_max_values()

        # self._update_rgb_values()

        logger.debug(nameMethod + " : Exit")


    # Invoked by : set_quaternions_and_min_max_values

    def __update_quaternion_pre_multiply_history(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Add the point to the list of points.

        self.quaternion_pre_multiply_w_components.append(self.quaternion_pre_multiply.w)

        if len(self.quaternion_pre_multiply_w_components) == 1 :

            self._w_difference = self.quaternion_pre_multiply_w_components[0]

        elif len(self.quaternion_pre_multiply_w_components) >= 2 :

            self._w_difference = self.quaternion_pre_multiply_w_components[-1] - self.quaternion_pre_multiply_w_components[-2]

        else :

            raise Exception("Not enough values in the list.")

        logger.debug(nameMethod + " : {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
        logger.debug(nameMethod + " : {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
        logger.debug(nameMethod + " : self.w_difference = " + str(self._w_difference))
        logger.debug(nameMethod + " : }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
        logger.debug(nameMethod + " : }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")

        logger.debug(nameMethod + " : Exit")


    # Invoked by : set_quaternions_and_min_max_values

    def __update_quaternion_history(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Add the point to the list of points.

        self.quaternion_pre_multiply_w_components.append(self.quaternion_pre_multiply.w)
        self.quaternion_pre_multiply_x_components.append(self.quaternion_pre_multiply.x)
        self.quaternion_pre_multiply_y_components.append(self.quaternion_pre_multiply.y)
        self.quaternion_pre_multiply_z_components.append(self.quaternion_pre_multiply.z)

        self.quaternion_rotated_w_components.append(self.quaternion_rotated.w)
        self.quaternion_rotated_x_components.append(self.quaternion_rotated.x)
        self.quaternion_rotated_y_components.append(self.quaternion_rotated.y)
        self.quaternion_rotated_z_components.append(self.quaternion_rotated.z)

        logger.debug(f"Length self.w_components = {len(self.quaternion_rotated_w_components):d}")
        logger.debug(f"Length self.x_components = {len(self.quaternion_rotated_x_components):d}")
        logger.debug(f"Length self.y_components = {len(self.quaternion_rotated_y_components):d}")
        logger.debug(f"Length self.z_components = {len(self.quaternion_rotated_z_components):d}")

        logger.debug(nameMethod + " : self._plotting_agent.x_components = ")
        logger.debug(self.quaternion_rotated_x_components)
        logger.debug(nameMethod + " : self._plotting_agent.y_components = ")
        logger.debug(self.quaternion_rotated_y_components)
        logger.debug(nameMethod + " : self._plotting_agent.z_components = ")
        logger.debug(self.quaternion_rotated_z_components)

        logger.debug(nameMethod + " : Exit")


    # Invoked by : set_quaternions_and_min_max_values

    def __update_min_max_values(self) :

        # Check if the scalar component of qv has reached a new minimum.

        if (
            (self.quaternion_pre_multiply_min is None) or
            (self.quaternion_pre_multiply.w < self.quaternion_pre_multiply_min)
           ) :

            self.quaternion_pre_multiply_min_updated = True
            self.quaternion_pre_multiply_min          = self.quaternion_pre_multiply.w

        else :

            self.quaternion_pre_multiply_min_updated = False

        # Check if the scalar component of qv has reached a new maximum.

        if (
            (self.quaternion_pre_multiply_max is None) or
            (self.quaternion_pre_multiply.w > self.quaternion_pre_multiply_max)
           ) :

            self.quaternion_pre_multiply_max_updated = True
            self.quaternion_pre_multiply_max          = self.quaternion_pre_multiply.w

        else :

            self.quaternion_pre_multiply_max_updated = False


    def get_min_updated(self) :

        return self.quaternion_pre_multiply_min_updated


    def get_max_updated(self) :

        return self.quaternion_pre_multiply_max_updated