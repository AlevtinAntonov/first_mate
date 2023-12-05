from app_model.db.db_query import query_insert_into, address, DB_DICT


class Address:
    def __init__(self, zipcode: str = None, region: str = None, district: str = None, town: str = None,
                 locality: str = None, street: str = None, house: str = None, house_body: str = None,
                 house_liter: str = None, house_building: str = None, flat: str = None, is_registration: bool = False,
                 is_fact: bool = False, is_residence: bool = False, address_type_id: int = None,
                 region_type_id: int = None, town_type_id: int = None, locality_type_id: int = None,
                 street_type_id: int = None, is_visible: bool = False):
        self.zipcode = zipcode
        self.region = region
        self.district = district
        self.town = town
        self.locality = locality
        self.street = street
        self.house = house
        self.house_body = house_body
        self.house_liter = house_liter
        self.house_building = house_building
        self.flat = flat
        self.is_registration = is_registration
        self.is_fact = is_fact
        self.is_residence = is_residence
        self.address_type_id = address_type_id
        self.locality_type_id = locality_type_id
        self.town_type_id = town_type_id
        self.region_type_id = region_type_id
        self.street_type_id = street_type_id
        self.is_visible = is_visible

    def save_address(self, db):
        query = query_insert_into(address) % DB_DICT[address]
        with db as cur:
            cur.execute(query,
                        (self.address_type_id, self.zipcode, self.region, self.region_type_id, self.district, self.town,
                         self.town_type_id, self.locality, self.locality_type_id, self.street, self.street_type_id,
                         self.house, self.house_body, self.house_liter, self.house_liter, self.house_building,
                         self.flat, self.is_registration, self.is_fact, self.is_residence))

    def print_address(self):
        print(self.address_type_id, self.zipcode, self.region, self.region_type_id, self.district, self.town,
              self.town_type_id, self.locality, self.locality_type_id, self.street, self.street_type_id,
              self.house, self.house_body, self.house_liter, self.house_liter, self.house_building,
              self.flat, self.is_registration, self.is_fact, self.is_residence)
