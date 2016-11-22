#!/usr/bin/env python2
from aimlanz import Aimlanz

aimlanz = Aimlanz()

while True:
    print(aimlanz.ask(raw_input('Enter your message >> ')))
