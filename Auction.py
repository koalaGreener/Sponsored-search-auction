#!/usr/bin/python
import Bid, Slot

class Auction:
	"""This class represents an auction of multiple ad slots to multiple advertisers"""
	query = ""
	bids = []

	def __init__(self, term, bids1=[]):
		self.query = term
		
		for b in bids1:
			j=0
			print len(self.bids)
			while j<len(self.bids) and b.value <self.bids[j].value:
				j+=1
			self.bids.insert(j,b)

	'''
	This method accepts a Vector of slots and fills it with the results
	of a VCG auction. The competition for those slots is specified in the bids Vector.
	@param slots a Vector of Slots, which (on entry) specifies only the clickThruRates
	and (on exit) also specifies the name of the bidder who won that slot,
	the price said bidder must pay,
	and the expected profit for the bidder.  
	'''

	def executeVCG(slots):
		# TODO: implement this method
		print ("executeVCG: To be implemented")
