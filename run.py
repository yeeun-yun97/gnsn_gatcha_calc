import os


ONE_GATCHA_GENSEKI=160
TRUCK_OF_GENSEKI=8080
PRICE_OF_TRUCK=13
GATCHA_FULL_EXPECTED=65

#your pull count after you got 5 star
currentStack=30
#your genseki count
gensekiLeft=0
#if you got pickup 5 star recently, false
pickUpMode=False
#your goal of pickUp character count
goalPickUp=4


pickUpCount=0
truckCount=0
while(pickUpCount<goalPickUp):
	needGensekiCount=(GATCHA_FULL_EXPECTED-currentStack)*ONE_GATCHA_GENSEKI
	while(needGensekiCount>gensekiLeft):
		truckCount+=1
		gensekiLeft+=8080
	gensekiLeft-=needGensekiCount
	currentStack=0
	if(pickUpMode):
		pickUpCount+=1
	pickUpMode=not pickUpMode

os.system("cat info.txt")
os.system(f"echo 당신은 총 {goalPickUp}회의 픽업 캐릭터를 원했습니다.")
os.system(f"echo 당신이 충전한 횟수는 {truckCount}회입니다.")
os.system(f"echo 당신은 총 {truckCount*PRICE_OF_TRUCK}만원을 사용하였습니다.")






