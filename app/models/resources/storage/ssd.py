from app.models.resources.storage.storage import Storage
from app.utils.validators.validate_integer import validate_integer


class SSD(Storage):
    """
    Class used for SSD type resources
    """
    def __init__(
            self, name, manufacturer, total, allocated, capacity_gb,
            interface
    ):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            interface (str): indicates the device interface (e.g. PCIe NVMe 3.0 x4)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        self._interface = interface

    @property
    def interface(self):
        """
        Interface used by SSD (e.g. PCIe NVMe 3.0 x4)

        Returns:
            str
        """
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return s