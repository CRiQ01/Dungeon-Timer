//Add

#ifdef DUNGEON_LIST_TIMER
ACMD(do_timer_teleport);
ACMD(do_open_dungeon_list);
#endif

//Inside struct command_info cmd_info[] =
//Add

#ifdef DUNGEON_LIST_TIMER
	{ "timer_teleport",				do_timer_teleport,	0,	POS_DEAD,	GM_PLAYER	},
	{ "open_dungeon_list",				do_open_dungeon_list,	0,	POS_DEAD,	GM_PLAYER	},
#endif