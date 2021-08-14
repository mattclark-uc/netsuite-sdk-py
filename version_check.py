from version import VERSION as NEW_VERSION
from old_version import VERSION as OLD_VERSION

if NEW_VERSION == OLD_VERSION:
	print('##vso[task.logissue type=error] You must change the version number in version.py')
