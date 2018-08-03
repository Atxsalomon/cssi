#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):

        def __init__(self, lable, balance):
            self.lable = lable
            self.balance = balance
        def __str__(self):
            return'Acount Name: {Name}\nCurrent Balance:.{balance}' .format(
                name=self.lable, balance=self.balance)
        def withdrawl(self, amount):
            amount <= self.balance and amount > 0:
            self.balance = self.balance - amount
        def deposit(self, amount):
            if amount > 0:
            self.balance= self.balance + amount
        def rename(self, name):
            if name != '':
                self.lable = name
        def transfer (self, otheract, amount):
            if amount > 0 and self.balance >= otheract.balance:
                self.balance = self.balance - amount
                otheract.balance = otheract.balance + amount
