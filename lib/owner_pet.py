class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} not in pet types")
        self.name = name
        self._pet_type = pet_type
        self._owner = None
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{new_pet_type} not in pet types")
        self._pet_type = new_pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if self._owner is not None:
            self._owner._pets.remove(self)
        self._owner = new_owner
        if new_owner is not None:
            new_owner._pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, new_pet):
        if not isinstance(new_pet, Pet):
            raise ValueError("The pet must be an instance of Pet")
        new_pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name.lower())
