import level_manager


level_manager = level_manager.LevelManager()
world = level_manager.get_current()
world.run()