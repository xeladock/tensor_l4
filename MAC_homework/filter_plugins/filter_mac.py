#!/usr/bin/python

import re
def mac_function(init):
    init=str(init)
    if len(init)!=12: return 'Error. It must be 12 letters strictly'
    res = re.sub(r'[h-z,\W_]+', '', init).upper()
    return 'Error. It must be A-F/0-9 chars strictly.' if len(res)!=12 else ':'.join(str(e) for e in [res[i:i+2] for i in range(0, len(res), 2)])


class FilterModule(object):
    def filters(self):
        return {
            'mac_function': mac_function
        }
