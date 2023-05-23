from graphene import Mutation, String
from .models import Job
# from services.grpc_job_cient import client as job_client
from .grpc_job_cient.client import send_job
from graphql_jwt.decorators import login_required


class AddJobMutation(Mutation):
    class Arguments:
        job_id = String(required=True)
        status = String(required=True)

    job = String()
    @login_required
    def mutate(self, info, job_id, status):
        # create a new job object
        new_job = Job(job_id=job_id, status=status)

        # save the job object to the database
        # new_job.save()

        # return the job's ID
        job = f"Job {job_id} has been added with status {status}."
        send_job(job_id, status)
        return AddJobMutation(job=job)

class DeleteJobMutation(Mutation):
    class Arguments:
        job_id = String(required=True)

    job = String()
    
    @login_required
    def mutate(self, info, job_id):
        # delete the job from the database
        job = Job.objects.get(job_id=job_id)
        job.delete()

        # return the job's ID
        job = f"Job {job_id} has been deleted."
        return DeleteJobMutation(job=job)