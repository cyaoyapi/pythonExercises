def group_files_by_owner(files):

	owners = {name for name in files.values()}
	owners = {name:[] for name in owners}
	for key, value in files.items():
		owners[value].append(key)
	return owners