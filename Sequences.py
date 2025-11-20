# create the superclass
class Sequence:

    # constructor sets  shared attributes
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    # getters for shared attributes
    # getter for id
    @property
    def id(self):
        return self._id 

    # getter for seq
    @property
    def seq(self):
        return self._seq
    
    # special method shared by subclasses
    # prints the class attributes nicely
    def __str__(self):
        return f'Sequence Object: ID; {self.id}, \
Seq; {self.seq}'
    
    # returns the length of the sequence when len is called on an object
    def __len__(self):
        return len(self.seq)
    
    # iterates over the sequence if a for loop is run on the class
    def __iter__(self):
        return iter(self.seq)
    
    # return a fasta string
    def make_fasta(self):
        return f'>{self.id}\n{self.seq}\n'
    
# create the subclass
# inherits from Sequence
class DNASequence(Sequence):

    # don't need to add any shared content here!

    # these methods are only relevant for DNA sequences
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    # translate method
    def translate_seq(self):
        # make codon table
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        # do translation
        # use a list comprehension and join to make a string
        aa_list = [codon_table[self.seq[start:start+3]] for start in range(0, len(self.seq) -2, 3)]
        protein = ''.join(aa_list)
        return protein
        
    # this is a polymorphic function to get the protein length
    # // is a floor division
    def get_protein_len(self):
        return len(self.seq) // 3



# create the subclass
# inherits from Sequence
class ProteinSequence(Sequence):

    # constructor override
    # descr is optional, default is an empty string
    def __init__(self, id, seq, descr=''):
        # call the constructor from the super class to set shared attributes
        super().__init__(id, seq)
        # aslo set the unique attribute
        self._descr = descr

    # getter for descr attribute
    @property
    def descr(self):
        return self._descr

    # method specific for protein sequences
    def get_prop_hydrophobic(self):
        count_hydrophobic = 0
        hydrophobic = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
        for hydro in hydrophobic:
            count = self.seq.count(hydro)
            count_hydrophobic += count
        return count_hydrophobic / len(self.seq)
    
    # polymorphic method to get protein length
    def get_protein_len(self):
        return len(self.seq)
