import grpc
import jobs_pb2
import jobs_pb2_grpc
from concurrent import futures

class JobService(jobs_pb2_grpc.JobServiceServicer):
    def AddJob(self, request, context):
        job_id = request.job_id
        job_status = request.job_status
        print(f"Received job with ID {job_id} and status {job_status}")
        return jobs_pb2.Job(job_id=job_id, job_status=job_status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jobs_pb2_grpc.add_JobServiceServicer_to_server(JobService(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print("gRPC server listening on port 50054...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()