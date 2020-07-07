# For custom settings to go with the flex theme,
# see https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
from __future__ import unicode_literals

AUTHOR = 'Geert Barentsen'
SITENAME = 'Geert Barentsen'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Disable feed generation for all but 'all'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = [
    'extra',
    'images'
    ]
EXTRA_PATH_METADATA = {
    'extra/geert.css': {'path': 'static/geert.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}
CUSTOM_CSS = 'static/geert.css'

LINKS = (('home', '/'),
         ('about me', '/pages/about.html'),
         ('publications', 'https://scholar.google.com/citations?user=oj_-lW4AAAAJ&hl=en'),)


DEFAULT_PAGINATION = 50

THEME = 'flex-theme'
SITELOGO = 'https://pbs.twimg.com/profile_images/683734803133235200/NogCr1RI_400x400.jpg'
SITETITLE = 'Geert Barentsen'
SITESUBTITLE = 'Scientist & Software Engineer'

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/barentsen'),
          ('twitter', 'https://twitter.com/geerthub'),
          ('github', 'https://github.com/barentsen'))
