#Search
def __ServerCommand_Build(self):
		serverCommandList={
        ...
        ...
        ...
        }


#Add after

		if app.DUNGEON_LIST_TIME:
			serverCommandList.update({"SetQuestTimer"			: self.SetQuestTimer,})
			serverCommandList.update({"refreshDungeonStatus"			: self.__RefreshDungStatus,})
			serverCommandList["BINARY_DungeonList_Open"]=self.OpenTimerWindow
            
            
#Add at the end of the file 

	if app.DUNGEON_LIST_TIME:
		def OpenTimerWindow(self):
			self.interface.OpenTimerWindow()

		def SetQuestTimer(self, index, time):
			self.interface.SetQuestTimer(int(index), int(time))

		def __RefreshDungStatus(self):
			self.interface.refreshDungeonStatus()	