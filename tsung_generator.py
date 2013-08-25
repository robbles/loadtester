import jinja2
from fabric.api import local
from collections import namedtuple

Server = namedtuple('Server', 'host', 'port')

class LoadTest(object):

    def __init__(self, servers=None, sessions=None, duration=None, log_level='debug'):
        if servers is None:
            servers = []
        if sessions is None:
            sessions = []

        self.servers = servers
        self.sessions = sessions
        self.duration = duration
        self.log_level = log_level

    def add_server(self, host, port=80):
        self.servers.append(Server(host=host, port=port))

    def add_session(self, session):
        self.sessions.append(session)

    def validate(self):
        # TODO: use xmllint like Syntastic does to check generated config file
        # against XML schema

    def run(self):
        # TODO: use fabric to run and manage Tsung

    def generate_config(self):
        # TODO: use jinja2 to render configuration into xml template


class Session(object):
    def __init__(self, name, probability, steps=None):
        self.name = name
        self.probability = probability
        if steps is not None:
            self.steps = steps
        else:
            self.steps = []

    def add_step(self, step):
        self.steps.append(step)


class Request(object):
    def __init__(url, method='GET', contents=None, auth, headers):
        # TODO: parse URL, set instance vars


class ThinkTime(object):
    pass


def test():
    loadtest = LoadTest(
        servers=[ Server('localhost', 8080) ],
        duration=3600,
        arrival_phases=[
            ArrivalPhase(duration=1000, max_users=1000, arrival_rate=1)
            ArrivalPhase(duration=600, max_users=300, inter_arrival=2)
        ]
    )

    session = Session('simple_request', 100, loop=True, steps=[
        Request('http://foobar.com/path/'),
        ThinkTime(5, random=True)
        Request('https://secure.foobar.com/admin/', auth=('admin', 'password')),
        ThinkTime(5, random=True)
    ])

