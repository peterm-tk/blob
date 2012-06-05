import blob.Animation as Anim
import blob.Box as Box
import blob.FileIO as IO
import blob.System as blob
import blob.Player as Player
import blob.Level as Level
import sf

def test():
	system = blob.System()
	system.create_window(640,480,b'Test')
	system.window.framerate_limit = 60 #default value

	#font = sf.Font.load_from_file(b'arial.ttf')

	textures = IO.load_texture_list("face")
	
	# Need to do this for all custom in-game classes
	Box.set_default_texture_list(textures)
	Player.set_default_texture_list(textures)

	box = Box.Box()
	player = Player.Player()
	level = Level.Level()

	level.add(box)
	level.add(player)

	box.move(10,10)
	
	box.reinit()
	player.reinit()

	running = True
	while running:
		#Docs: http://pysfml2-cython.readthedocs.org/en/latest/events.html
		for event in system.window.iter_events():
			if event.type == sf.Event.CLOSED:
				running = False
			if event.type == sf.Event.KEY_PRESSED:
				if event.code == sf.Keyboard.ESCAPE:
					running = False
				if event.code == sf.Keyboard.F:
					enable = True
		
		player.reset_acc()
		player.process_controls(system)

		#if box.current_animation().is_done():
		#	if box.animation_chosen == "fast":
		#		box.change_animation("default")
		#		print("default")
		#	else:
		#		box.change_animation("fast")
		#		print("fast")
		
		level.animate()
		level.do_movement()

		system.window.clear(sf.Color.WHITE)
		level.draw(system.window)
		system.display()
	
	#system.exit()
	print("Done")

if __name__ == '__main__':
	test()
