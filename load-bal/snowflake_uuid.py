import time

# Define constants
EPOCH = 1288834974657  # Twitter snowflake epoch (in milliseconds)
DATA_CENTER_ID_BITS = 5
MACHINE_ID_BITS = 5
SEQUENCE_BITS = 12
MAX_DATA_CENTER_ID = (1 << DATA_CENTER_ID_BITS) - 1
MAX_MACHINE_ID = (1 << MACHINE_ID_BITS) - 1
MAX_SEQUENCE = (1 << SEQUENCE_BITS) - 1

# Initialize variables
last_timestamp = 0
data_center_id = 0
machine_id = 0
sequence = 0

def generate_snowflake():
    # Get the current timestamp in milliseconds
    timestamp = int(time.time() * 1000)

    # If the timestamp hasn't changed since last call, increment the sequence number
    global last_timestamp, sequence
    if timestamp == last_timestamp:
        sequence = (sequence + 1) & MAX_SEQUENCE
        if sequence == 0:
            # Sequence number has rolled over, wait until next millisecond
            timestamp = wait_for_next_millisecond(last_timestamp)
    else:
        # Reset sequence number
        sequence = 0

    # Update last timestamp
    last_timestamp = timestamp

    # Generate snowflake ID
    snowflake = (
        ((timestamp - EPOCH) << (DATA_CENTER_ID_BITS + MACHINE_ID_BITS + SEQUENCE_BITS)) |
        (data_center_id << (MACHINE_ID_BITS + SEQUENCE_BITS)) |
        (machine_id << SEQUENCE_BITS) |
        sequence
    )

    return snowflake

def wait_for_next_millisecond(last_timestamp):
    # Wait until the next millisecond
    timestamp = int(time.time() * 1000)
    while timestamp <= last_timestamp:
        timestamp = int(time.time() * 1000)
    return timestamp

import datetime

def decode_snowflake(snowflake):
    # Extract parts of the snowflake ID
    timestamp = (snowflake >> (5 + 5 + 12)) + 1288834974657
    data_center_id = (snowflake >> (5 + 12)) & 0x1F
    machine_id = (snowflake >> 12) & 0x1F
    sequence = snowflake & 0xFFF

    # Convert timestamp to datetime object
    date = datetime.datetime.utcfromtimestamp(timestamp / 1000)

    # Return decoded values as a dictionary
    return {
        'timestamp': timestamp,
        'date': date,
        'data_center_id': data_center_id,
        'machine_id': machine_id,
        'sequence': sequence
    }
