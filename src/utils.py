import urllib.robotparser
from urllib.parse import urljoin

def can_fetch(base_url, user_agent='*', path='/'):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(base_url, 'robots.txt'))
    rp.read()
    return rp.can_fetch(user_agent, path)
