import ui
import app
import net
import localeInfo
import chat
import uiCommon 
import renderTarget
import grp

#DUNGEON_AND_MAP_START
DESCRIPTION = {
	0 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/dt.tga", "Demon Tower (Dungeon)", 40, "Optional", "No time", 99099, None, None, None, None, None, None  ],                      #DEMON_TOWER_DUNGEON_40_TO_120
	1 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/baroneasa.tga", "Baroness (Dungeon)", 55, "Yes", "30 minutes", 30324, None, None, None, None, None, None  ],                    #BARONESE_DUNGEON_55_TO_80
	2 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/slime.tga", "Slime Dungeon (Dungeon)", 65, "Yes", "1 hour", 30723, None, None, None, None, None, None  ],                       #SLIME_DUNGEON_65_TO_80
	3 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/bluedragon.tga", "Blue Dragon (Dungeon)", 75, "Optional", "No time", 30179, None, None, None, None, None, None  ],              #BLUE_DRAGON_DUNGEON_75_TO_105
	4 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/dragonv.tga", "Dragon Valley (Map)", 75, "Optional", "No time", 90645, None, None, None, None, None, None  ],                   #DRAGON VALEY_MAP_75_TO_105
	5 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/shark.tga", "Shark Cave (Map)", 75, "Optional", "No time", 90643, None, None, None, None, None, None  ],                        #SHARK_CAVE_MAP_75_TO_105
	6 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/biblioteca.tga", "Cursed Library (Dungeon)", 75, "Optional", "1 hour", 30811, None, None, None, None, None, None  ],            #CURSED_LIBRARY_DUNGEON_75_TO_105
	7 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/cave.tga", "Magic Cave (Map)", 80, "Optional", "No time", 90640, None, None, None, None, None, None  ],                         #MAGIC_CAVE_MAP_80_TO_105
	8 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/azrael.tga", "Azrael (Dungeon)", 80, "Optional", "1 hour", 30319, None, None, None, None, None, None  ],                        #AZRAEL_DUNGEON_80_TO_120
	9 : [ "d:/ymir work/ui/game/dungeon_list/info_image_map/purgatory.tga", "Razador's Purgatory (Dungeon)", 95, "Optional", "1 hour", 71173, None, None, None, None, None, None  ],        #RAZADOR_DUNGEON_95_TO_12
	10 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/nemerestower.tga", "Nemere's Tower (Dungeon)", 95, "Optional", "1 hour", 71173, None, None, None, None, None, None  ],          #NEMERE_DUNGEON_95_TO_120
	11 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/vale.tga", "Ghost Valley (Map)", 90, "Optional", "No time", 90642, None, None, None, None, None, None  ],                       #GHOST_VALERRY_MAP_90_TO_120
	12 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/ganish.tga", "Ganesha Ruins (Dungeon)", 105, "Optional", "1 hour", 30794, None, None, None, None, None, None  ],                #GANISHA_DUNGEON_95_TO_120
	13 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/natural.tga", "Natural Map (Map)", 105, "Optional", "No time", 90644, None, None, None, None, None, None  ],                    #NATURAL_MAP_105_TO_120
	14 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/sufering.tga", "Desert of Suffering (Map)", 110, "Optional", "No time", 90641, None, None, None, None, None, None  ],            #SAND_MAP_110_TO_120
	15 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/mine.tga", "Mining Cave (Map)", 30, "Optional", "No time", 90646, None, None, None, None, None, None  ],                        #MINING_MAP_30_TO_120
	16 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/hidra.tga", "Hydra Ship Defense (Dungeon)", 110, "Optional", "No time", None, None, None, None, None, None, None  ],            #HIDRA_DUNGEON_110_TO_120
	17 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/zodiac.tga", "Zodiac Temple (Dungeon)", 120, "Optional", "No time", None, None, None, None, None, None, None  ],                #ZODIAC_DUNGEON_120_TO_120
	18 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/incoming.tga", "Incoming", 95, "Optional", "No time", None, None, None, None, None, None, None  ],                              #TEST_FUTURE_MAP_OR_DUNGEONS
	19 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/incoming.tga", "Incoming", 95, "Optional", "No time", None, None, None, None, None, None, None  ],                              #TEST_FUTURE_MAP_OR_DUNGEONS
	20 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/incoming.tga", "Incoming", 95, "Optional", "No time", None, None, None, None, None, None, None  ],                              #TEST_FUTURE_MAP_OR_DUNGEONS
	21 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/incoming.tga", "Incoming", 95, "Optional", "No time", None, None, None, None, None, None, None  ],                              #TEST_FUTURE_MAP_OR_DUNGEONS
	22 :[ "d:/ymir work/ui/game/dungeon_list/info_image_map/incoming.tga", "Incoming", 95, "Optional", "No time", None, None, None, None, None, None, None  ],}                             #TEST_FUTURE_MAP_OR_DUNGEONS
#DUNGEON_AND_MAP_END

#DUNGEON_AND_MAP_INFO_DROP_IMAGE_START
DESCRIPTION1 = {
	0 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/00.dt.tga"],                                    #IMAGE_WITH_DROP_FOR:   #### DEMON_TOWER_DUNGEON
	1 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/01.baroneasa.tga"],                             #IMAGE_WITH_DROP_FOR:   #### BARONESE_DUNGEON
	2 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/02.slime.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### SLIME_DUNGEON
	3 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/03.bluedragon.tga"],                            #IMAGE_WITH_DROP_FOR:   #### BLUE_DRAGON_DUNGEON
	4 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/04.dragonv.tga"],                               #IMAGE_WITH_DROP_FOR:   #### DRAGON VALEY_MAP
	5 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/05.shark.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### SHARK_CAVE_MAP
	6 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/06.biblioteca.tga"],                            #IMAGE_WITH_DROP_FOR:   #### CURSED_LIBRARY_DUNGEON
	7 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/07.cave.tga"],                                  #IMAGE_WITH_DROP_FOR:   #### MAGIC_CAVE_MAP
	8 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/08.azrael.tga"],                                #IMAGE_WITH_DROP_FOR:   #### AZRAEL_DUNGEON
	9 : [ "d:/ymir work/ui/game/dungeon_list/info_drop_image/09.purgatory.tga"],                             #IMAGE_WITH_DROP_FOR:   #### RAZADOR_DUNGEON
	10 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/10.nemerestower.tga"],                          #IMAGE_WITH_DROP_FOR:   #### NEMERE_DUNGEON
	11 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/11.vale.tga"],                                  #IMAGE_WITH_DROP_FOR:   #### GHOST_VALERRY_MAP
	12 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/12.ganish.tga"],                                #IMAGE_WITH_DROP_FOR:   #### GANISHA_DUNGEON
	13 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/13.natural.tga"],                               #IMAGE_WITH_DROP_FOR:   #### NATURAL_MAP
	14 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/14.sufering.tga"],                              #IMAGE_WITH_DROP_FOR:   #### SAND_MAP
	15 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/15.mine.tga"],                                  #IMAGE_WITH_DROP_FOR:   #### MINING_MAP
	16 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/16.hidra.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### HIDRA_DUNGEON
	17 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/17.zodiac.tga"],                                #IMAGE_WITH_DROP_FOR:   #### ZODIAC_DUNGEON
	18 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/incoming.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	19 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/incoming.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	20 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/incoming.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	21 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/incoming.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	22 :[ "d:/ymir work/ui/game/dungeon_list/info_drop_image/incoming.tga"],                                 #IMAGE_WITH_DROP_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
}
#DUNGEON_AND_MAP_INFO_DROP_IMAGE_START

#DUNGEON_AND_MAP_INFO_PENDANT_FOR_BOSS_IMAGE_START
DESCRIPTION2 = {
	0 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/dark.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### DEMON_TOWER_DUNGEON
	1 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### BARONESE_DUNGEON
	2 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/nature.tga"],                #IMAGE_WITH_PENDANT_BOSS_FOR:   #### SLIME_DUNGEON
	3 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/ice.tga"],                   #IMAGE_WITH_PENDANT_BOSS_FOR:   #### BLUE_DRAGON_DUNGEON
	4 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga",],                #IMAGE_WITH_PENDANT_BOSS_FOR:   #### DRAGON VALEY_MAP
	5 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/fire.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### SHARK_CAVE_MAP
	6 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/fire.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### CURSED_LIBRARY_DUNGEON
	7 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/ice.tga"],                   #IMAGE_WITH_PENDANT_BOSS_FOR:   #### MAGIC_CAVE_MAP
	8 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/dark.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### AZRAEL_DUNGEON
	9 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/fire.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### RAZADOR_DUNGEON
	10 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/ice.tga"],                   #IMAGE_WITH_PENDANT_BOSS_FOR:   #### NEMERE_DUNGEON
	11 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/dark.tga"],                  #IMAGE_WITH_PENDANT_BOSS_FOR:   #### GHOST_VALERRY_MAP
	12 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/nature.tga"],                #IMAGE_WITH_PENDANT_BOSS_FOR:   #### GANISHA_DUNGEON
	13 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/nature.tga"],                #IMAGE_WITH_PENDANT_BOSS_FOR:   #### NATURAL_MAP
	14 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### SAND_MAP
	15 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### MINING_MAP
	16 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### HIDRA_DUNGEON
	17 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### ZODIAC_DUNGEON
	18 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	19 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	20 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	21 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	22 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                 #IMAGE_WITH_PENDANT_BOSS_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
}
#DUNGEON_AND_MAP_INFO_PENDANT_FOR_BOSS_IMAGE_END

#DUNGEON_AND_MAP_INFO_PENDANT_FOR_STONE_IMAGE_START
DESCRIPTION3 = {
	0 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### DEMON_TOWER_DUNGEON
	1 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### BARONESE_DUNGEON
	2 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/nature.tga"],                 #IMAGE_WITH_PENDANT_STONE_FOR:   #### SLIME_DUNGEON
	3 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### BLUE_DRAGON_DUNGEON
	4 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga",],                 #IMAGE_WITH_PENDANT_STONE_FOR:   #### DRAGON VALEY_MAP
	5 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/fire.tga"],                   #IMAGE_WITH_PENDANT_STONE_FOR:   #### SHARK_CAVE_MAP
	6 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/fire.tga"],                   #IMAGE_WITH_PENDANT_STONE_FOR:   #### CURSED_LIBRARY_DUNGEON
	7 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/ice.tga"],                    #IMAGE_WITH_PENDANT_STONE_FOR:   #### MAGIC_CAVE_MAP
	8 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### AZRAEL_DUNGEON
	9 : [ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### RAZADOR_DUNGEON
	10 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### NEMERE_DUNGEON
	11 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### GHOST_VALERRY_MAP
	12 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/nature.tga"],                 #IMAGE_WITH_PENDANT_STONE_FOR:   #### GANISHA_DUNGEON
	13 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### NATURAL_MAP
	14 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/earth.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### SAND_MAP
	15 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### MINING_MAP
	16 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### HIDRA_DUNGEON
	17 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### ZODIAC_DUNGEON
	18 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	19 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	20 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	21 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
	22 :[ "d:/ymir work/ui/game/dungeon_list/info_pendan_slot/empty.tga"],                  #IMAGE_WITH_PENDANT_STONE_FOR:   #### TEST_FUTURE_MAP_OR_DUNGEONS
}
#DUNGEON_AND_MAP_INFO_PENDANT_FOR_BOSS_IMAGE_END

class TimerBoard(ui.ImageBox):
	def __init__(self, parent, index):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.index = index
		self.parent = parent
		self.__Build()


	def __del__(self):
		ui.ImageBox.__del__(self)

	def __Build(self):
			
		self.LoadImage("d:/ymir work/ui/game/dungeon_list/available.tga")
			
		self.Show()

		self.image = ui.MakeImageBox(self, ("d:/ymir work/ui/game/dungeon_list/info_image_slot/%d.tga" % self.index), 3, 3)

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetPosition(46, -10)
		self.textLine.SetWindowHorizontalAlignLeft()
		self.textLine.SetHorizontalAlignLeft()
		self.textLine.SetText(DESCRIPTION[self.index][1])

		self.textLine2 = ui.MakeTextLine(self)
		self.textLine2.SetPosition(8, 0)
		self.textLine2.SetWindowHorizontalAlignRight()
		self.textLine2.SetHorizontalAlignRight()
		self.textLine2.SetText(localeInfo.QUEST_TIMER_AVAILABLE)
		
		self.textLine3 = ui.MakeTextLine(self)
		self.textLine3.SetPosition(46, 7)
		self.textLine3.SetWindowHorizontalAlignLeft()
		self.textLine3.SetHorizontalAlignLeft()
		self.textLine3.SetText("Cool Down 00:00:00")
		
		self.incoming = ui.MakeTextLine(self)
		self.incoming.SetPosition(150, 0)
		self.incoming.SetWindowHorizontalAlignLeft()
		self.incoming.SetHorizontalAlignLeft()
		self.incoming.SetText("Soon")

		self.endTime = 0

	def SetTimeLeft(self, time):
		self.endTime = app.GetGlobalTimeStamp() + time

	def UpdateTime(self, indexNum):
		if self.endTime - app.GetGlobalTimeStamp() > 0:
			m, s = divmod(self.endTime - app.GetGlobalTimeStamp(), 60)
			h, m = divmod(m, 60)
			self.textLine3.SetText("%02d:%02d:%02d" % (h, m, s))
			self.textLine2.SetText(localeInfo.QUEST_TIMER_UNAVAILABLE)
			self.incoming.SetText("")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/unavailable.tga")
		else:
			self.textLine3.SetText("00:00:00")
			self.textLine2.SetText(localeInfo.QUEST_TIMER_AVAILABLE)
			self.incoming.SetText("")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/available.tga")
			
		if indexNum > 15:
			self.textLine3.SetText("")
			self.textLine2.SetText("")
			self.incoming.SetText("Soon")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/unavailable.tga")
	
	def OnMouseLeftButtonDown(self):
		self.parent.SetDescription(self.index)

	def Destroy(self):
		self.image = None
		self.image1 = None
		self.imagePendant = None
		self.imagePendantStone = None
		self.textLine = None
		self.textLine2 = None
		self.textLine3 = None
		
class TimerWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		
		self.LoadWindow()
		self.index = 0
		self.DungeonScrollBar = None
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/timerwindow.py")
		except:
			import exception
			exception.Abort("TimerWindow.LoadWindow.LoadObject")

		try:
			self.titleBar = self.GetChild("TitleBar")
			self.itemSlot = self.GetChild("ItemSlot")
			self.teleport = self.GetChild("Button")
			self.scrollBarDungeon = self.GetChild("ScrollBar2")
		except:
			import exception
			exception.Abort("TimerWindow.LoadWindow.BindObject")

		self.titleBar.SetCloseEvent(ui.mem_func(self.Close))

		self.itemSlot.SetOverInItemEvent(ui.mem_func(self.__OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.mem_func(self.__OnOverOutItem))

		self.teleport.SetEvent(ui.mem_func(self.Teleport))

		self.timerBoards = []
		for x in xrange(19):
			board = TimerBoard(self, x)
			board.SetPosition(23, 50 * (x + 1) - 7)
			self.timerBoards.append(board)

		self.tooltip = None

		self.image = ui.ImageBox()
		self.image.SetParent(self)
		self.image.SetPosition(342, 36)

		self.image1 = ui.ImageBox()
		self.image1.SetParent(self)
		self.image1.SetPosition(345, 280)

		self.imagePendant = ui.ImageBox()
		self.imagePendant.SetParent(self)
		self.imagePendant.SetPosition(845, 70)
		
		self.imagePendantStone = ui.ImageBox()
		self.imagePendantStone.SetParent(self)
		self.imagePendantStone.SetPosition(845, 360)

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetPosition(342 - 178 - 111, 36 - 85 - 142)

		self.textLine2 = ui.MakeTextLine(self)
		self.textLine2.SetPosition(263, -167)
		self.textLine2.SetWindowHorizontalAlignRight()
		self.textLine2.SetHorizontalAlignRight()

		self.textLine3 = ui.MakeTextLine(self)
		self.textLine3.SetPosition(263, -150)
		self.textLine3.SetWindowHorizontalAlignRight()
		self.textLine3.SetHorizontalAlignRight()

		self.textLine4 = ui.MakeTextLine(self)
		self.textLine4.SetPosition(263, -133)
		self.textLine4.SetWindowHorizontalAlignRight()
		self.textLine4.SetHorizontalAlignRight()

		self.index = 0
		self.SetDescription(0) #default

		self.scrollBarDungeon.SetPosition(605, 27)
		self.scrollBarDungeon.SetScrollBarSize(579) 
		self.scrollBarDungeon.SetScrollEvent(ui.mem_func(self.OnScroll))
		self.scrollBarDungeon.SetPos(0.0)
		self.RefreshShowList()

	def OnScroll(self):
		self.RefreshShowList()

	def RefreshShowList(self):
		for btn in self.timerBoards:
			btn.Hide() 

		yPos = 50
		totalCount = len(self.timerBoards)
		showCount = max(0, totalCount - 11)
		showStart = int(showCount * self.scrollBarDungeon.GetPos())
		showIndex = 0

		for c in self.timerBoards:
			showIndex += 1
			if showIndex < showStart:
				c.Hide()
			else:		
				c.SetPosition(22, yPos)
				c.Show()
				yPos += 48
				
				if yPos > 600:
					c.Hide()
					
	def GetBossByDungeonID(self):
		if self.index == 0:
			return 1093 #DEMON_TOWER_DUNGEON_BOSS
			
		if self.index == 1:
			return 2092 #BARONESE_DUNGEON_BOSS
	
		if self.index == 2:
			return 768 #SLIME_DUNGEON_BOSS
	
		if self.index == 3:
			return 2493 #BLUE_DRAGON_DUNGEON_BOSS
		
		if self.index == 4:
			return 996 #DRAGON_VALEY_MAP_BOSS
		
		if self.index == 5:
			return 4305 #SHARK_CAVE_MAP_BOSS
		
		if self.index == 6:
			return 4311 #CURSED_LIBRARY_DUNGEON_BOSS
		
		if self.index == 7:
			return 841 #MAGIC_CAVE_MAP_BOSS
		
		if self.index == 8:
			return 2598 #AZRAEL_DUNGEON_BOSS
		
		if self.index == 9:
			return 6091 #RAZADOR_DUNGEON_BOSS
		
		if self.index == 10:
			return 6191 #NEMERE_DUNGEON_BOSS
		
		if self.index == 11:
			return 4326 #GHOST_VALERRY_MAP_BOSS
		
		if self.index == 12:
			return 4110 #GANISHA_DUNGEON_BOSS
		
		if self.index == 13:
			return 880 #NATURAL_MAP_BOSS
		
		if self.index == 14:
			return 4138 #SAND_MAP_BOSS
		
		if self.index == 15:
			return 20015 #MINING_MAP_NPC
		
		return -1
		
	def GetStoneByDungeonID(self):
		if self.index == 0:
			return 8016 #DEMON_TOWER_DUNGEON_STONE
			
		if self.index == 1:
			return 2095 #BARONESE_DUNGEON_STONE
	
		if self.index == 2:
			return 8430 #SLIME_DUNGEON_STONE
	
		if self.index == 3:
			return 8021 #BLUE_DRAGON_DUNGEON_STONE
		
		if self.index == 4:
			return 8419 #DRAGON_VALEY_MAP_STONE
		
		if self.index == 5:
			return 8479 #SHARK_CAVE_MAP_STONE
		
		if self.index == 6:
			return 8481 #CURSED_LIBRARY_DUNGEON_STONE
		
		if self.index == 7:
			return 8404 #MAGIC_CAVE_MAP_STONE
		
		if self.index == 8:
			return 8482 #AZRAEL_DUNGEON_STONE
		
		if self.index == 9:
			return 8482 #RAZADOR_DUNGEON_STONE
		
		if self.index == 10:
			return 8482 #NEMERE_DUNGEON_STONE
		
		if self.index == 11:
			return 8483 #GHOST_VALERRY_MAP_STONE
		
		if self.index == 12:
			return 8468 #GANISHA_DUNGEON_STONE
		
		if self.index == 13:
			return 8407 #NATURAL_MAP_STONE
		
		if self.index == 14:
			return 8471 #SAND_MAP_STONE
		
		if self.index == 15:
			return 20047 #MINING_MAP_NPC
		
		return -1
		
	def __ModelPreview(self, Vnum):

		self.ModelPreviewBoard = ui.ThinBoard()
		self.ModelPreviewBoard.SetParent(self)
		self.ModelPreviewBoard.SetSize(200+10, 230+30-12)
		self.ModelPreviewBoard.SetPosition(600+25, 65)
		self.ModelPreviewBoard.Show()
	
		self.ModelPreview = ui.RenderTarget()
		self.ModelPreview.SetParent(self.ModelPreviewBoard)
		self.ModelPreview.SetSize(200, 230)
		self.ModelPreview.SetPosition(5, 22-12)
		self.ModelPreview.SetRenderTarget(2)
		self.ModelPreview.Show()

		self.EyeXSliderBar = ui.SliderBar()
		self.EyeXSliderBar.SetParent(self.ModelPreview)
		self.EyeXSliderBar.SetPosition(12, 29 + 3 + 1 * 20 + 165)
		self.EyeXSliderBar.SetSliderPos(0.5)
		self.EyeXSliderBar.backGroundImage.OnMouseLeftButtonDown = self.SeekSliderPosEyeX
		self.EyeXSliderBar.cursor.OnMouseRightButtonDown = self.ResetSliderPosEyeX
		self.EyeXSliderBar.SetEvent(ui.mem_func(self.OnChangeEyeX))
		self.EyeXSliderBar.Show()
			
			
		renderTarget.SetBackground(2, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(2, True)
		renderTarget.SelectModel(2, Vnum)

	def ResetSliderPosEyeX(self):
		self.EyeXSliderBar.SetSliderPos(0.5)
		apply(self.EyeXSliderBar.eventChange, [])

	def SeekSliderPosEyeX(self):
		if self.EyeXSliderBar.GetSliderPos() < 0.5 and float(self.EyeXSliderBar.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar.backGroundImage.GetWidth()) > 0.5 or self.EyeXSliderBar.GetSliderPos() > 0.5 and float(self.EyeXSliderBar.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar.backGroundImage.GetWidth()) < 0.5:
			self.EyeXSliderBar.SetSliderPos(0.5)
		else:
			self.EyeXSliderBar.SetSliderPos(float(self.EyeXSliderBar.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar.backGroundImage.GetWidth()))
		apply(self.EyeXSliderBar.eventChange, [])
		
	def OnChangeEyeX(self):
		pos = self.EyeXSliderBar.GetSliderPos()
		i = (pos*60) #aici se schimba zoom
		renderTarget.SetZoom(2, i)
		
	def __ModelPreviewClose(self):

		if self.ModelPreviewBoard:
			self.ModelPreviewBoard.Hide()
			
			if self.ModelPreview:
				self.ModelPreview.Hide()

				self.ModelPreviewBoard = None
				self.ModelPreview = None

			renderTarget.SetVisibility(2, False)

	def __StoneModelPreview(self, Vnum):
	
		self.StoneModelPreviewBoard = ui.ThinBoard()
		self.StoneModelPreviewBoard.SetParent(self)
		self.StoneModelPreviewBoard.SetSize(200+10, 230+30-12)
		self.StoneModelPreviewBoard.SetPosition(600+25, 350)
		self.StoneModelPreviewBoard.Show()
	
		self.StoneModelPreview = ui.RenderTarget()
		self.StoneModelPreview.SetParent(self.StoneModelPreviewBoard)
		self.StoneModelPreview.SetSize(200, 230)
		self.StoneModelPreview.SetPosition(5, 22-12)
		self.StoneModelPreview.SetRenderTarget(3)
		self.StoneModelPreview.Show()

		self.EyeXSliderBar2 = ui.SliderBar()
		self.EyeXSliderBar2.SetParent(self.StoneModelPreview)
		self.EyeXSliderBar2.SetPosition(12, 29 + 3 + 1 * 20 + 165)
		self.EyeXSliderBar2.SetSliderPos(0.5)
		self.EyeXSliderBar2.backGroundImage.OnMouseLeftButtonDown = self.SeekSliderPosEyeX2
		self.EyeXSliderBar2.cursor.OnMouseRightButtonDown = self.ResetSliderPosEyeX2
		self.EyeXSliderBar2.SetEvent(ui.mem_func(self.OnChangeEyeX2))
		self.EyeXSliderBar2.Show()
		
		renderTarget.SetBackground(3, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(3, True)
		renderTarget.SelectModel(3, Vnum)

	def ResetSliderPosEyeX2(self):
		self.EyeXSliderBar2.SetSliderPos(0.5)
		apply(self.EyeXSliderBar2.eventChange, [])

	def SeekSliderPosEyeX2(self):
		if self.EyeXSliderBar2.GetSliderPos() < 0.5 and float(self.EyeXSliderBar2.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar2.backGroundImage.GetWidth()) > 0.5 or self.EyeXSliderBar.GetSliderPos() > 0.5 and float(self.EyeXSliderBar.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar.backGroundImage.GetWidth()) < 0.5:
			self.EyeXSliderBar2.SetSliderPos(0.5)
		else:
			self.EyeXSliderBar2.SetSliderPos(float(self.EyeXSliderBar2.backGroundImage.GetMouseLocalPosition()[0])/float(self.EyeXSliderBar2.backGroundImage.GetWidth()))
		apply(self.EyeXSliderBar2.eventChange, [])
		
	def OnChangeEyeX2(self):
		pos = self.EyeXSliderBar2.GetSliderPos()
		i = (pos*60) #aici se schimba zoom
		renderTarget.SetZoom(3, i)
	
	def __StoneModelPreviewClose(self):

		if self.StoneModelPreviewBoard:
			self.StoneModelPreviewBoard.Hide()
			
			if self.StoneModelPreview:
				self.StoneModelPreview.Hide()

				self.StoneModelPreviewBoard = None
				self.StoneModelPreview = None

			renderTarget.SetVisibility(3, False)
	
	def SetDescription(self, index):
		self.index = index
		self.image.LoadImage(DESCRIPTION[index][0])
		self.image1.LoadImage(DESCRIPTION1[index][0])
		self.imagePendant.LoadImage(DESCRIPTION2[index][0])
		self.imagePendantStone.LoadImage(DESCRIPTION3[index][0])
		self.textLine.SetText(DESCRIPTION[index][1])
		self.itemSlot.SetItemSlot(0, DESCRIPTION[index][5])
		self.image.Show()
		self.image1.Show()
		self.imagePendant.Show()
		self.imagePendantStone.Show()
		self.textLine2.SetText(str(DESCRIPTION[index][2]))
		self.textLine3.SetText(str(DESCRIPTION[index][3]))
		self.textLine4.SetText(str(DESCRIPTION[index][4]))
		
		self.__ModelPreview(self.GetBossByDungeonID())
		self.__StoneModelPreview(self.GetStoneByDungeonID())

	def SetTimeLeft(self, index, time):
		self.timerBoards[index].SetTimeLeft(time);
	
	def SetToolTip(self, tooltip):
		self.tooltip = tooltip
		self.tooltip.Hide()

	def __OnOverInItem(self, slotIndex):
		self.tooltip.SetItemToolTip(DESCRIPTION[self.index][5])

	def __OnOverOutItem(self):
		self.tooltip.HideToolTip()

				
	def Teleport(self):		
		dialog = uiCommon.QuestionDialog()
		dialog.SetText(localeInfo.DO_TIMER_TELEPORT_WINDOW)
		dialog.SetAcceptEvent(ui.mem_func(self.AcceptTeleport))
		dialog.SetCancelEvent(ui.mem_func(self.OnCancelAccept))
		dialog.Open()
		self.dialog = dialog
		self.Close()

	def AcceptTeleport(self):
		if self.index >= 23:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[Information] - This dungeon is currently unavailable")
			return
		else:
			net.SendChatPacket("/timer_teleport %d" % self.index)
			
		self.OnCancelAccept()

	def OnCancelAccept(self):
		if self.dialog:
			self.dialog.Close()
		
		self.dialog = None
		return True
			
			
	def Open(self):
		self.__ModelPreview(self.GetBossByDungeonID())
		self.__StoneModelPreview(self.GetStoneByDungeonID())
		self.Show()

	def Close(self):
		self.__ModelPreviewClose()
		self.__StoneModelPreviewClose()
		self.Hide()

	def OnUpdate(self):
		for x in xrange(19):
			self.timerBoards[x].UpdateTime(x)
			
	def OnScrollWheel(self, len):
		if len >= 0:
			self.scrollBarDungeon.OnUp()
		else:
			self.scrollBarDungeon.OnDown()
		return True
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.scrollBarDungeon.OnUp()
		else:
			self.scrollBarDungeon.OnDown()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Destroy(self):
		self.ClearDictionary()
		self.image = None
		self.image1 = None
		self.imagePendant = None
		self.imagePendantStone = None
		self.textLine = None
		self.textLine2 = None
		self.textLine3 = None
		self.textLine4 = None
		self.titleBar = None
		self.itemSlot = None
		self.teleport = None
		self.scrollBarDungeon = None
		self.ModelPreviewBoard = None
		self.ModelPreview = None
		self.StoneModelPreviewBoard = None
		self.StoneModelPreview = None
		for t in self.timerBoards:
			t.Destroy()
			t = None
		del self.timerBoards[:]
