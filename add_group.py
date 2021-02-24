# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
from application import Application

class Task1(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(name="admin", password="secret")
        self.app.create_group(Group(name="task_1", header="test", footer="test"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(name="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
