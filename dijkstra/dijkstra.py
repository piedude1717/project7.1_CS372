import sys
import json
import math  # If you want to use math.inf for infinity

def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """
    #test
    # TODO Write me!
    shortest_path = []
    start = src_ip.split('.')
    start = start[0:3]
    start_sub = start[0:2]
    start[0] += "."
    start[1] += "."
    start_sub[0] += "."
    start = ''.join(start)
    start_sub = ''.join(start_sub)
    end = dest_ip.split('.')
    end = end[0:3]
    end_sub = end[0:2]
    end[0] += "."
    end_sub[0] += "."
    end_sub[1] += "."
    end = ''.join(end)
    end_sub = ''.join(end_sub)
    if start_sub == end_sub:
        return []

    else:
        to_visit = []
        distance = {}
        parent = {}
        curr_node = ''
        stripped_src_ip = src_ip.split('.')
        stripped_src_ip[0] += "."
        stripped_src_ip[1] += "."
        stripped_src_ip = ''.join(stripped_src_ip[0:3])
        for router in routers:
            distance[router] = math.inf
            parent[router] = None
            to_visit.append(router)
            if stripped_src_ip in router:
                curr_node = router

            if start in router:
                start = router

            if end in router:
                end = router

        # print(to_visit, "this is to visit\n")
        # print(distance, "this is distance\n")
        # print(parent, "this is parent")

        while len(to_visit) > 0:
            if curr_node in to_visit:
                to_visit.remove(curr_node)
            for i in range(len(routers[curr_node]["connections"])):
                neghbors = list(routers[curr_node]["connections"].keys())

            return shortest_path

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
