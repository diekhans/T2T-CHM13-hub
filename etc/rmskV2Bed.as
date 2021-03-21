table rmskV2Bed
"RepeatMasker V2 structure with color"
    (
    string chrom;    "Genomic sequence name"
    uint chromStart;     "Start in genomic sequence"
    uint chromEnd;       "End in genomic sequence"
    string name;     "Family of repeat"
    uint score;       "always 0 place holder"
    char[1] strand;     "Relative orientation + or -"
    uint thickStart;   "Start of where display should be thick (start codon)"
    uint thickEnd;     "End of where display should be thick (stop codon)"
    uint reserved;     "color"
    uint swScore;       "Smith Waterman alignment score"
    string repClass;    "Class of repeat"
    string repSubClass;   "Subclass repeat"
    float repDiverence;   "divergence"
    )
