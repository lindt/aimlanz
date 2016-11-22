#!/usr/bin/env python2
import aiml


class Aimlanz:

    def __init__(self):
        self.kernel = aiml.Kernel()
        self.session_id = 42
        import glob

        for level in ['first', 'second', 'third']:
            for path in sorted(glob.glob('aiml-en-us-foundation-alice/{0}/*.aiml'.format(level))):
                self.kernel.learn(path)
        self.kernel.learn('allianz.aiml')

    def learn(self, path):
        self.kernel.learn(path)

    def ask(self, question):
        answer = self.kernel.respond(question, self.session_id)
        session = self.kernel.getSessionData(self.session_id)
        offers = self.personal_offers(session)
        discount = 5 * len(offers)
        offers = '\n'.join(offers) if offers != [] else 'None yet. Please tell me something about you. Do you have a Dog?'
        self.kernel.setPredicate('personal offers', offers, self.session_id)
        self.kernel.setPredicate('personal discount', str(discount), self.session_id)

        return answer

    @staticmethod
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
