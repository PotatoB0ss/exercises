import re


def domain_name(url):
    dom_name = ""
    address = url.split("/")
    if address[0] == "https:" or address[0] == "http:":
        address = address[2].split(".")
    else:
        address = address[0].split(".")
    if address[0] == "www":
        dom_name = address[1]
    else:
        dom_name = address[0]

    return dom_name


def domain_name_v2(url):
    return re.search('(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')


