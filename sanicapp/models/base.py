# -*- coding: utf-8 -*-

from gino import Gino
from gino.dialects.asyncpg import NullPool

db = Gino()
create_engine('postgresql://...', pool_class=NullPool)