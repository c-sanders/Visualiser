import sys
import colorsys
import logging


logger = logging.getLogger(__name__)


class ColorAgent :

    def __init__(self) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        self.__rgb_value_current = None
        self.__rgb_value_minimum = None
        self.__rgb_value_maximum = None

        logger.debug(nameMethod + " : Exit")


    def _compute_rgb_value(self,

        value
    ) :

        hue_value = (value * (0.5 / 0.577)) + 0.5

        rgb_value = colorsys.hsv_to_rgb(

            hue_value,  # hue (0–1)
            1.0,        # saturation
            1.0         # value
        )

        return rgb_value

    def update_rgb_value_current(self,

        value
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Set the current RGB value.

        self.__rgb_value_current = self._compute_rgb_value(value)

        logger.debug(nameMethod + " : Exit")


    def update_rgb_value_minimum(self,

        value
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Set the minimum RGB value.

        self.__rgb_value_minimum = self._compute_rgb_value(value)

        logger.debug(nameMethod + " : Exit")


    def update_rgb_value_maximum(self,

        value
    ) :

        nameMethod = str(self.__class__.__name__) + "::" + str(sys._getframe().f_code.co_name)


        logger.debug(nameMethod + " : Enter")

        # Set the maximum RGB value.

        self.__rgb_value_maximum = self._compute_rgb_value(value)

        logger.debug(nameMethod + " : Exit")


    def get_rgb_value_current(self) :

        return self.__rgb_value_current


    def get_rgb_value_minimum(self) :

        return self.__rgb_value_minimum


    def get_rgb_value_maximum(self) :

        return self.__rgb_value_maximum