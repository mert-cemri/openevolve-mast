'''
Main module to start the Ping Application
'''
import argparse
from ping_tool import PingTool
def main():
    parser = argparse.ArgumentParser(description="Ping a host and display the round-trip time.")
    parser.add_argument("host", type=str, help="IP address or hostname to ping")
    parser.add_argument("-c", "--count", type=int, default=4, help="Number of pings to send")
    args = parser.parse_args()
    ping_tool = PingTool(args.host, args.count)
    results = ping_tool.ping_host()
    if not results:
        print("Failed to ping the host.")
        return
    for i, result in enumerate(results, 1):
        print(f"Ping {i}: {result} ms")
    avg_time = sum(results) / len(results)
    print(f"\nAverage round-trip time: {avg_time:.2f} ms")
if __name__ == "__main__":
    main()