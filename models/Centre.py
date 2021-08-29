from collections import defaultdict


class Centre:
    def __init__(self, centre_id, vaccine_inventories):
        self.centre_id = centre_id
        self.vaccine_inventories = vaccine_inventories
        self.booking = defaultdict()
        self.number_of_bookings = 0

    def make_booking(self, user):
        vaccine_type = user.preferred_vaccine_type
        if self.booking.get(vaccine_type) and user in self.booking.get(vaccine_type):
            return "user already booked for vaccine"

        self.vaccine_inventories[vaccine_type] -= 1
        self.number_of_bookings += 1
        if not self.booking.get(vaccine_type):
            self.booking[vaccine_type] = [user]
        else:
            self.booking[vaccine_type].append(user)

        return "successfully booked"

    def get_vaccine_available_count(self, vaccine_type):
        return self.vaccine_inventories.get(vaccine_type)
