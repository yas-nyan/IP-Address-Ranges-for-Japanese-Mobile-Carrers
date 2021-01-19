import pandas as pd
import ipaddress


def get_start_addr(cidr):
    network = ipaddress.ip_network(cidr)
    return network.network_address


def get_end_addr(cidr):
    network = ipaddress.ip_network(cidr)
    return network.broadcast_address


# get ranges
mobile_ipv4_df = pd.read_csv("../ipv4_ranges.csv", header=0)
mobile_ipv4_df["prefix"] = mobile_ipv4_df["prefix"].apply(str.strip)
mobile_ipv6_df = pd.read_csv("../ipv6_ranges.csv", header=0)
mobile_ipv6_df["prefix"] = mobile_ipv6_df["prefix"].apply(str.strip)

# start_addrとend_addrを埋める
mobile_ipv4_df["start_addr"] = mobile_ipv4_df["prefix"].apply(get_start_addr)
mobile_ipv4_df["end_addr"] = mobile_ipv4_df["prefix"].apply(get_end_addr)
mobile_ipv6_df["start_addr"] = mobile_ipv6_df["prefix"].apply(get_start_addr)
mobile_ipv6_df["end_addr"] = mobile_ipv6_df["prefix"].apply(get_end_addr)


def get_mobile_carrers(ipaddr):
    ipaddr_obj = ipaddress.ip_address(ipaddr)
    if ipaddr_obj.version == 4:
        carrers = (mobile_ipv4_df[(mobile_ipv4_df["start_addr"] <= ipaddr_obj) & (
            mobile_ipv4_df["end_addr"] >= ipaddr_obj)])
    elif ipaddr_obj.version == 6:
        carrers = (mobile_ipv6_df[(mobile_ipv6_df["start_addr"] <= ipaddr_obj) & (
            mobile_ipv6_df["end_addr"] >= ipaddr_obj)])

    return carrers

def get_mobile_carrers_name(ipaddr):
    carrers = get_mobile_carrers(ipaddr)
    if len(carrers) >=1:
      isp_name = carrers.iat[0, 2]
      return isp_name
    else:
      return ""
      

def is_mobile_ip(ipaddr):
    carrers = get_mobile_carrers(ipaddr)
    if len(carrers) >= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    import sys

    while True:
        addr = input("IP address?: ")
        try:
            ipaddress.ip_address(addr)
        except ValueError:
            print("Invalid IP address", file=sys.stderr)
            continue

        carrers = get_mobile_carrers(addr)
        is_this_addr_mobile = is_mobile_ip(addr)

        if is_this_addr_mobile:
            print(f"{addr} is mobile address. ({carrers.iloc[-1]['ISP']})")
        else:
            print(f"{addr} is not mobile address. ")
