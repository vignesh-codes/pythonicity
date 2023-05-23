import grpc
from concurrent import futures
from jobs_pb2_grpc import add_JobServiceServicer_to_server
from services.job_service import JobService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    
    add_JobServiceServicer_to_server(JobService(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print("Load balancer started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()