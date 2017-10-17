from general import *
from domain import *
from ip_address import *
from nmap_scan import *
from robots_txt import *
from whois import *


root_dir='sites'
create_dirs(root_dir)

def get_info(url):
	domain_name=get_domain_name(url)
	name=domain_name[:domain_name.find('.')]
	ip_address=get_ip_address(domain_name)
	nmap=get_nmap("-F",ip_address)
	robots=get_robot_txt(url)
	who_is=whois(domain_name)
	create_report(domain_name,name,ip_address,nmap,robots,who_is)


def create_report(domain_name,name,ip_address,nmap,robots,who_is):
	path=root_dir+'/'+name
	create_dirs(path)
	write_files(path+"/domain_name",domain_name)
	write_files(path+"/ip_address",ip_address)
	write_files(path+"/nmap",nmap)
	write_files(path+"/robots",robots)
	write_files(path+"/whois",who_is)


