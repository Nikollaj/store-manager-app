from app.models.resources.storage.storage import Storage
from app.utils.validators.validate_integer import validate_integer


class HDD(Storage):
    """
    Class used for HDD type resources
    """
    def __init__(
            self, name, manufacturer, total, allocated, capacity_gb,
            size, rpm
    ):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            size (str): indicates the device size (must be either 2.5" or 3.5")
            rpm (int): disk rotation speed (in rpm)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        allowed_sizes = ["2.5'", "3.5'"]
        if size not in allowed_sizes:
            raise ValueError(f'Invalid HDD size. '
                             f'Must be one of {", ".join(allowed_sizes)}')
        validate_integer('rpm', rpm, min_value=1000, max_value=50000)

        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        The HDD size (2.5" / 3.5")

        Returns:
            str
        """
        return self._size

    @property
    def rpm(self):
        """
        The HDD spin speed (rpm)

        Returns:
            int
        """
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'
