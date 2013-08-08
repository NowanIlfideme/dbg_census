# PS2 API wrapper
import requests

# we aren't going to create explicit methods, just a framework for calling them
# if someone else wants to maintain a wrapper to this, of course, they're free to do so

class Stats:
	base_url = "census.soe.com"
	service_id = None # not strictly required--API works without, but TOS does say it's required, so you may get throttled or blacklisted for excessive calls without
	verb = "get" # sensible default
	namespace = None # must be set to use
	format = "json" # sensible default
	_collections = {}
	_collection_names = None

	def __call__(self, collection, options):
		target = None
		if self.service_id:
			target = "http://%s/s:%s/%s/%s/%s/%s" % (self.base_url, self.service_id, self.format, self.verb, self.namespace, collection)
		else:
			target = "http://%s/%s/%s/%s/%s" % (self.base_url, self.format, self.verb, self.namespace, collection)

		result = requests.get(target, params=options)
		if result.ok:
			return result.json()
		else:
			result.raise_for_stats()

	def __str__(self):
		return "SOE STATS API"

	# just for introspection really
	def collections(self, collection):
		"""list available collections for this namespace"""
		if self._collection_names is None:
			collections = self("", {})['datatype_list']
			self._collection_names = map(lambda x: x['name'], collections)
			for thing in collections:
				self._collections[thing['name']] = thing

		if collection is not None:
			return self._collections[collection]

		return self._collection_names





