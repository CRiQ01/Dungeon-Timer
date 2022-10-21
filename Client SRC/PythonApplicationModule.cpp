//Search 

PyModule_AddIntConstant(poModule, "CAMERA_STOP", CPythonApplication::CAMERA_STOP);

// Add after

#ifdef DUNGEON_LIST_TIME
	PyModule_AddIntConstant(poModule, "DUNGEON_LIST_TIME", 1);
#else
	PyModule_AddIntConstant(poModule, "DUNGEON_LIST_TIME", 0);
#endif