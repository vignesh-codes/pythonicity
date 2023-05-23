from .consistent_hash import ConsistentHashLoadBalancer

class JobLoadBalancer():
    def __init__(self, targets):
        self.lb = ConsistentHashLoadBalancer(targets)

    def getTarget(self, request, context):
        target = self.lb.route(request.job_id)
        return target
        # return Job(job_id=request.job_id, job_status=request.job_status)