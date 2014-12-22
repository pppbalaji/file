"""
Staging environment
"""

config = {
    'debug': True,

    'session.cookie_domain': None,

    'auth.secret.password': 'foo',
    'auth.secret.reset': 'bar',

    'email.sender': 'RatedApartments <bounce@staging2-ratedapartments.appspotmail.com>',

    'cloudsearch.enabled': False,

    'hsbc.mode': 'Y',

    'analytics.enabled': False,

    'olark.enabled': False,

    'kigo.enabled': False,

    'robots.enabled': False,

    'app.domain': 'staging2-ratedapartments.appspot.com',
    'app.domain.secure': None,

    'app.order.card': None
}
