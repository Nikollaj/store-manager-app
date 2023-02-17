from app.models.resources.resources_base import Resource
from app.utils.validators.validate_integer import validate_integer


class Storage(Resource):
    """
    A base class for storage devices - probably not used directly
    """

    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
        """
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Indicates the capacity (in GB) of the storage device

        Returns:
            int
        """
        return self._capacity_gb

    def __repr__(self):
        return super().__repr__()

