import graphene
from graphql_auth import mutations
from .job_mutations import AddJobMutation
from graphql_auth.schema import UserQuery, MeQuery
from .job_queries import Query as JobQuery


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    refresh_token = mutations.RefreshToken.Field()

class Query(UserQuery, MeQuery, JobQuery, graphene.ObjectType):
    pass
class JobMutations(AuthMutation, graphene.ObjectType):
    add_job = AddJobMutation.Field()
    pass

schema = graphene.Schema(query=Query, mutation=JobMutations)