import grpc
import jobs_pb2
import jobs_pb2_grpc

def send_job(job_id, job_status):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = jobs_pb2_grpc.JobServiceStub(channel)
        job = jobs_pb2.Job(job_id=job_id, job_status=job_status)
        response = stub.AddJob(job)
        print(f"Server responded with job ID {response.job_id} and status {response.job_status}")

if __name__ == '__main__':
    send_job("123", "completed")