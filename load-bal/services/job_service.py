from jobs_pb2 import Job
from jobs_pb2_grpc import JobServiceServicer
from .send_job import send_job

from load_balancer.job_lb import JobLoadBalancer

targets = ["localhost:50054"]

class JobService(JobServiceServicer):
    def __init__(self):
        self.lb = JobLoadBalancer(targets)
        
    def AddJob(self, request, context):
        target = self.lb.getTarget(request, context)
        print(f"Sending request to {target}")
        send_job(target, request.job_id, request.job_status)
        return Job(job_id=request.job_id, job_status=request.job_status)
    
    