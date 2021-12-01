# -*- coding: utf-8 -*-
import json
import os
from src.common import read_config_file
from src.db import run_update
from src.templates import db_query as dbq


def create_user(count):
    user_list = ['TU_' + str(u) for u in range(int(count))]
    password_list = ['TuPass_' + str(u) for u in range(int(count))]
    email_list = ['TU' + str(u) + '@test.com' for u in range(int(count))]

    return user_list, password_list, email_list


def prepare_user_query(ul, pl, el):
    tmp = ''
    for u, p, e in zip(ul, pl, el):
        tmp += f"('{u}', '{p}', '{e}'),"

    return dbq.ADD_USER.value + tmp[0:-1] + ';'


def create_recipes(uid, count, rt, ip):
    # name | user_id | recipes_type | is_public
    r_name = ['recipes_' + str(r) + '_' + str(uid) for r in range(int(count))]
    tmp = ''
    for rn in r_name:
        tmp += f" ('{rn}', {uid}, {rt}, '{ip}'),"
    run_update(dbq.ADD_RECIPES.value + tmp[0:-1] + ';')


class mock:

    def mock_users(self, count):
        # name | password |    email
        ul, pl, el = create_user(count)
        run_update(prepare_user_query(ul, pl, el))

    def mock_recipes(self, conf):
        # name | user_id | recipes_type | is_public
        for r in read_config_file(conf)['recipes']:
            create_recipes(r['user_id'], r['recipes_count'], r['recipes_type'], r['public'])

    def mock_recipes_details(self):
        # recipes_id | ming_id | weight
        pass

    def mock_ming(self):
        # name
        pass

    def mock_steps(self):
        # recipes_id | s_number | s_desc
        pass

