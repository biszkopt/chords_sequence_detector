class SequenceDetector:
	
	sequence = None
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
		
	def analyze(self, input_sequence):
		for elem in input_sequence:
			if elem is self.sequence[self.i_seq] or elem in self.alternatives[self.i_seq]:
				print(f'Sequence element {elem} at pos {self.i_seq} detected')
				self.i_seq += 1
				
				if self.i_seq == len(self.sequence):
					print('Entire sequence has been succesfully detected!')
					self.restart()
					return
				
				continue
		
			if elem in self.exceptions:
				if self.print_exceptions:
					print(f'Exception element {elem} detected')
				continue
			 
			if self.ignore_duplicates:
				if self.i_seq > 0 and elem is self.sequence[self.i_seq-1]:
					if self.print_duplicates:
						print(f'Sequence element {elem} duplicate detected')
					continue
					
			print(f'Incorrect sequence element {elem} detected, expected {self.sequence[self.i_seq]} at {self.i_seq} from sequence {self.sequence}')
			#self.restart()

					
					
						
			
				
						
				
		
		
			
			
			
		
		
	
	
