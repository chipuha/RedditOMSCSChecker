#!/usr/bin/env python

redinst = {'user_agent':'funfunsearch',
           'client_id':'oTDwExc6dEbs2Q',
           'client_secret':'c9gkK9bvnKFZ7C609ofoUX_z_Qk',
           'username':'chipuha',
           'password':'P1n3appl3'}
           
preprocessing_queue = [
    preprocessing.scale_and_center,
    preprocessing.dot_reduction,
    preprocessing.connect_lines,
]
use_anonymous = True
