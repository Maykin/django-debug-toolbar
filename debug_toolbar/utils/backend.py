from django.core.cache import cache

class CacheBackend(object):
    prefix = 'django_debug_data_'
    counter = prefix + 'counter'

    def store(self, data):
        cache.add(self.counter, 0)
        count = cache.incr(self.counter)
        cache.set(self.prefix + str(count), data)

    def last(self):
        return cache.get(self.counter)

    def get(self, count):
        return cache.get(self.prefix + str(count))
