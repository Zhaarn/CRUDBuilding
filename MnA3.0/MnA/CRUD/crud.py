from crudbuilder.abstract import BaseCrudBuilder
from CRUD.models import Deal

class DealCrud(BaseCrudBuilder):
    model = Deal
    search_fields = ['Deal Number']
    tables2_fields = tuple([f.name for f in model._meta.get_fields()])
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    modelform_excludes = []
    #login_required=True
    #permission_required=True

    # @classmethod
    # def custom_queryset(cls, request, **kwargs):
    #     """Define your own custom queryset for list view"""
    #     qset = cls.model.objects.filter(created_by=request.user)
    #     return qset

    # @classmethod
    # def custom_context(cls, request, context, **kwargs):
    #     """Define your own custom context for list view"""
    #     context['custom_data'] = "Some custom data"
    #     return context