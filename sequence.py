import math

# list of valid PP16 loci for entry validation
sites = ('D3S1358', 'TH01', 'D21S11', 'D18S51', 'PENTA-E', 'D5S818', 'D13S317', 'D7S820', 'D16S539', 'CSF1PO', 'PENTA-D', 'vWA', 'D8S1179', 'TPOX', 'FGA')
# creation of dictionary for final readout
final = {}

print('Type "done" to quit')
while True:
    site = input('Please input the STR locus: ')
    if site == 'done':
        break
    if site == 'final':
        print(final)
        break
    if site not in sites:
        print('Error: not a valid PowerPlex 16 locus')
        continue
    try:
        reps = float(input('reps?: '))
    except ValueError:
        print('Error: not a valid number')
        continue
    rep = int(reps)

    # BLUE
    # D3S1358
    if site == 'D3S1358':
        seq1 = 'TCTA'
        seq2 = 'TCTG'
        if 13 <= rep <= 14:
            D3S1358 = (seq1 + (seq2*2) + (seq1*(rep - 3)))
            final['D3S1358'] = D3S1358
            print(D3S1358)
        if 14 < rep <= 19:
            D3S1358 = (seq1 + (seq2*3) + (seq1*(rep-4)))
            final['D3S1358'] = D3S1358
            print(D3S1358)
    # TH01
    if site == 'TH01':
        seq1 = 'AATG'
        seq2 = 'ATG'
        seq3 = 'AACT'
        if rep == reps:
            # this is an integer
            TH01 = (seq1 * rep)
            final['TH01'] = TH01
            print(TH01)
        else:
            # this is a float (decimal)
            if reps < 11:
                TH01 = (seq1*(math.floor(reps)-3) + seq2 + seq1*3)
                final['TH01'] = TH01
                print(TH01)
            if reps == 13.3:
                TH01 = (seq1 + seq3 + (seq1*8) + seq2 + (seq1*3))
                final['TH01'] = TH01
                print(TH01)
    # D21S11
    if site == 'D21S11':
        print('aw hell naw')
     # D18S51
    if site == 'D18S51':
        seq1 = 'AGAA'
        D18S51 = (seq1 * rep)
        final['D18S51'] = D18S51
        print(D18S51)
    # PENTA-E
    if site == 'PENTA-E':
        seq1 = 'AAAGA'
        PENTAE = (seq1 * rep)
        final['PENTA-E'] = PENTAE
        print(PENTAE)
    # GREEN
    # D5S818
    if site == 'D5S818':
        seq1 = 'AGAT'
        D5S818 = (seq1 * rep)
        final['D5S818'] = D5S818
        print(D5S818)
    # D13S317
    if site == 'D13S317':
        seq1 = 'TATC'
        D13S317 = (seq1 * rep)
        final['D13S317'] = D13S317
        print(D13S317)
    # D7S820
    if site == 'D7S820':
        seq1 = 'GATA'
        D7S820 = (seq1 * rep)
        final['D7S820'] = D7S820
        print(D7S820)
    # D16S539
    if site == 'D16S539':
        seq1 = 'GATA'
        D16S539 = (seq1 * rep)
        final['D16S539'] = D16S539
        print(D16S539)
    # CSF1PO
    if site == 'CSF1PO':
        seq1 = 'AGAT'
        CSF1PO = (seq1 * rep)
        final['CSF1PO'] = CSF1PO
        print(CSF1PO)
    # PENTA-D
    if site == 'PENTA-D':
        seq1 = 'AAAGA'
        PENTAD = (seq1 * rep)
        final['PENTA-D'] = PENTAD
        print(PENTAD)
    # YELLOW
    # vWa
    if site == 'vWA':
        print('aw hell naw')
    # D8S1179
    if site == 'D8S1179':
        seq1 = 'TCTA'
        seq2 = 'TCTG'
        if rep <= 12:
            D8S1179 = (seq1 * rep)
            final['D8S1179'] = D8S1179
            print(D8S1179)
        if 12 < rep <= 15:
            D8S1179 =(seq1 + seq2 + (seq1*(rep - 2)))
            final['D8S1179'] = D8S1179
            print(D8S1179)
        if rep == 16 or rep == 18:
            D8S1179 =((seq1*2) + seq2 + (seq1*(rep - 3)))
            final['D8S1179'] = D8S1179
            print(D8S1179)
        if rep == 17 or rep == 19:
            D8S1179 =((seq1*2) + (seq2*2) + (seq1*(rep - 4)))
            final['D8S1179'] = D8S1179
            print(D8S1179)
        else:
            print('ERROR: the coder is lazy and hasnt gotten this far')
    # TPOX
    if site == 'TPOX':
        seq1 = 'AATG'
        TPOX = (seq1 * rep)
        final['TPOX'] = TPOX
        print(TPOX)
    # FGA
    if site == 'FGA':
        print('aw hell naw')
