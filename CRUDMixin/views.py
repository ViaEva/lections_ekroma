from search import search_object

class CreateMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def post(self, **kwargs):
        self._get_or_set_objects_and_id()
        self.id +=1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status':201, 'msg':object_}

class RetrieveMixin:
    def get(self):
        response = []
        for obj in self.objects:
            response.append({'title':obj['title'], 'price' : obj['price']})
        return {'status':200, 'msg': response}

    @search_object
    def get_detail(self, id, **kwargs):
        obj = kwargs['object_']
        if not obj:
            return {'status': 404, 'msg': 'Not Found'}
        return {'status': 200, 'msg':obj}
        
class UpdateMixin:
    @search_object
    def patch(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if not obj:
            return {'status': 404, 'msg':'Not Found'}
        obj.update(**kwargs)
        return {'status':206,'msg':'Succesfully updated'}

class DestroyMixin:
    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs['object_']
        if not obj:
            return {'status':404,'msg':'Not Found'}
        self.objects.remove(obj)
        return {'status': 204,'msg': 'Soccessfully deleted'}
