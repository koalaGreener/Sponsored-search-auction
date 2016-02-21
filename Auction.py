#!/usr/bin/python
import Bid, Slot

class Auction:
	"""This class represents an auction of multiple ad slots to multiple advertisers"""
	query = ""
	bids = []

	def __init__(self, term, bids1=[]):
		self.query = term
		
		for b in bids1:
			j = 0
			while j < len(self.bids) and b.value < self.bids[j].value:
			    j += 1
			#print len(self.bids), b.value, j
			self.bids.insert(j, b)



	'''
	This method accepts a Vector of slots and fills it with the results
	of a VCG auction. The competition for those slots is specified in the bids Vector.
	@param slots a Vector of Slots, which (on entry) specifies only the clickThruRates
	and (on exit) also specifies the name of the bidder who won that slot,
	the price said bidder must pay,
	and the expected profit for the bidder.  
	'''
    # slots bids
	def executeVCG(self, slots):
         count = 0
         for slot in slots:
             #price
             tempPrice = 0.0
             withoutValue = 0.0
             withinValue = 0.0

             for i in range( count + 1, len(self.bids) ):
                 withoutValue += (slots[i - 1].clickThruRate * 1.0 * self.bids[i].value  )

             for j in range( count + 1, len(self.bids) ):
                 withinValue += (slots[j].clickThruRate * 1.0 * self.bids[j].value)

             tempPrice = (withoutValue - withinValue) * 1.0 / slot.clickThruRate
             slot.price = tempPrice

             #profit
             slot.profit = (self.bids[count].value - slot.price) * slot.clickThruRate

             #bidder
             slot.bidder = self.bids[count].name
             count += 1





