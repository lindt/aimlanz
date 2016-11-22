#!/usr/bin/env python2
import aiml

kernel = aiml.Kernel()

def learn(path):
    kernel.learn('aiml-en-us-foundation-alice/{0}'.format(path))

import glob
for path in sorted(glob.glob('aiml-en-us-foundation-alice/first/*.aiml')):
    kernel.learn(path)
for path in sorted(glob.glob('aiml-en-us-foundation-alice/second/*.aiml')):
    kernel.learn(path)
for path in sorted(glob.glob('aiml-en-us-foundation-alice/third/*.aiml')):
    kernel.learn(path)
kernel.learn('allianz.aiml')

def personal_offers(session):
  result = []
  if 'car' in session:
    result.append('A car insurance')
  if 'dog' in session:
    if 'dog race' in session:
      if session['dog race'] == 'Pitbull':
        result.append('A car insurance including a person insurance')
      else:
        result.append('A dog insurance for your {0}'.format(session['dog race']))
    else:
      result.append('A generic dog insurance,but we can tailor it to your need if you tell us your dogs race.')
  return result

sessionId = 23
while True:
    print kernel.respond(raw_input('Enter your message >> '), sessionId)
    session = kernel.getSessionData(sessionId)
    offers = personal_offers(session)
    discount = 5 * len(offers)
    offers = '\n'.join(offers) if offers != [] else 'None yet. Please tell me something about you. Do you have a Dog?'
    kernel.setPredicate('personal offers', offers, sessionId)
    kernel.setPredicate('personal discount', str(discount), sessionId)
