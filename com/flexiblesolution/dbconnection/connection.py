from datetime import datetime

from pony import *
from pony.orm import Database, PrimaryKey, Required, db_session, Optional, Set, set_sql_debug

from com.flexiblesolution.model.submitcasemodel import getSubmitCase
from com.flexiblesolution.model.usermodel import getUser

db = Database()

db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='postgres')
user_class = getUser(db)
submit_case_class = getSubmitCase(db,user_class)
#test

set_sql_debug(True)
db.generate_mapping(create_tables=True)
