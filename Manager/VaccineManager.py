
from collections import defaultdict


class VaccineManager:
    user_map = defaultdict()
    centre_map = defaultdict()

    def get_centres(self, vaccine_type):
        centres = []
        response = []
        for key, centre in self.centre_map.items():
            if centre.vaccine_inventories.get(vaccine_type) != 0:
                centres.append(centre)

        # centres.sort()  please write the comparator and use cmp_to_key to sort (see problem statement about how to sort)
        for centre in centres:
            response.append("{}-{}".format(
                centre.centre_id,
                centre.get_vaccine_available_count(vaccine_type)
            ))

        return response

    @classmethod
    def book_slot(cls, user_name, centre_id):
        user = cls.user_map.get(user_name)
        if not user:
            return "User not registered. Please register the user"

        centre = cls.centre_map.get(centre_id)
        if not centre:
            return "Centre not registered. try some other centre"

        vaccine_type = user.preferred_vaccine_type
        if centre.get_vaccine_available_count(vaccine_type) <= 0:
            return "no vaccine available at this centre"

        response = centre.make_booking(user)
        cls.centre_map[centre_id] = centre
        return response

    @classmethod
    def register_centre(cls, centre):
        if cls.centre_map.get(centre.centre_id):
            return "centre already registered"

        cls.centre_map[centre.centre_id] = centre
        return "successfully registered centre"

    @classmethod
    def register_user(cls, user):
        if cls.user_map.get(user.name):
            return "User already registered"

        cls.user_map[user.name] = user
        return "user registered successfully"

    @classmethod
    def get_stats(cls):
        # stats to show how many users registered for each vaccine type
        # check the requirements in the problem statement
        pass




