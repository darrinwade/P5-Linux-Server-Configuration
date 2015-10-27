
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application_dbsetup import Base, Owner, Category, Item

import datetime

engine = create_engine('sqlite:///category.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#------------------------------------------

def addDBRec(objToAdd):
	""" Add a new record into the reference table specified table."""
	session.add(objToAdd)
	session.commit()

def deleteDBRec(objToDelete):
	""" Update a record into the reference table specified table."""
	session.delete(objToDelete)
	session.commit()

def updateDBRec(objToUpdate):
	""" Delete a record from the reference table specified table."""
	session.add(objToUpdate)
	session.commit()


print "\n\n\nStart of test load....\n\n\n"

# Load my test users
for iCnt in range(0, 1):
	userName  = "TestUser %04d" % (iCnt)
	userEmail = "Node%i.Node%i@xMail.com" % (iCnt,iCnt)
	userPic   = "No Pic Available"
	print "Adding Test User '%s'..." % (userName)
	OwnerObj = Owner(name=userName, email=userEmail, pic=userPic)
	#addDBRec(OwnerObj)
	#print "***  Added Test Owner record"

	oTmpOwner = session.query(Owner).filter_by(name=userName).first()
	for iCnt1 in range(0, 2):
		catname     = "Category Object Name - %s---%s" % (iCnt1, oTmpOwner.name)
		catdesc     = "Category Object Description - %s---%s" % (iCnt1, oTmpOwner.name)
		catownerid  = oTmpOwner.id
		CatObj      = Category(name=catname, desc=catdesc, owner_id=catownerid)
		#addDBRec(CatObj)
		#print "***      Added Test Category record"

		oTmpCategory = session.query(Category).filter_by(name=catname).first()
		for iCnt2 in range(0, 5):
			itemname     = "Category Item Object Name - %s---%s" % (iCnt2, oTmpCategory.name)
			itemdesc     = "Category Item Object Description - %s---%s" % (iCnt2, oTmpCategory.name)
			itemcreateDt = datetime.date.today()
			ItemObj      = Item(name=itemname, desc=itemdesc, owner_id=oTmpOwner.id, 
				category_id=oTmpCategory.id)
			#addDBRec(ItemObj)
			#print "***          Added Test Item record\n\n"


#---------------------------------------------------------
#OwnerObjs = session.query(Owner).all()
#for ownObj in OwnerObjs:
	#print "Name     - %s" % (ownObj.name)
	#print "Owner ID - %s" % (ownObj.id)
	#print "Email    - %s" % (ownObj.email)
	#print "Picture  - %s" % (ownObj.pic)
	#print "OwnerObj - %s\n\n" % (ownObj)

#CatObjs = session.query(Category).all()
#for CatObj in CatObjs:
	#print "Cat Name     - %s" %  (CatObj.name)
	#print "Cat ID       - %s" %  (CatObj.id)
	#print "Cat Desc     - %s" %  (CatObj.desc)
	#print "Cat Created  - %s" %  (CatObj.createDt)
	#print "Cat Modified - %s" %  (CatObj.modifyDt)
	#print "Cat Owner Id - %s" %  (CatObj.owner_id)
	#print "Cat Obj      - %s\n\n" % (CatObj)


###user, country = session.query(User, Country.country).join(Country).filter(User.user_email == 'abc@def.com').first()
###itm cat = session.query(Item,Category).join(Category).filter(Item.category_id=1).order_by(Item.createDt.desc()).limit(3).all()

###ItemObjs = session.query(Item).all()
ItemObjs = session.query(Item).order_by(Item.createDt.desc()).limit(10).all()
for ItemObj in ItemObjs:
	#print "Item Name     - %s" %  (ItemObj.name)
	#print "Item ID       - %s" %  (ItemObj.id)
	#print "Item Desc     - %s" %  (ItemObj.desc)
	#print "Item Created  - %s" %  (ItemObj.createDt)
	print "Item Modified - %s" %  (ItemObj.modifyDt)
	#print "Item Owner Id - %s" %  (ItemObj.owner_id)
	#print "Item Obj      - %s\n\n" % (ItemObj)

