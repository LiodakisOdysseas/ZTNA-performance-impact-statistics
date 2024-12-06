import sys
import re
import numpy as np

def parse_file(file_path):
    response_codes = []
    total_times = []
    download_speeds = []

    with open(file_path, 'r') as file:
        for line in file:
            if match := re.search(r'response_code:\s+(\d+)', line):
                response_codes.append(int(match.group(1)))
            elif match := re.search(r'time_total:\s+([\d\.]+)s', line):
                total_times.append(float(match.group(1)))
            elif match := re.search(r'average_download_speed:\s+(\d+)', line):
                download_speeds.append(int(match.group(1)))

    return response_codes, total_times, download_speeds

def calculate_statistics(data):
    minimum = np.min(data)
    maximum = np.max(data)
    average = np.mean(data)
    stddev = np.std(data)
    return minimum, maximum, average, stddev

def main():
    if len(sys.argv) != 2:
        print("Usage: python response_metrics_analysis.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        response_codes, total_times, download_speeds = parse_file(file_path)

        # Calculate success rate
        success_count = response_codes.count(200)
        success_rate = (success_count / len(response_codes)) * 100 if response_codes else 0

        # Calculate statistics for total_time and average_download_speed
        total_time_stats = calculate_statistics(total_times)
        download_speed_stats = calculate_statistics(download_speeds)

        # Print results
        print(f"Success Rate: {success_rate:.2f}%")
        print("\nTotal Time Statistics:")
        print(f"  Minimum: {total_time_stats[0]:.6f}s")
        print(f"  Maximum: {total_time_stats[1]:.6f}s")
        print(f"  Average: {total_time_stats[2]:.6f}s")
        print(f"  Std Dev: {total_time_stats[3]:.6f}s")

        print("\nAverage Download Speed Statistics:")
        print(f"  Minimum: {int(download_speed_stats[0])} bytes/sec")
        print(f"  Maximum: {int(download_speed_stats[1])} bytes/sec")
        print(f"  Average: {int(download_speed_stats[2])} bytes/sec")
        print(f"  Std Dev: {int(download_speed_stats[3])} bytes/sec")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

