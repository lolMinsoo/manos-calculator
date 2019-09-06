import random as rand
import math
import argparse
import os

global total_cost, average_accessory, average_c_black_crystal
total_cost = 0
average_accessory = 0
average_c_black_crystal = 0

global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
total_cost_armor = 0
average_memory_fragment = 0
average_armor_c_black_crystal = 0
average_armor_black_crystal = 0

# init
parser = argparse.ArgumentParser()
debug = True

# constants (prices) subject to change

# game constant
black_crystal = 1000000  # mp price 
c_black_crystal = (black_crystal * 5) + 3600000 + 1600000  # 5 black crystals + sharp + hard
bmc =  1500000  # average bmc price
manos_accessory = math.floor((36.36 * bmc) + 25000000 + (340000 * 100) + 1200000)  # magical shards + 5 manos + pure vanadium/titanium + essence of x 
memory_fragment = 2000000


		
# functions
def rng():
	return rand.randint(1, 100)  # inclusive, can roll 1 and 100
	
def _get_values():
	print('Black Crystal: 				{}'.format(black_crystal))
	print('Concentrated Black Crystal:		{}'.format(c_black_crystal))
	print('Black Magic Crystal:			{}'.format(bmc))
	print('Manos Accessories:			{}'.format(manos_accessory))
	print('Memory Fragment:			{}'.format(memory_fragment))
	
def parse_level(level):
	if(level.lower() == 'pri'):
		return 1
	elif(level.lower() == 'duo'):
		return 2
	elif(level.lower() == 'tri'):
		return 3
	elif(level.lower() == 'tet'):
		return 4
	else:
		return 5
		
		
def pen_acc_attempt(level):
	global total_cost, average_accessory, average_c_black_crystal
	if level == 5:
		total_cost += 20 * c_black_crystal
		average_c_black_crystal += 20
		if rng() <= 5:
			return 6
		else:
			return 1
	else:
		return tet_acc_attempt(level)
		
def tet_acc_attempt(level):
	global total_cost, average_accessory, average_c_black_crystal
	if level == 4:
		total_cost += 16 * c_black_crystal
		average_c_black_crystal += 16
		if rng() <= 15:
			return 5
		else:
			return 1
	else:
		return tri_acc_attempt(level)
		
		
def tri_acc_attempt(level):
	global total_cost, average_accessory, average_c_black_crystal
	if level == 3:
		total_cost += 13 * c_black_crystal
		average_c_black_crystal += 13
		if rng() <= 30:
			return 4
		else:
			return 1
	else:
		return duo_acc_attempt(level)
		
def duo_acc_attempt(level):
	global total_cost, average_accessory, average_c_black_crystal
	if level == 2:
		total_cost += 11 * c_black_crystal
		average_c_black_crystal += 11
		if rng() <= 45:
			return 3
		else:
			return 1
	else:
		return pri_acc_attempt(level)
		
def pri_acc_attempt(level):
	global total_cost, average_accessory, average_c_black_crystal
	total_cost += manos_accessory + 10 * c_black_crystal
	average_c_black_crystal += 10
	average_accessory += 1
	if rng() <= 75:
		return 2
	else:
		return 1
		
def calculate_cost_accessory():
	manos_level = parse_level(manos.level)
	for i in range(manos.iterations):
		print('Currently on iteration: {}/{}'.format(i+1, manos.iterations))
		level = 1
		while level != (manos_level + 1):
			if manos_level == 1:
				level = pri_acc_attempt(level)
			elif manos_level == 2:
				level = duo_acc_attempt(level)
			elif manos_level == 3:
				level = tri_acc_attempt(level)
			elif manos_level == 4:
				level = tet_acc_attempt(level)
			else:
				level = pen_acc_attempt(level)
			
			
			
	print('With {} iterations, it took an average of {} manos accessories, {} concentrated black crystals, with an average cost of {}.'.format(
		manos.iterations, average_accessory/manos.iterations, average_c_black_crystal/manos.iterations, total_cost/manos.iterations))
		
def mem_fragment():
	global average_memory_fragment
	if manos.art:
		average_memory_fragment += 2.5
		return memory_fragment * 2.5
	else:
		average_memory_fragment += 10
		return memory_fragment * 10
		
def roll_success(chance):
	attempts = 0
	succeed = False
	while not succeed:
		if rng() <= chance:
			succeed = True
			attempts += 1
		else:
			attempts += 1
	return attempts
			
def one_to_pri():
	global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
	total_cost_armor += 5 * average_armor_black_crystal  # 1 to 5
	attempts = roll_success(90)
	average_armor_black_crystal += attempts * 2
	total_cost_armor += (attempts * 2 * black_crystal) + ((attempts - 1) * mem_fragment())  # 6
	attempts = roll_success(80)
	average_armor_black_crystal += attempts * 2
	total_cost_armor += (attempts * 2 * black_crystal) + ((attempts - 1) * mem_fragment())  # 7
	attempts = roll_success(70)
	average_armor_black_crystal += attempts * 2
	total_cost_armor += (attempts * 2 * black_crystal) + ((attempts - 1) * mem_fragment())  # 8
	attempts = roll_success(60)
	average_armor_black_crystal += attempts * 3
	total_cost_armor += (attempts * 3 * black_crystal) + ((attempts - 1) * mem_fragment())  # 9
	attempts = roll_success(50)
	average_armor_black_crystal += attempts * 3
	total_cost_armor += (attempts * 3 * black_crystal) + ((attempts - 1) * mem_fragment())  # 10
	attempts = roll_success(40)
	average_armor_black_crystal += attempts * 3
	total_cost_armor += (attempts * 3 * black_crystal) + ((attempts - 1) * mem_fragment())  # 11
	attempts = roll_success(30)
	average_armor_black_crystal += attempts * 4
	total_cost_armor += (attempts * 4 * black_crystal) + ((attempts - 1) * mem_fragment())  # 12
	attempts = roll_success(20)
	average_armor_black_crystal += attempts * 4
	total_cost_armor += (attempts * 4 * black_crystal) + ((attempts - 1) * mem_fragment())  # 13
	attempts = roll_success(15)
	average_armor_black_crystal += attempts * 5
	total_cost_armor += (attempts * 5 * black_crystal) + ((attempts - 1) * mem_fragment())  # 14
	attempts = roll_success(10)
	average_armor_black_crystal += attempts * 5
	total_cost_armor += (attempts * 5 * black_crystal) + ((attempts - 1) * mem_fragment())  # 15
	attempts = roll_success(30)
	average_armor_c_black_crystal += attempts
	total_cost_armor += (attempts * 1 * c_black_crystal) + ((attempts - 1) * mem_fragment())  # pri


def pen_arm_attempt(level):
	global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
	if level == 5:
		average_armor_c_black_crystal += 1
		if rng() <= 6:
			total_cost_armor += c_black_crystal
			return level + 1
		else:
			total_cost_armor += c_black_crystal + mem_fragment()
			
			return level - 1
	return tet_arm_attempt(level)
	
	
	
def tet_arm_attempt(level):
	global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
	if level == 4:
		average_armor_c_black_crystal += 1
		if rng() <= 15:
			total_cost_armor += c_black_crystal
			return level + 1
		else:
			total_cost_armor += c_black_crystal + mem_fragment()
			return level - 1
	return tri_arm_attempt(level)
	
	
def tri_arm_attempt(level):
	global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
	if level == 3:
		average_armor_c_black_crystal += 1
		if rng() <= 20:
			total_cost_armor += c_black_crystal
			return level + 1
		else:
			total_cost_armor += c_black_crystal + mem_fragment()
			return level - 1
	return duo_arm_attempt(level)
	
	
def duo_arm_attempt(level):
	global total_cost_armor, average_memory_fragment, average_armor_c_black_crystal, average_armor_black_crystal
	average_armor_c_black_crystal += 1
	if rng() <= 25:
		total_cost_armor += c_black_crystal
		return level + 1
	else:
		total_cost_armor += c_black_crystal + mem_fragment()
		return 2
		
		
def calculate_cost_armor():
	manos_level = parse_level(manos.level)
	for i in range(manos.iterations):
		print('Currently on iteration: {}/{}'.format(i+1, manos.iterations))
		one_to_pri()
		level = 2
		while level != (manos_level + 1):
			if manos_level == 2:
				level = duo_arm_attempt(level)
			elif manos_level == 3:
				level = tri_arm_attempt(level)
			elif manos_level == 4:
				level = tet_arm_attempt(level)
			elif manos_level == 5:
				level = pen_arm_attempt(level)
				
	if(manos.art):
		print('With {} iterations, it took an average of {} black crystals, {} concentrated black crystals, {} memory fragments, {} artisan memories.'.format(manos.iterations, average_armor_black_crystal/manos.iterations, 
																																							average_armor_c_black_crystal/manos.iterations, average_memory_fragment/
																																							manos.iterations, (average_memory_fragment*2.5)/(4*manos.iterations)))
		print('For a total of {} silver and {} pearls (assuming 100 bundle)'.format((average_armor_black_crystal/manos.iterations)*black_crystal + (average_armor_c_black_crystal/manos.iterations)*c_black_crystal + (average_memory_fragment/manos.iterations)*memory_fragment, (average_memory_fragment*2.5*40)/(manos.iterations*4)))
	else:
		print('With {} iterations, it took an average of {} black crystals, {} concentrated black crystals, {} memory fragments.'.format(manos.iterations, average_armor_black_crystal/manos.iterations, 
																																							average_armor_c_black_crystal/manos.iterations, average_memory_fragment/
																																							manos.iterations, (average_memory_fragment)/(manos.iterations)))
		print('For a total of {} silver.'.format((average_armor_black_crystal/manos.iterations)*black_crystal + (average_armor_c_black_crystal/manos.iterations)*c_black_crystal + (average_memory_fragment/manos.iterations)*memory_fragment))
		
		
parser.add_argument('-enhance', action='store_true', default=False, dest='enhance')
parser.add_argument('-level', action='store', dest='level')
parser.add_argument('-price', action='store_true', default=False, dest='price')
parser.add_argument('-it', action='store', dest='iterations', type=int)
parser.add_argument('-acc', action='store_true', default=False, dest='acc')
parser.add_argument('-arm', action='store_true', default=False, dest='arm')
parser.add_argument('-art', action='store_true', default=False, dest='art')
manos = parser.parse_args()

if(manos.price):
	_get_values()

if(manos.enhance):
	if(manos.acc):
		calculate_cost_accessory()
	if(manos.arm):
		calculate_cost_armor()

