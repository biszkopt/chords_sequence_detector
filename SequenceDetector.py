class SequenceDetector:
	
	sequence = None
	matches = None
	i_seq = 0
	exceptions = None
	alternatives = None
	ignore_duplicates = True
	print_duplicates = True
	print_exceptions = True
	detected = False
	
	def restart(self):
		self.detected = False
		self.i_seq = 0
		self.matches = len(self.sequence) * [False]
		
	def analyze(self, input_sequence):
		for elem in input_sequence:

			elem_match = False

			if elem is self.sequence[self.i_seq]:
				print(f'{elem} at pos {self.i_seq} detected')
				elem_match = True

			if elem in self.alternatives[self.i_seq]:
				print(f'{elem} at pos {self.i_seq} detected (alternative)')
				elem_match = True

			if elem_match:

				self.matches[self.i_seq] = True
				self.i_seq += 1

				if self.i_seq == len(self.sequence):
					print('Entire sequence has been succesfully detected!')
					self.restart()
					return

				continue
		
			if elem in self.exceptions:
				if self.print_exceptions:
					print(f'Exception: {elem}')
				continue

			if self.ignore_duplicates:
				if self.i_seq > 0 and elem is self.sequence[self.i_seq-1]:
					if self.print_duplicates:
						print(f'{elem} duplicate detected')
					continue
					
			print(f'Error: {elem} detected, expected {self.sequence[self.i_seq]} at {self.i_seq} from sequence {self.sequence}')
			#self.restart()


					
						
			
				
						
				
		
		
			
			
			
		
		
	
	
