from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name = "not stated", calories = 0, flavor = "tasteless"):
        super().__init__(name, calories)
        if isinstance(flavor, str) and flavor:
            self._flavor = flavor
        else:
            self._flavor = "tasteless"
            Dessert.warn(flavor)

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, new_value):
        if isinstance(new_value, str) and new_value:
            self._flavor = new_value
        else:
            Dessert.warn(new_value, reset = False)
    
    def is_delicious(self):
        return self._flavor.lower().strip() != "black licorice"

