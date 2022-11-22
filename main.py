from flask import Flask, render_template, request
import subprocess
import pres
# VARIABLE_CONDICIONAL = True #useTicket, vambiar de 0 a 1

app = Flask(__name__)
@app.route('/index.html', methods =['GET', 'POST'])
@app.route('/', methods =['GET', 'POST'])
def home():
    return render_template('home.html')
        

@app.route('/createAccount', methods =['GET', 'POST'])
def createAccount():
    if request.method=='POST':
        name = str(request.form['account'])
        pres.create_account(name)
        return render_template('message.html',title="Account creation", message = f"Enjoy your account {name}")

    else:
        return render_template('createAccount.html')

@app.route('/issueTickets', methods =['GET', 'POST'])
def issueTickets():
    if request.method=='POST':
        name_of_vendor = str(request.form['name_of_vendor'])
        name_of_concert = str(request.form['name_of_concert'])
        num_tickets = str(request.form['num_tickets'])
        ticket_id = str(request.form['ticket_id'])
        description_of_concert = str(request.form['description_of_conc'])
        
        pres.create_tickets(name_of_vendor,name_of_concert,num_tickets,ticket_id,description_of_concert) 
        # return name_of_vendor+ticket_id+num_tickets+name_of_concert+description_of_concert
        return render_template('message.html',title="Issue Tickets", message = f"Tickets for {name_of_concert} issued")
    else:
        return render_template('issueTickets.html')
    
@app.route('/buyTicket', methods =['GET', 'POST'])
def buyTicket():
    if request.method=='POST':
        name_of_buyer = str(request.form['account'])
        ticket_id = str(request.form['ticket_id'])
        name_of_vendor = str(request.form['name_of_vendor'])
        num_tickets = str(request.form['num_tickets'])
        
        pres.transfer_ticket(name_of_vendor,name_of_buyer,num_tickets,ticket_id,"bought tickets")
        return render_template('exit.html', message= "Comprador: "+name_of_buyer+ " de "+ticket_id+" Gracias! Disfruta tu concierto")
    
    else:
        return render_template('buyTicket.html')
    
@app.route('/useTicket', methods =['GET', 'POST'])
def useTicket():
    if request.method=='POST':
        name = str(request.form['account'])
        ticket_id = str(request.form['ticket_id'])
        name_of_vendor = str(request.form['name_of_vendor'])
        num_tickets = str(request.form['num_tickets'])
        
        if pres.verify_tickets(name,ticket_id)>= int(num_tickets):
            pres.transfer_ticket(name,name_of_vendor,num_tickets,ticket_id,"used tickets")
            return render_template('message.html',title="Use ticket", message = f"Enjoy your concert!")
        return render_template('message.html',title="Fail", message = f"not enough tickets to complete")
    else:
        return render_template('useTicket.html')
    
@app.route('/verifyTickets', methods =['GET', 'POST'])
def verifyTickets():
    if request.method=='POST':
        name = str(request.form['account'])
        ticket_id = str(request.form['ticket_id'])
        amount = pres.verify_tickets(name,ticket_id)
        print
        return render_template('message.html',title="Verify tickets", message = f"You have {amount} {ticket_id}")
        
    else:
        return render_template('verifyTickets.html')
    
@app.route('/exit', methods =['GET', 'POST'])
def exit():
    return render_template('exit.html')
if __name__ == "__main__":

    # pres.create_account("nft")
   # result = subprocess.run("cleos set contract nft ./ eosio.nft.wasm eosio.nft.abi -p nft@active", shell=True,stdout=subprocess.PIPE)
    app.run(debug=False, host='0.0.0.0', port=3023)