#! python
'''Extended gpg execution module.
This module implements extra execution actions related to the gpg module.

Version: 0.0.1

TODO:
- everything

Refs:
'''

import logging

LOGGER = logging.getLogger(__name__)

def key_details(text = None, filename = None):
	'''Key Details
	Get the details for a key, like the output of gpg.list_keys, for the provided key file or content.
	'''

	gnupghome = __salt__['temp.dir']()
	__salt__['gpg.import_key'](text = text, filename = filename, gnupghome = gnupghome)
	result = __salt__['gpg.list_keys'](gnupghome = gnupghome)
	
	if len(result) > 1:
		raise RuntimeError('Too many keys on the temp GPG keyring, someone is tampering with our temp dir')
	elif not result:
		raise RuntimeError("The key wasn't imported, there's something wrong with gpg")
	else:	
		result = result[0]
		
	__salt__['file.remove'](gnupghome)
	return result