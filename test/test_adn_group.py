# -*- coding: utf-8 -*-

from model.group import Group


def test_adn_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Name", header="header", footer="footer"))
    app.session.logout()


def test_adn_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

