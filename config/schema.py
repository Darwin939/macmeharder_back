import graphene

from apps.main.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
