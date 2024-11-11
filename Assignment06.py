import argparse 
import socket
import time
from scapy.all import IP, ICMP, sr1

def parse_arguments():
    parser = argparse.ArgumentParser(description='Python Traceroute Utility')
    parser.add_argument("destination", help="Target host (domain name or IP address)")
    parser.add_argument("-m", "--max-hops", type=int, default=30, help="Maximum number of hops (default: 30)")
    parser.add_argument("-t", "--timeout", type=float, default=2, help="Timeout in seconds (default: 2)")
    return parser.parse_args()

def traceroute(destination, max_hops, timeout):
    try:
        destination = socket.gethostbyname(destination)
    except socket.gaierror as e:
        print(f"Error: Unable to resolve {destination}")

    print(f"Traceroute to {destination} ({destination}), with maximum of {max_hops} hops:\n")
    
    for ttl in range(1, max_hops + 1):
        packet = IP(dst=destination, ttl=ttl) / ICMP()
        start_time = time.time()
        reply = sr1(packet, timeout=timeout, verbose=0)
        end_time = time.time()
          
        if reply:
            round_trip_time = (end_time - start_time) * 1000 #convert to milliseconds
            print(f"{ttl}\t{reply.src:<20}{round_trip_time:.2f}")  

            if reply.type == 0: # ICMP Echo Reply indiciates destination reached        
                print("Destination Reached.")
                break

        else:
            print(f"{ttl:<3} *")

    else:
        print("\nReached maximum hops without reaching destination.")

    try:
        destination = socket.gethostbyname(destination)
    except socket.gaierror:
        print(f"Error: Unable to resolve {destination}")
        return
    
    except KeyboardInterrupt:
        print("\nTraceroute interruped by user")
        return

if __name__ == "__main__":
    args = parse_arguments()
    traceroute(args.destination, args.max_hops, args.timeout)