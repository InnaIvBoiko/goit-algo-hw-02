import queue
import uuid
import random
import time

# Create request queue
request_queue: queue.Queue[str] = queue.Queue()
request_counter = 0


def generate_request():
    """
    Create a new request and add it to the queue.
    """
    global request_counter
    request_counter += 1
    
    # Create new request with unique identifier
    request_id = f"REQ_{request_counter:04d}_{str(uuid.uuid4())[:8]}"
    
    # Add request to queue
    request_queue.put(request_id)
    print(f"Generated request {request_id} and added to queue")


def process_request():
    """
    Process request from queue if queue is not empty.
    Otherwise, print message that queue is empty.
    """
    if not request_queue.empty():
        # Remove request from queue
        request = request_queue.get()
        
        # Process request
        print(f"Processing request {request}")
        time.sleep(0.5)  # Simulate processing time
        print(f"Request {request} processed successfully")
        
        # Mark task as done
        request_queue.task_done()
    else:
        # Print message that queue is empty
        print("Queue is empty. No requests to process.")


def main():
    """
    Main program loop: while user doesn't exit program,
    execute generate_request() to create new requests,
    execute process_request() to process requests.
    """
    print("Service Center Request Processing System")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            # Execute generate_request() for creating new requests
            if random.choice([True, False]):
                generate_request()
            
            # Execute process_request() for processing requests
            process_request()
            
            # Small pause between operations
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user")


if __name__ == "__main__":
    main()
