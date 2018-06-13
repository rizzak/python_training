import jsonpickle
import random
import string
from model.contact import Contact
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                    home_tel="", mobile_tel="", work_tel="", fax="", email="", homepage="", birthday="",
                    anniversary="", secondary_address="", secondary_tel="", notes="")] + [
    Contact(first_name=random_string('first_name', 10), middle_name=random_string('middle_name', 10), last_name=random_string('last_name', 10),
            nickname=random_string('nickname', 10), title=random_string('random_string', 10), company=random_string('company', 10),
            address=random_string('address', 10), home_tel=random_string('home_tel', 10), mobile_tel=random_string('mobile_tel', 10),
            work_tel=random_string('work_tel', 10), fax=random_string('fax', 10), email=random_string('email', 10),
            homepage=random_string('homepage', 10), birthday=random_string('birthday', 10), anniversary=random_string('anniversary', 10),
            secondary_address=random_string('secondary_address', 10), secondary_tel=random_string('secondary_tel', 10), notes=random_string('notes', 10))
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file , "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))