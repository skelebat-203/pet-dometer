#poke-dometer
## Mood
- Mad
- Ok
- Likes
- Loves
### Upgrades
- Add a progress bar to see your progress up / down a level
- Difficulty setting to account for bad days.
### How it works
- You lose mood points if you don't walk
- You gain mood points by walking
- You can gain mood points by gifting resources. Max 999 resources at a time 
### Need to think through the conversion
- 10,000 resources = mood up / down grade
- Mood up / down through walking
	- There is an interaction component to this.
		- >3 interactions and you loose 10%
		- 4 - 5 no change
		- <5 +10%
	- If you walk >nn steps in a day you loose nn% of a mood level
		- There is a 1 day grace period
		- Love: >250 = -10% 
		- Like: >250 = -30%
		- Ok: >250 = -40%
		- Mad: lowest level
## Step counter / resource converter
20 steps = 1 resource
## Slot machine
Give it 5 resources you can get [0, 30, 50, 500]
## Giving resources to pet
- Range 0 - 999 at once.
- No limit per day
## Set clock
No flare. No daylight savings time.
## Animations
- slot machine
- eating
- reading
- RC car
- ball balancing
- get ready for bed
- swimming with fishes
- Possible new
	- seasonal
	- getting up in the morning
	- happy b-day
## New Features
- Multiple alarms
- Set date
	- Add seasonal animations
- Set date of birth
	- Happy b-day animation
- Alarm categories
	- wakeup (default 8am )
	- get ready for bed (default 10pm)
	- eating (no default)
	- get up and move (default every hour)
- Mood upgrades
	- Add a progress bar to see your progress up / down a level
	- Difficulty setting to account for bad days.
- Choose from multiple pets 