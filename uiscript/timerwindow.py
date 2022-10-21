import uiScriptLocale
window = {
	"name" : "Window",
	"x" : (SCREEN_WIDTH - 850) / 2,
	"y" : (SCREEN_HEIGHT - 612) / 2,
	"style" : ("movable", "float",),
	"width" : 850,
	"height" : 612,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 850,
			"height" : 612,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 7,
					"width" : 850 - 15,
					"color" : "red",
					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -1, "text" : uiScriptLocale.QUEST_TIMER_TITLE, "all_align" : "center" },
					),
				},
				{
					"name" : "content",
					"type" : "image",
					"x" : 0,
					"y" : 23,
					"image" : "d:/ymir work/ui/game/dungeon_list/content.tga",
				},
				{
					"name" : "ItemSlot",
					"type" : "slot",
					"x" : 545,
					"y" : 200,
					"width" : 32,
					"height" : 32,
					"slot" :
					(
						{ "index" : 0, "x" : 0, "y" : 0, "width" : 32, "height" : 32 },
					),
				},
				{ "name" : "text1", "type" : "text", "x" : 358, "y" : 133, "text" : uiScriptLocale.QUEST_TIMER_REQ_LEVEL, },
				{ "name" : "text2", "type" : "text", "x" : 358, "y" : 151, "text" : uiScriptLocale.QUEST_TIMER_GROUP, },
				{ "name" : "text3", "type" : "text", "x" : 358, "y" : 169, "text" : uiScriptLocale.QUEST_TIMER_COOLDOWN, },
				{ "name" : "text4", "type" : "text", "x" : 358, "y" : 208, "text" : uiScriptLocale.QUEST_TIMER_TICKET, },
				{ "name" : "text5", "type" : "text", "x" : 45, "y" : -49, "text" : uiScriptLocale.QUEST_TIMER_DESC, "all_align" : "center" },
				{
					"name" : "Button",
					"type" : "button",
					"x" : 351,
					"y" : 566,
					"text" : "Teleport",
					"default_image" : "d:/ymir work/ui/game/dungeon_list/button_d.tga",
					"over_image" : "d:/ymir work/ui/game/dungeon_list/button_h.tga",
					"down_image" : "d:/ymir work/ui/game/dungeon_list/button_d.tga",
				},
				{
					"name" : "ScrollBar2",
					"type" : "scrollbar",

					"x" : 590 + 15,
					"y" : 28,

					"size" : 560 + 14,
				},
				{
					"name" : "RederTargetBossName", 
					"type" : "text",
					
					"text_horizontal_align" : "center",
					
					"x" : 724,
					"y" : 40,
					
					"text" : "Boss Preview",
				},
				{
					"name" : "RederTargetStoneName", 
					"type" : "text",
					
					"text_horizontal_align" : "center",
					
					"x" : 724,
					"y" : 325,
					
					"text" : "Stone Preview",
				},
			),
		},
	),
}
