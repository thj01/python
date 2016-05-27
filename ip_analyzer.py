
import os, re

# definerer cls() som renser skærmen
def cls():
	os.system("clear")
	
test = 0

if test == 1:	

	ip = "112.143.0.45/45"

else:
	
	ip = input("IP-adresse inklusiv CIDR (f.eks: 192.168.2.100/24): ")
	
dot1 = ip.find(".")

pos_dot1 = dot1

dot2 = ip[pos_dot1+1:].find(".")

pos_dot2 = pos_dot1 + dot2+1

dot3 = ip[pos_dot2+1:].find(".")

pos_dot3 = pos_dot2 + (dot3+1)

cidr_pos = ip.find("/")

if test == 1:

	print ("Første dot: {0}".format(pos_dot1))
	print ("Andet dot: {0}".format(pos_dot2))
	print ("tredie dot: {0}".format(pos_dot3))
	print ("CIDR position: {0}".format(cidr_pos))
	print("- - - - - - - - - - - - - - - - - - - - - - - - ")

ip_1 = int(ip[:pos_dot1])

ip_2 = int(ip[pos_dot1+1:pos_dot2])

ip_3 = int(ip[pos_dot2+1:pos_dot3])

ip_4 = int(ip[pos_dot3+1:cidr_pos])

cidr = int(ip[cidr_pos+1:])

ip_1_bin = bin(ip_1)[2:]

ip_2_bin = bin(ip_2)[2:]

ip_3_bin = bin(ip_3)[2:]

ip_4_bin = bin(ip_4)[2:]

ip_1_hex = hex(ip_1)[2:]

ip_2_hex = hex(ip_2)[2:]

ip_3_hex = hex(ip_3)[2:]

ip_4_hex = hex(ip_4)[2:]

ip_all={'ip_0': ip_1,'ip_1': ip_2,'ip_2': ip_3,'ip_3': ip_4}

ip_error = 0

cidr_error = 0

for i in range(4):
	
	test_ip=ip_all['ip_{0}'.format(i)]

	if test_ip < 0 or test_ip > 255:
		
		print ("Der er fejl i den {0}. oktet. Tallet {1} er ikke imellem 0 og 255".format(i,test_ip))
		
		ip_error += 1

if cidr < 1 or cidr > 30:
	
	print("Der er fejl i din CIDR. Tallet er ikke imellem 1 og 32")
		
	cidr_error +=1
	
all_errors = ip_error + cidr_error

if ip_error > 0 or cidr_error > 0:
	
	print("""
	
     ######  #####   #####    ####   #####
     #       #    #  #    #  #    #  #    #
     #####   #    #  #    #  #    #  #    #
     #       #####   #####   #    #  #####
     #       #   #   #   #   #    #  #   #
     ######  #    #  #    #   ####   #    #

	""")
	
	print("\nDer er {0} fejl i den indtastede IP-adressen ({1}). Indtast en ny!".format(all_errors,ip))

	exit(0)
	
		

	
if test == 1:

	print ("Første oktet: {0}".format(ip_1))
	print ("Anden oktet: {0}".format(ip_2))
	print ("Tredie oktet: {0}".format(ip_3))
	print ("Fjerde oktet: {0}".format(ip_4))
	print ("CIDR: {0}".format(cidr))
	print (ip_all)
	print("- - - - - - - - - - - - - - - - - - - - - - - - ")


fulde_okt = cidr//8

rest_okt = cidr%8

if test == 1:

	print("Fulde oktetter{0}".format(fulde_okt))

	print("Rest oktetter{0}\n".format(rest_okt))

	


oktets_all ={}

for i in range(4):
	
	if fulde_okt > 0:
		
		oktets_all["oktet{0}".format(i)] = 8
		
		fulde_okt -= 1
		
		if test == 1:
		
			print (oktets_all)
	else:
		
		oktets_all["oktet{0}".format(i)] = rest_okt
		
		rest_okt -= rest_okt
		
		if test == 1:
		
			print (oktets_all)

netm_okt_1 = int(oktets_all["oktet0"])

netm_okt_2 = int(oktets_all["oktet1"])

netm_okt_3 = int(oktets_all["oktet2"])

netm_okt_4 = int(oktets_all["oktet3"])

netm1 = 2**netm_okt_1-1

netm2 = 2**netm_okt_2-1

netm3 = 2**netm_okt_3-1

netm4 = 2**netm_okt_4-1

netm1_bin = bin(netm1)[2:]

netm2_bin = bin(netm2)[2:]

netm3_bin = bin(netm3)[2:]

netm4_bin = bin(netm4)[2:]

netm1_hex = hex(netm1)[2:]

netm2_hex = hex(netm2)[2:]

netm3_hex = hex(netm3)[2:]

netm4_hex = hex(netm1)[2:]

if test == 1:

	print ("Udskrift af dictionary : {0}.{1}.{2}.{3}".format(netm_okt_1,netm_okt_2,netm_okt_3,netm_okt_4))

print("\n\n- - - - - - - - - - - - - - - - - - - - - - - - \n\n")

print ("Du indtastede IP-adressen: %s" %(ip))

print ("Omregnet til binær : {0}.{1}.{2}.{3}".format(ip_1_bin, ip_2_bin,ip_3_bin,ip_4_bin))

print ("Omregnet til hex : {0}.{1}.{2}.{3}".format(ip_1_hex, ip_2_hex,ip_3_hex,ip_4_hex))

hosts = (2**32-cidr) - 2

print("Det kan være {0} klienter på dit netværk".format(hosts))



print ("\nNETMASKEN")

print ("\nCidr: {0}".format(cidr))

print ("Omregnet til titalssystem værdier : {0}.{1}.{2}.{3}".format(netm1,netm2,netm3,netm4))

print ("Omregnet til binær : {0}.{1}.{2}.{3}".format(netm1_bin,netm2_bin,netm3_bin,netm4_bin))

print ("Omregnet til hex : {0}.{1}.{2}.{3}".format(netm1_hex,netm2_hex,netm3_hex,netm4_hex))

