from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from gqlapp.models import ProductModel
import graphene

class Products(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = ['id', 'Segment', 'Country', 'Product']
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    prodinfo = relay.Node.Field(Products)
    all_prodinfo = DjangoFilterConnectionField(Products)

    def resolve_prodinfo(self, info):
        return ProductModel.objects.all()

schema = graphene.Schema(query=Query)
