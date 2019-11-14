# OpenTrack
A Blockchain and ML based smart contract

## Installation Steps
We will use ```Truffle``` and ```Ganache-cli``` as a basic environment. Also , we will use ```http-server``` for hosting our Web Interface.
```
npm install -g truffle ganache-cli http-server
```
Install [Metamask](https://metamask.io/) for interacting with Web Interface.
Now, run ```ganache-cli``` and note down the mnemonic from the console output. Setup Metamask with the mnemonic and connect to "localhost:8545", you should see all the wallets ganache creates and now we can use them to call Smart Contract methods!.

Now run ```truffle migrate -network development```.
You will observe contract addresses written on the console, which are obtained after compilation and deployment done by truffle.

Note the contract addresses of ChangeOwnership and ProductManagement and replace it with the values in "web/js/utils.js". You need to change
```
window.pm.options.address = '<Product Management contract address>'
window.co.options.address = '<Change Ownership contract address>'
```
Host the web folder with the help of this command 
```
http-server <foldername i.e web>
```
and visit the browser on the port ```localhost:8080```.

Now you can perform various tasks like from building parts and products to changing ownerships. 

Note: Build car by clicking on 6 parts and filing the serial number of the car.