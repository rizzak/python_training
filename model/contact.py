class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home_tel=None, mobile_tel=None,
                       work_tel=None, fax=None, e_mail=None, homepage=None, birthday=None, anniversary=None, secondary_address=None, home=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.e_mail = e_mail
        self.homepage = homepage
        self.birthday = birthday
        self.anniversary = anniversary
        self.secondary_address = secondary_address
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name
