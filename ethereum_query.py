#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install web3==5.13.0 


# In[2]:


import web3
from web3 import Web3
from hexbytes import HexBytes


# In[3]:


IP_ADDR='18.188.235.196'
PORT='8545'


# In[4]:


w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))


# In[5]:


if w3.isConnected():
    print( "Connected to Ethereum node" )
else:
    print( "Failed to connect to Ethereum node!" )



# In[6]:


def getTransaction(tx):
    
    #YOUR CODE HERE
    tx = w3.eth.getTransaction(tx)  
    return tx



# In[7]:


tx = '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060'   


# In[8]:


# Return the gas price used by a particular transaction,
#   tx is the transaction
def getGasPrice(tx):
    
    #YOUR CODE HERE
    gasPrice = w3.eth.getTransaction(tx)['gasPrice'] 
    return gasPrice


# In[9]:


getGasPrice(tx)


# In[10]:


#that takes a transaction and returns the amount of gas used by the transaction.
def getGas(tx):
    
    #YOUR CODE HERE
    gas = 1 
    gas = w3.eth.getTransactionReceipt(tx)['gasUsed']
    return gas


# In[11]:


getGas(tx)


# In[12]:


def getTransactionCost(tx):
    
    #YOUR CODE HERE
    txCost = getGas(tx)*getGasPrice(tx)
    return txCost


# In[13]:


getTransactionCost(HexBytes(0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578))


# In[20]:


def getBlockCost(blockNum):
    
    #YOUR CODE HERE
    #given a block number,returns the total cost of all transactions in that block.
    #This is the amount that the miner of the block earns from transaction fees.
    #(The miner will additionally earn a reward of a certain number of ether from having mined a new block.)
    numTransaction = w3.eth.getBlockTransactionCount(blockNum)
    blockCost = 0
    for x in range(numTransaction):
        temp = w3.eth.getTransactionByBlock(blockNum, x)
        blockCost =  getTransactionCost(temp.hash) + blockCost


    #blockCost = w3.eth.getBlock(blockNum).gasUsed 
    return blockCost


# In[15]:


#getBlockCost(4022281)


# In[16]:


# given a block number, returns the hash of the most expensive transaction (as a HexBytes object)
# Return the hash of the most expensive transaction
def getMostExpensiveTransaction(blockNum):
    
    #YOUR CODE HERE
    numTransaction = w3.eth.getBlockTransactionCount(blockNum)
    maxTransaction = 0
    for x in range(numTransaction):
        temp = w3.eth.getTransactionByBlock(blockNum, x)
        #temp = w3.eth.get_transaction_by_block(blockNum,x)
        tempExpense = getTransactionCost(temp.hash)
        if tempExpense > maxTransaction:
            maxTransaction = tempExpense
            maxTx = temp.hash    
    
    #maxTx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  
    return maxTx


# In[17]:


#The highest price Ethereum has reached so far was approximately $1385.02 on Jan 12, 2018.
#One of the transactions that occurred on that day had the following hash:
#0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578
#Given the above price of Ether in USD, how much was the transaction fee for this transaction (in USD to the nearest cent)?etherPrice = 1385.02
#etherPrice = 1385.02
#transactionCost_wei = getTransactionCost('0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578')
#transactionCost_ether = transactionCost_wei/(10**18)
#transactionFee = transactionCost_ether*etherPrice
#print("this is the transaction fee:", transactionFee)


# In[21]:


#What was the average amount of Ether (to 2 decimal places) that was earned from transaction fees
#per block in the block range 10237100 to 10237109 (inclusive)?

#totalTransactionFee = 0
#numBlock = 10237109-10237100+1

#for x in range(10237100,10237110,1):
#    totalTransactionFee = totalTransactionFee + getBlockCost(x)
#aveTransactionFee_wei = totalTransactionFee/numBlock
#aveTransactionFee_ether = aveTransactionFee_wei/(10**18)
#print("this is the average ether cost per block:",aveTransactionFee_ether)
    


# In[22]:


#getMostExpensiveTransaction(10237208)


# In[23]:


#etherPrice = 248.26
#blockTransactionCost_wei = getBlockCost(10237208)
#print("this is blockTransactionCost_wei :", blockTransactionCost_wei)
#blockCost_ether = blockTransactionCost_wei/(10**18)
#blockReward = 2* etherPrice + blockCost_ether*etherPrice
#print("this is the reward for the block in $",blockReward)


# In[ ]:


#transactionCost_wei = getTransactionCost('0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578')
#transactionCost_ether = transactionCost_wei/(10**18)
#blockReward = 2* etherPrice + transactionCost_ether*etherPrice
#blockReward

