from random import randrange, choice


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''        maze            '''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Maze:
	"""
	Maze is a ROW x COL matrix. 
	Cell is an (i, j) pair. It has (up to) 4 neighbors that it can be connected with.
	The challenge is to get from top left corner to bottom right corner.
	"""

	def __str__(self):
		"""
		nice printable version of the maze.
		"""
		builder = ['╷', ' ↓ ', '╶' if self.are_connected((0, 0), (0, 1)) else '┌']

		for col in range(1, self.COLS):
			builder.append('───')
			builder.append('┐' if col + 1 == self.COLS else '─' if self.are_connected((0, col), (0, col + 1)) else '┬')
		builder.append('\n')

		for row in range(self.ROWS):

			builder.append('│')
			for col in range(self.COLS - 1):
				builder.append('   ')
				builder.append(' ' if self.are_connected((row, col), (row, col + 1)) else '│')
			builder.append('   │')
			builder.append('\n')

			if row + 1 < self.ROWS:
				builder.append('│' if self.are_connected((row, 0), (row + 1, 0)) else '├')
				for col in range(self.COLS):
					builder.append('   ' if self.are_connected((row, col), (row + 1, col)) else '───')
					if col + 1 == self.COLS:
						builder.append('│' if self.are_connected((row, col), (row + 1, col)) else '┤')
					else:
						top = self.are_connected((row, col), (row, col + 1))
						bottom = self.are_connected((row + 1, col), (row + 1, col + 1))
						right = self.are_connected((row, col + 1), (row + 1, col + 1))
						left = self.are_connected((row, col), (row + 1, col))

						builder.append(
							'┼' if (not top)	and		(not bottom)	and		(not right)		and		(not left)		else
							'├' if (not top)	and		(not bottom)	and		(not right)		and		(left)			else
							'┤' if (not top)	and		(not bottom)	and		(right)			and		(not left)		else
							'│' if (not top)	and		(not bottom)	and		(right)			and		(left)			else
							'┴' if (not top)	and		(bottom)		and		(not right)		and		(not left)		else
							'└' if (not top)	and		(bottom)		and		(not right)		and		(left)			else
							'┘' if (not top)	and		(bottom)		and		(right)			and		(not left)		else
							'╵' if (not top)	and		(bottom)		and		(right)			and		(left)			else
							'┬' if (top)		and		(not bottom)	and		(not right)		and		(not left)		else
							'┌' if (top)		and		(not bottom)	and		(not right)		and		(left)			else
							'┐' if (top)		and		(not bottom)	and		(right)			and		(not left)		else
							'╷' if (top)		and		(not bottom)	and		(right)			and		(left)			else
							'─' if (top)		and		(bottom)		and		(not right)		and		(not left)		else
							'╶' if (top)		and		(bottom)		and		(not right)		and		(left)			else
							'╴' if (top)		and		(bottom)		and		(right)			and		(not left)		else
							'·')
				builder.append('\n')

		builder.append('└')	
		for col in range(self.COLS - 2):
			builder.append('───')
			builder.append('─' if self.are_connected((row, col), (row, col + 1)) else '┴')
		builder.append('───')

		builder.append('╴' if self.are_connected((row, self.COLS - 2), (row, self.COLS - 1)) else '┘')

		builder.append(' ↓ ')
		builder.append('╵')

		return ''.join(builder)


	def __init__(self, rows, cols):
		"""
		create a random maze of ROWS x COLS cells.
		"""
		self.ROWS = rows
		self.COLS = cols

		self.connections = set()  # each element is a frozenset({cell1, cell2}) [cell is an (i, j) coordinates tuple]

		# for (i, j) in self.all_coordinates():
		# 	self.__connect((i, j), (i + 1, j))
		# 	self.__connect((i, j), (i, j + 1))

		self.__init_at_random()
	
	def all_coordinates(self):
		"""
		all cells in the maze.
		"""
		for i in range(self.ROWS):
			for j in range(self.COLS):
				yield (i, j)
	
	def is_in_grid(self, cell):
		"""
		True coordinates in the maze.
		False if you'd get an 'IndexError: list index out of range' exception
		"""
		i, j = cell
		return i in range(self.ROWS) and j in range(self.COLS)

	def __connect(self, cell1, cell2):
		"""
		mark the two cells as connected (order between them does not matter), so
		when printed, there will be no wall between them.
		"""
		edge = frozenset({cell1, cell2})
		self.connections.add(edge)

	def are_connected(self, cell1, cell2):
		"""
		True if self.__connect was called between them (order does not matter).
		"""
		edge = frozenset({cell1, cell2})
		return edge in self.connections

	def adjacent_cells(self, cell):
		"""
		yield 2 to 4 adjacent cells (2 if corner, 3 if at an edge, 4 if an inner cell) whether connected or not.
		"""
		deltas = (0, 1), (0, -1), (1, 0), (-1, 0)
		for d in deltas:
			neighbor = cell[0] + d[0], cell[1] + d[1]
			if self.is_in_grid(neighbor):
				yield neighbor
	
	def neighbors(self, cell):
		"""
		yield the 1 to 3 cells that are connected to given the cell.
		"""
		for adj in self.adjacent_cells(cell):
			if self.are_connected(cell, adj):
				yield adj

	def __init_at_random(self):
		"""
		random dfs manner
		"""
		start = randrange(self.ROWS), randrange(self.COLS)

		stack = [start]
		visited = {start}

		while stack:
			cell = stack.pop()
			unvisited_adjacent_cells = [c for c in self.adjacent_cells(cell) if c not in visited]
			if unvisited_adjacent_cells:
				stack.append(cell)
				neighbor = choice(unvisited_adjacent_cells)
				self.__connect(cell, neighbor)
				visited.add(neighbor)
				stack.append(neighbor)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''        main            '''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def get_dimensions_from_cmd_args():
	from sys import argv

	def display_help_and_exit():
		print(f'usage: \n\t python3 {argv[0]} <int num_rows> <int num_columns>')
		print(f'or \n\t python3 {argv[0]} -fill')
		exit()

	if len(argv) == 2 and argv[1] == '-fill':
		import shutil
		cols, rows = shutil.get_terminal_size((80, 20))
		rows = rows // 2 - 1
		cols = (cols - 1) // 4

	elif len(argv) == 1:
		print('what size do you want your maze to be? \n')
		display_help_and_exit()

	elif len(argv) == 3:
		try:
			rows, cols = int(argv[1]), int(argv[2])
			assert rows > 0 and cols > 1

		except ValueError:
			print('invalid arguments \n')
			display_help_and_exit()
		
		except AssertionError:
			print('invalid arguments \n')
			print('plase make (num_rows > 0) and (num_columns > 1)')
			exit()
	else:
		print('invalid arguments \n')
		display_help_and_exit()
	
	return (rows, cols)


def main():
	rows, cols = get_dimensions_from_cmd_args()
	maze = Maze(rows, cols)
	print(maze)

if __name__ == "__main__":
	main()
