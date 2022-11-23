import subprocess 
import time
import re


def create_account(name):
    result = subprocess.run("cleos create key --to-console", shell=True,stdout=subprocess.PIPE)

    result = str(result)

    result = result.split("key:")
    pkey = result[1].replace("\\nPublic ","")
    pubkey = result[2].replace("\\n')","")

    pubkey = pubkey.strip()

    pkey = pkey.strip()


    result1 = subprocess.run(f"cleos create account eosio {name} {pubkey}", shell=True,stdout=subprocess.PIPE)
    print (result1)

    result2 = subprocess.run(f"cleos wallet import --name local --private-key {pkey}", shell=True,stdout=subprocess.PIPE)
    print (result2)


    return name

# create_account("comprador")

def create_tickets(name_of_vendor,name_of_concert,num_tickets,ticket_id,description_of_concert):
    result1 = subprocess.run("cleos push action nft create '{"+f'"issuer":"{name_of_vendor}", "symbol":"{ticket_id}"' + "}' --permission nft@active", shell=True,stdout=subprocess.PIPE)
    print (result1)
    tickets_ids = []

    for i in range(int(num_tickets)):
        tickets_ids.append(f"ticket{i}")

    tickets_ids = str(tickets_ids)


    result1 = subprocess.run("cleos push action nft issue " + "'" + f'["{name_of_vendor}","{num_tickets} {ticket_id}",{tickets_ids},"{name_of_concert}","{description_of_concert}"]"'+ f"' --permission {name_of_vendor}@active", shell=True,stdout=subprocess.PIPE)
    print (result1)


# create_tickets("buyer","wisin y yandel","15","PRUEBA","concierto 25 noviembre")





def transfer_ticket(name_of_vendor,name_of_buyer,num_tickets,ticket_id,description):
    for i in range(int(num_tickets)):
        result1 = subprocess.run("cleos push action nft transfer '["+f'"{name_of_vendor}", "{name_of_buyer}", "1 {ticket_id}", "{description}" ' +f"]' -p {name_of_vendor}@active", shell=True,stdout=subprocess.PIPE)
        print (result1)
        time.sleep(0.5)


# transfer_ticket("buyer","comprador","2","TEST","compra de dos tickets para test")    

def verify_tickets(name,ticket_id):
    result1 = subprocess.run(f"cleos get currency balance nft {name}", shell=True,stdout=subprocess.PIPE)


    result1 = str(result1)
    
    
    r = re.search(r"(stdout=b')([^']+)(')", result1)
    result = str(r.group(2))   
    
     
    result = result.split('\\n')
    amount = 0
    for token in result:
        ress = token.replace(ticket_id, '')
        ress = ress.strip()
        if ress.isdigit():
            amount = int(ress)
            break
    return amount


# print(type(verify_tickets("jean","WISYAN")))