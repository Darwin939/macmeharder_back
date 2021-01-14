import graphene

from apps.apps.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
