#Add 

if app.DUNGEON_LIST_TIME:
	import uitimerwindow
    
#Search 
	def OpenLetterEvent(self):
		self.LetterEvent.Show()	

#Add after

	if app.DUNGEON_LIST_TIME:
		def __MakeTimerWindow(self):
			self.wndTimer = uitimerwindow.TimerWindow()
			self.wndTimer.LoadWindow()

#Search
		self.questButtonList = []

#Add after 

		if app.DUNGEON_LIST_TIME:
			self.__MakeTimerWindow()
            
#Search

		self.__InitWhisper()

#Add before

		if app.DUNGEON_LIST_TIME:
			self.wndTimer.SetToolTip(self.tooltipItem)

#Search

		if self.wndGameButton:
			self.wndGameButton.Destroy()

#Add after

		if app.DUNGEON_LIST_TIME:
			if self.wndTimer:
				self.wndTimer.Destroy()
                
#Search

		del self.wndItemSelect
        
#Add after

		if app.DUNGEON_LIST_TIME:	
			del self.wndTimer

#Search

	def ShowGift(self):
		self.wndTaskBar.ShowGift()
        
#Add after

	if app.DUNGEON_LIST_TIME:
		def OpenTimerWindow(self):
			self.wndTimer.Open()
			
		def SetQuestTimer(self, index, time):
			self.wndTimer.SetTimeLeft(index, time)
			
		def refreshDungeonStatus(self):
			self.wndTimer.OnUpdate()