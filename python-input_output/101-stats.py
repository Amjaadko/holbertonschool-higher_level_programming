#!/usr/bin/python3
"""Log parsing script that computes metrics."""

import sys

def print_stats(total_size, status_counts):
    """Print total file size and status codes."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

def main():
    total_size = 0
    status_counts = {}
    line_count = 0
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()
            if len(parts) < 9:
                continue
            # Extract status code and file size
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except ValueError:
                continue

            total_size += size
            if status in valid_codes:
                status_counts[status] = status_counts.get(status, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
