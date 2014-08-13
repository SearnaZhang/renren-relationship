# from renren import FriendsStore, RenRenRelationShip, RenRen
# from utils import get_accounts

# r = RenRen(*get_accounts())
# print r.get_friends()
import sys
import pickle
# with  open('renren_data','r') as f:
# 	print 'asldf'
# 	print pickle.load(f)

f = open('renren_data','r')
print pickle.load(f)
