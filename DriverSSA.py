# -*- coding: utf-8 -*-
import sys
from Bid import Bid
from Slot import Slot
from Auction import Auction

'''
reads a file, constructs an Auction from it,
	prints the bids and slots info, calls the auction.executeVCG() method,
	and prints results
	@param fName	the name of the file to read data from
'''


def runAndPrint(filename):
    print ("loading Auction from file %s" % filename)
    print(" ")
    count = 0
    # CTR + price + profit + bidder

    slots = []
    # value + name
    bids = []
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            count += 1
            '''print count 1-6 '''
            # row1 dataset's name
            if count == 1:
                term = line
            # row2 CTR
            if count == 2:
                parts = line.split(' ')
                for ctr in parts:
                    slot = Slot(ctr)
                    slots.append(slot)
            # the rest row bid and advertisers' name
            if count > 2:
                bid = Bid(line)
                bids.append(bid)

    print ("Auction for \"%s\" with %d slots and %d bidders" % (term, len(slots), len(bids)))

    '''Slot.py 里面抓出来的'''
    for slot in slots:
        print("slot: %6.2f %8.2f %8.2f   %s" % (
            float(slot.clickThruRate), float(slot.price), float(slot.profit), slot.bidder))
    #print ("  <-- click through rates")
    print(" ")

    '''0123在 Auction 初始化的时候打印出来 应该是看有没有塞进去 Auction.bids里面 '''
    auction = Auction(term, bids)

    for b in auction.bids:
        # print ("%s\t%s"%(b.value,b.name))
        print ("bid:%6.2f %s" % (float(b.value), b.name))
    print(" ")
    #这里应该读入一个 slots executeVCG()里面有 但是这里似乎暂时没加上去 这样Auction里面才同时有 bids 和 slots
    auction.executeVCG(slots)
    print(" ")
    print("%12s %8s %8s %8s\n" % ("clicks", "price", "profit", "bidder"))
    for slot in slots:
        print("slot: %6.2f %8.2f %8.2f   %s" % (
            float(slot.clickThruRate), float(slot.price), float(slot.profit), slot.bidder))

    '''这三个应该是各个 column 的 sum的初始化'''
    cls = 0;
    rev = 0;
    val = 0;

    for s in slots:
        cls += float(s.clickThruRate);
        rev += s.price;
        val += s.profit;
    print ("sums: %6.2f %8.2f %8.2f\n" % (cls, rev, val))

'''主函数调用import的数据'''
if __name__ == '__main__':
    # runAndPrint("burgers.data.txt")
    # runAndPrint("etaMeson.data.txt")
    # runAndPrint("bicycleParts.data.txt")
    # runAndPrint("bicyclePartsDup.data.txt")
    # runAndPrint("jewelers5.data.txt")
     runAndPrint("jewelers8.data.txt")
