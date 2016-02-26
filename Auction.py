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
         # count is the index of bids[], and we will also use it to calculate with CTR
         count = 0
         for slot in slots:
             #calculated the price
             tempPrice = 0.0
             # WithoutValue means the first slot without the relative advertisers, so that we can calculate the lost of others
             withoutValue = 0.0
             withinValue = 0.0
             # Two different situations when the bids' length not equals to the slots' length
             indexGap = 0
             if len(self.bids) <= len(slots):
                 indexGap = 0
             else:
                 indexGap = 1

             for i in range(count + 1, self.smallOne(len(self.bids) , len(slots)) + indexGap ):
                 withoutValue += (1.0 * self.bids[i].value * slots[i - 1].clickThruRate)

             for j in range( count + 1,  self.smallOne(len(self.bids) , len(slots))):
                 withinValue += (1.0 * self.bids[j].value * slots[j].clickThruRate)

             tempPrice = (withoutValue - withinValue) * 1.0 / slot.clickThruRate
             slot.price = tempPrice

             #profit
             slot.profit = (self.bids[count].value - slot.price) * slot.clickThruRate

             #bidder
             slot.bidder = self.bids[count].name
             count += 1

             if(self.smallOne(len(self.bids) , len(slots)) <= count):
                 break

        # choose the smaller number and then output
        def smallOne(self, a, b):
            if a <= b:
                return a
            else:
                return b





