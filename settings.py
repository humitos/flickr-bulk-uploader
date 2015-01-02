import re

api_secret = 'a131ba6ac653b986'
api_key = 'dced4d69f72c55375dd72f12d2a3941b'

PHOTOS_DIRECTORY = '/home/YOUR_USERNAME/fotos'


EXCLUDE_FILES = (
    r'.*thm$',
    r'.*/recuerdos viejos/.*',
    r'.*/camara pauli/.*MOV$',
    r'.*\.nono.*',
    r'.*\.con estefa.*',
)

EXCLUDE_FILES = '(' + '|'.join(EXCLUDE_FILES) + ')'
EXCLUDE_FILES_REGEX = re.compile(EXCLUDE_FILES, flags=re.IGNORECASE)
