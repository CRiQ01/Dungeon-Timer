// CHANGE DATA WITH YOURS
// ADD AT THE END OF THE FILE

#ifdef DUNGEON_LIST_TIMER
ACMD(do_timer_teleport)
{
	int xPos, yPos, mapIndex, maxLevel, contor;
	int minLevel = 1;
	bool isBlock = false;

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	str_to_number(contor, arg1);

	switch (contor)
	{
		case 0:	//TURNUL DEMONILOR
			minLevel = 40; maxLevel = 120; xPos = 590300; yPos = 111100; mapIndex = 65;
			break;

		case 1:	//BARONESA	TIMER
			minLevel = 55; maxLevel = 80; xPos = 68900; yPos = 611000; mapIndex = 217;
			break;

		case 2:	//SLIME	DUNGEON
			minLevel = 65; maxLevel = 80; xPos = 299000; yPos = 4900; mapIndex = 67;
			break;

		case 3:	//DRAGON ALBASTRU
			minLevel = 75; maxLevel = 105; xPos = 182800; yPos = 1220600; mapIndex = 73;
			break;

		case 4:	//DRAGON	VALLERY
			minLevel = 75; maxLevel = 105; xPos = 2113900; yPos = 3548500; mapIndex = 401;
			break;

		case 5:	//SHARK	MAP
			minLevel = 75; maxLevel = 105; xPos = 1057300; yPos = 2281200; mapIndex = 76;
			break;

		case 6:	//BIBLIOTECA BLESTEMATILOR	TIMER
			minLevel = 75; maxLevel = 105; xPos = 1115835; yPos = 53412; mapIndex = 68;
			break;

		case 7:	//PESTERA	MAGICA	MAP
			minLevel = 80; maxLevel = 105; xPos = 2119100; yPos = 2406700; mapIndex = 74;
			break;

		case 8:	//AZRAEL
			minLevel = 80; maxLevel = 120; xPos = 592000; yPos = 100000; mapIndex = 65;
			break;

		case 9:	//RAZADOR	TIMER
			minLevel = 95; maxLevel = 120; xPos = 599400; yPos = 707300; mapIndex = 62;
			break;

		case 10:	//NEMERE	TIMER
			minLevel = 95; maxLevel = 120; xPos = 432000; yPos = 164500; mapIndex = 61;
			break;

		case 11:	//VALEA	FANTOMELOR	MAP
			minLevel = 90; maxLevel = 120; xPos = 1239897; yPos = 2320321; mapIndex = 78;
			break;

		case 12:	//GANISHA DUNGEON	TIMER
			minLevel = 95; maxLevel = 120; xPos = 1115835; yPos = 53412; mapIndex = 68;
			break;

		case 13:	//NATURAL_MAP
			minLevel = 105; maxLevel = 120; xPos = 2149077; yPos = 2666807; mapIndex = 400;
			break;

		case 14:	//DESERTUL	SUFERINTEI	MAP
			minLevel = 110; maxLevel = 120; xPos = 654437; yPos = 2365913; mapIndex = 57;
			break;

		case 15:	//MINERIT	MAP
			minLevel = 30; maxLevel = 120; xPos = 3004189; yPos = 4956240; mapIndex = 34;
			break;

		default:
			return;
	}

	if (ch->GetLevel() < minLevel)
		isBlock = true;

	if (ch->GetLevel() > maxLevel)
		isBlock = true;

	if (isBlock)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You must have the minimum level %d and the maximum level %d", minLevel, maxLevel);
		return;
	}

	if (contor == 7) // MAGIC_CAVE_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90640) > 0)
		{
			ch->RemoveSpecifyItem(90640, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 14) // DESERT_OF_SUFFERING_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90641) > 0)
		{
			ch->RemoveSpecifyItem(90641, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 11) // GHOST_VALLERY_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90642) > 0)
		{
			ch->RemoveSpecifyItem(90642, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 5) // SHARK_CAVE_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90643) > 0)
		{
			ch->RemoveSpecifyItem(90643, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 13) // NATURAL_MAP_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90644) > 0)
		{
			ch->RemoveSpecifyItem(90644, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 4) // DRAGON_MAP_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90645) > 0)
		{
			ch->RemoveSpecifyItem(90645, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	if (contor == 15) // MINEREU_MAP_REQUESTED_ITEM
	{
		if (!ch->CanWarp())
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not do that!");
			return;
		}
			
		if (ch->CountSpecifyItem(90646) > 0)
		{
			ch->RemoveSpecifyItem(90646, 1);
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("The necessary ticket has been taken, I will teleport you to this map!"));
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Sorry, but I can't find the ticket to teleport you on this map!"));
			return;
		}
	}

	// Additional checks

	if (ch->IsDead())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You are dead.");
		return;
	}

	if (!ch->IsHack() || ch->CanWarp())
		ch->WarpSet(xPos, yPos, mapIndex);

	// Additional checks
	
	// Reset everything
	
	maxLevel = 0;
	xPos = 0;
	yPos = 0;
	mapIndex = 0;
	isBlock = false;
	
	// Reset everything
}

ACMD(do_open_dungeon_list)
{
	char buf[CHAT_MAX_LEN + 1];
	snprintf(buf, sizeof(buf), "BINARY_DungeonList_Open");
	ch->ChatPacket(CHAT_TYPE_COMMAND, buf);	
}
#endif