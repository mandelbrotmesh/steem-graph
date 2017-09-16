#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `steem_graph` package."""

import pytest
from steem_graph import database

def test_setupdb():
    database.setup_user_database()

def test_createuser():
    database.create_user("marnee")

def test_getusercount():
    database.get_user_count()
    