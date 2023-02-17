"""Inventory models"""


from app.utils.validators.validate_integer import validate_integer


class Resource:
    """Base class for resources"""

    def __init__(self, name, manufacturer, total, allocated):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources

        Note:
            `allocated` cannot exceed `total`
        """
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message='Allocated inventory cannot exceed total inventory'
        )
        self._allocated = allocated

    @property
    def name(self):
        """

        Returns:
            str: the resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """

        Returns:
            str: the resource manufacturer
        """
        return self._manufacturer

    @property
    def total(self):
        """

        Returns:
            int: the total inventory count
        """
        return self._total

    @property
    def allocated(self):
        """

        Returns:
            int: number of resources in use
        """
        return self._allocated

    @property
    def category(self):
        """

        Returns:
            str: the resource category
        """
        return type(self).__name__.lower()

    @property
    def available(self):
        """

        Returns:
            int: number of resources available for use
        """
        return self.total - self.allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f'{self.name} ({self.category} - {self.manufacturer}) : '
                f'total={self.total}, allocated={self.allocated}'
                )

    def claim(self, num):
        """
        Claim num inventory items (if available)

        Args:
            num (int): Number of inventory items to claim

        Returns:

        """
        validate_integer(
            'num', num, 1, self.available,
            custom_max_message='Cannot claim more than available'
        )
        self._allocated += num

    def freeup(self, num):
        """
        Return an inventory item to the available pool

        Args:
            num (int): Number of items to return (cannot exceed number in use)

        Returns:

        """
        validate_integer(
            'num', num, 1, self.allocated,
            custom_max_message='Cannot return more than allocated'
        )
        self._allocated -= num

    def died(self, num):
        """
        Number of items to deallocate and remove from the inventory pool
        altogether

        Args:
            num (int): Number of items that have died

        Returns:

        """
        validate_integer('num', num, 1, self.allocated,
                         custom_max_message='Cannot retire more than allocated')
        self._total -= num
        self._allocated -= num

    def purchased(self, num):
        """
        Add new inventory to the pool.

        Args:
            num (int): Number of items to add to the pool

        Returns:

        """
        validate_integer('num', num, 1)
        self._total += num


