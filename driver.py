

from models import (
    User,
    VaccineType,
    Centre
)
from Manager import VaccineManager

if __name__ == "__main__":
    user1 = User('vikas', 'M', 'covaxin')
    user2 = User('rahul', 'M', 'covishield')
    user3 = User('ankit', 'M', 'covishield')
    user4 = User('veena', 'M', 'covishield')

    inventory1 = {
        VaccineType.COVAXIN: 2,
        VaccineType.COVISHIELD: 2
    }
    centre1 = Centre('centre1', inventory1)
    inventory2 = {
        VaccineType.COVAXIN: 1,
        VaccineType.COVISHIELD: 1

    }
    centre2 = Centre('centre2', inventory2)
    vaccine_manager = VaccineManager()

    print(vaccine_manager.register_user(user1))
    print(vaccine_manager.register_user(user3))
    print(vaccine_manager.register_user(user4))
    vaccine_manager.register_user(user2)
    print(vaccine_manager.register_user(user2))
    print(vaccine_manager.register_centre(centre1))
    print(vaccine_manager.register_centre(centre2))

    print(vaccine_manager.get_centres(user1.preferred_vaccine_type))
    print(vaccine_manager.book_slot("vikas", "centre1"))
    print(vaccine_manager.book_slot("rahul", "centre1"))
    print(vaccine_manager.book_slot("vikas", "centre1"))
    print(vaccine_manager.book_slot("ankit", "centre1"))
    print(vaccine_manager.book_slot("veena", "centre1"))
    print(vaccine_manager.get_stats())
    # vaccine_manager.book_slot(user2)
    # todo - book slot get stats
    # for key, value in vaccine_manager.centre_map.items():
    #     print(vaccine_manager.centre_map[key].vaccine_inventories)

