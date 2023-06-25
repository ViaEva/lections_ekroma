def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for obj in self.objects:
            if obj.get('id') == id:
                kwargs.update(object_ = obj)
                return func(*args, **kwargs)
        kwargs.update(object_=None)
        return func(*args, **kwargs)
    return wrapper