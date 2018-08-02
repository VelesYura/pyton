# -*- coding: utf-8 -*-

from model.group import Group


def test_adn_group(app):
    app.group.create(Group(name="Name", header="header", footer="footer"))


def test_adn_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

