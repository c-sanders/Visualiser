import sys
import logging


logger = logging.getLogger(__name__)


def format_component(

        name,
        space,
        value
) :
    nameMethod = "::" + str(sys._getframe().f_code.co_name)


    logger.debug(nameMethod + " : Enter")

    logger.debug(nameMethod + " : name  = " + str(name))
    logger.debug(nameMethod + " : space = " + str(space))
    logger.debug(nameMethod + " : value = " + str(value))

    if value == 0 :

        logger.debug(nameMethod + " : MARKER 0")

        if space :

            return f"+ {name}{abs(value):.3f}"

        else :

            logger.debug(nameMethod + " : MARKER 0A")

            return_value = f"+{name}{abs(value):.3f}"

            logger.debug(nameMethod + " : return_value = " + str(return_value))

            return return_value

    elif value < 0 :

        if space :

            return f"- {name}{abs(value):.3f}"

        else :

            return f"-{name}{abs(value):.3f}"

        logger.debug(nameMethod + " : MARKER 1")

    else :

        if space :

            return f"+ {name}{value:.3f}"

        else :

            return f"+{name}{value:.3f}"

        logger.debug(nameMethod + " : MARKER 2")

    logger.debug(nameMethod + " : Exit")


def generate_string(

        scalar_value,
        i_value,
        j_value,
        k_value
) :

    label  = f"{format_component("",  False, scalar_value)} "
    label += f"{format_component('i', True,  i_value)} "
    label += f"{format_component('j', True,  j_value)} "
    label += f"{format_component('k', True,  k_value)}"

    return label