import graphene
from graphene_django import DjangoObjectType
from .models import Job
from graphql import GraphQLError

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):
    jobs = graphene.List(JobType)

    def resolve_jobs(self, info):
        # raise GraphQLError('Name argument is missing or empty', code='INVALID_ARGUMENT', fields=['name'])

        return Job.objects.all()
    
    job = graphene.Field(JobType, id=graphene.Int(required=True))
    def resolve_job(self, info, id):
        try:
            return Job.objects.get(id=id)
        except Job.DoesNotExist:
            return None