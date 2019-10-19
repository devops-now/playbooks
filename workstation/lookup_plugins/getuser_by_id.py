__metaclass__ = type

import os

from ansible.errors import AnsibleFileNotFound, AnsibleLookupError, AnsibleUndefinedVariable
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        if len(terms) > 1:
            raise AnsibleLookupError("must be a uid, not a list")

        try:
            uid = int(terms[0])
        except ValueError:
            raise AnsibleLookupError("must be an integer")

        with open('/etc/passwd', 'r') as f:
            for line in f:
                user = line.split(':')
                if int(user[2]) == uid:
                    return [user[0]]

        return None
