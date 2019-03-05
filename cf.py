import CloudFlare
import socket
import sys
def main():
    zone_name = "feral.dev"

    # Initialize Cloudflare object
    cf = CloudFlare.CloudFlare()

    # Get the a/cname/txt/etc names from the domain zone
    zone_info = zones = cf.zones.get(params={'name':zone_name})

    zone_id = zone_info[0]['id']
    dns_records = []

    # Iterate through the feral_servers file to get all server names
    with open("feral_servers", "r") as server:

        for slot in server:

            # Reading the newline character gives us a crash
            slot = slot.strip('\n')

            # Get the IP for a server by pinging the slot
            ip = socket.gethostbyname(slot)

            # Since we only need the slot name we can take out feralhosting.com
            slot = slot.replace(".feralhosting.com","")

            # All the IPs are recorded as A name reords
            dns_records.append({'name':slot, 'type':'A', 'content':ip})


    for dns_record in dns_records:
        # Insert each record in the dns_records array
        r = cf.zones.dns_records.post(zone_id, data=dns_record)
    exit(0)
    '''
    This block of code is to remove records from the zones
    It only removes a couple at a time though
    '''

    # zone_info = cf.zones.get(params={'name': zone_name, 'per_page':1000})
    # zone_id = zone_info[0]['id']
    #
    # dns_records = cf.zones.dns_records.get(zone_id)
    # for dns_record in dns_records:
    #     print dns_record
    #     dns_record_id = dns_record['id']
    #     r = cf.zones.dns_records.delete(zone_id, dns_record_id)

if __name__ == '__main__':
    main()
