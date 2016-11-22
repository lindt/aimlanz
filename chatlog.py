#!/usr/bin/env python2
from aimlanz import Aimlanz

aimlanz = Aimlanz()

def ask(question):
    print('\n\nAsking: {0}'.format(question))
    answer = aimlanz.ask(question)
    print(answer)

ask('Hi.')
ask('My dogs name is Mike.')
ask('What insurances do you have?')
ask('My dog is a Pitbull')
ask('What insurances do you have?')
ask('I have a car from BMW')
ask('What insurances do you have?')
