# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_adn_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Name", header="header", footer="footer"))
    app.logout()


def test_adn_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

