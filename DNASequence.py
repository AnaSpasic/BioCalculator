
class DNASequence:
    
    # class attribute: number of created instances of class 
    count_sequences = 0
    
    valid = {'A', 'G', 'T', 'C'}
    
    
    def __init__ (self, seq, ID):
        self.seq = seq
        self.ID = ID
        DNASequence.count_sequences += 1
        
        
    def is_valid_sequence (self):       
       a = True
       
       for nt in self.seq:   
           if nt not in DNASequence.valid: 
               a = False
               break  
       return a
   
    
    def seq_len (self):
        return len(self.seq)
    
    
    def count_nucleotides (self):
        count = {'A':0, 'G':0, 'T':0, 'C':0}
        
        for nt in self.seq:
            for n in count:
                if nt == n:
                    count[n] = count[n] + 1
        return(count)
        
    
    def GC_content (self):
        a = self.count_nucleotides() 
        return (a['G'] + a['C']) / self.seq_len()  
    
    
    def unique_nucleotides (self):
        nt_set = set()

        for nt in self.seq:
            if nt in DNASequence.valid:
                nt_set.add(nt)
                if nt_set == DNASequence.valid:
                    break
        return nt_set
    
    
    def transcribe_to_rna (self):
        rna = self.seq.replace('T', 'U')
        
        return rna
         
           
                   
                   