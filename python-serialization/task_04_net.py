#!/usr/bin/python3
"""Client-server application with serialization using JSON."""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """Start a server that receives a serialized dictionary from a client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = b''
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet
            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON from client.")


def send_data(dictionary, host='127.0.0.1', port=65432):
    """Send a Python dictionary to the server after serializing it."""
    try:
        serialized_data = json.dumps(dictionary).encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Failed to connect to the server.")
