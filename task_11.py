class Dessert:

    @staticmethod
    def warn(invalid, reset = True):
        if reset:
            print(f"invalid input '{invalid}', value set to default")
        else:
            print(f"invalid input '{invalid}', old value remains")

    def __init__(self, name = "not stated", calories = 0):
        if isinstance(name, str) and name:
            self._name = name
        else:
            self._name = "not stated"
            Dessert.warn(name)

        if isinstance(calories, (int,float)) and calories >= 0:
            self._calories = calories
        else:
            self._calories = 0
            Dessert.warn(calories)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value,str) and new_value:
            self._name = new_value
        else:
            Dessert.warn(new_value, reset=False)

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, new_value):
        if isinstance(new_value, (int,float, str)):
            self._calories = new_value
        else:
            Dessert.warn(new_value, reset=False)

    def is_healthy(self):
        
        if isinstance(self._calories, (int,float)):
            return self._calories < 200

    def is_delicious(self):
        return True
    
