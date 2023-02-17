from app.models.resources.resources_base import Resource
from app.utils.validators.validate_integer import validate_integer


class CPU(Resource):
    """Resource subclass used to track specific CPU inventory pools"""

    def __init__(
            self, name, manufacturer, total, allocated,
            cores, socket, power_watts
    ):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            cores (int): number of cores
            socket (str): CPU socket type
            power_watts (int): CPU rated wattage
        """
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        """
        Number of cores.

        Returns:
            int
        """
        return self._cores

    @property
    def socket(self):
        """
        The socket type for this CPU
        Returns:
            str
        """
        return self._socket

    @property
    def power_watts(self):
        """
        The rated wattage of this CPU

        Returns:
            int
        """
        return self._power_watts

    def __repr__(self):
        return super().__repr__()
