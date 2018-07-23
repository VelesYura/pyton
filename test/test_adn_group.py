# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_adn_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Name", header="header", footer="footer"))
    app.session.logout()


def test_adn_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

