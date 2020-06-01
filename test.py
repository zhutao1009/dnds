from dnds import dnds
a='ATGTGCACTAAGTTCTGGGTTGCACCTCCAGCTGATGGCACAGAGGAGATTGCCACTGTCAAGCTGCTTATCACAGGCCAAGGAGTCAGTATTGAGGAGAAGAAAAAGGTCCTGATCCACAAGGCAAACAGTGGCACCTTCATTCAAATGGACAAGCCCATCTATAAACCAGGGCAAACAGTGAAATTTCGTATTGTGACTCTGGATGAGGACTTCATTGCACTTAATGATTCGATTTCCGTGTTTCTCCAGGACCCTAACAACAACCGGATAGAGCAGTGGCTGAACGTGGTGCCCCAAGATGGCATTGCAGATCTGTCTTTCCAGCTAAGTGATGAGCCTCTGCTGGGGACATATGTCATCAATGTAACCAACAGGAAAATATATGACAGCTTCACCGTTGAGGAGTATGTGCTGCCAAGATTTGAAGTGATCTTTGAGGCACCAATTAAGATTTATGCACTAGATGAAACCTTCCCACTCCGGGTATGTGGCAGATACACCTATGGGAAAGCTGTCCAGGGGATGGTTTATGTGAGTCTTTGTCAGAAGATATCTCAGTTCTTACCCAGTGCTTCGAAACCTGATCTCTGTCAGGAATTCTACAACCAGACAGACAATATGGGTTGCTTCTTCACAAATGTGACACTATCCTTCAGCCGAGACTTCCGATACTATCAGGACAGCATAGTTGCAGAGGCCTCACTGGTGGAAGATGGCACAGAGATACAGGTCAATGCATCCCACAAATTACTCATTTCCAAGATTGGCGGAATGGCCTTGTTTGATGATGTGAATTCTTACTACCATGCTGGAGAGATGTACAGGGGGAAGATCAAAGTCATTGACTACAAAGGCAAGATGCTGAAGTACAAAAAAGTCCTCCTTGTAGTAAGCAGTGGTGAGCAGCAGTTTCAGCAAAAGTACCTCACTGGGGACACTGGAACAGCTTCGTTTAGCCTGAATACAACTGCTTGGAACAGCACCTCAGCCTCCCTGGAGGTAAGTGTCCTGCATCAAGATTTGGATACAGAGCCTGGGACAATTGATTTGAGTTACCAGAAAGCCTCTCATTTCATACATCCATTCTACAGCACCAGCAAGAGTTTTCTCACTATTGTCCGTGTGCCAGAAACGATGCCCTGTGGTAAAAAGCAGGCTATCCAGGTGGACTTCAGAATCTATCAGGAAGACCTGGAACATGGGCCCAAGCGTGTCATTTTCTCCTACTTTGTCACGGGGAAAAGAGGGATAGTCCATGCAGGCCAGAAGACTGTTTGGGTTGGGCTGCCAAGAATGCTGAAAGGCTTCTTCTCCATCCCTGTTACCTTCAGCTCAGTCTATGCTCCAGCTTCAACACTTATTGTTTATGTTATCTTCCCTAATGGAAAAATCATTGCTGATTCTGCCACCTTCAGTGTCTCCACATGTTTCAGAAATAAGGCAGAGCTGAGCTTCTCAGTGCCCAAGATTCTTCCTGGTTCAGAGGTTAATCTCCACCTGCTGGCAGCTCCTGGGTCCACATGTGCTGTCTGGGCTGTGGATCAGAGTGCCTTTTTGCTGAAGCCAGAGAAAGAACTCAGCCACTCTATGATCTATGGGCTCTTTCCATCTATTCCATCTACATACTCCGGGTATCCTCGCCAAGTGTCTGAAGATGATCATTCATGCGGGTTCCCAAATTCTGACGAGCTTGATGTGTTTACAGCATTCAGGGAAGTGGGGTTGAAAATTATGTCCAACACCAATATCAGGAAACCAAGACTGTGTCTAACTACTCAGTCAACAACTATGCTGCAGGAAACAGGGATGTTCACTTCCAGGCCCATGTTGATGTTTGCTCAGCCTCATAAGGAATCTAACACAGGACATCTGATGACATCTACCTATCAGCCCACTATGTTTTCACCTGTTTCTCCAGCTGAAGAGAAAGTGCACAAACATTTCACAAAAACCTGGATATGGGATTTGTATTCTGTCGGTCCCAGTGGAAAACAGACTGTCACTGTCACTGTACCTAACACCATCACAGAATGGAAAGCAGGGATGTTCTGCACAGGACGTAATGGCTTTGGACTTGCTCCAACCTCCAGTCTGCTTGTTTTCAAGCCCTTTTTTGTGGAGCTCACACTGCCATCTTCTGTGATCCAGGGTGAGACCTTCACCTTGAAGGCCACAGTCTTCAACTACCTGCAACAATGTATGAAGATCCAAGTGACTATGGAGGAGTTCACACACTTCCAGCTGAAGCCATGTGAAGGCTGTGTCTACAGCAGCTGCTTATGTGCTGGAGAAGCTAAAACATTTCAGTGGAGTGTCACAGCTGAGCGACTAGGGTTCACGAACATCACTCTCAGCACAGAGGCCGTGGCCACAAAGAGCTCTGTGGCAAAGAGATACCATTTGTCCCAAACCAAGGACAGAAAGACACAATCACCAAACTCCTTTTATTTGGTGCAGAGTAATTCTAGGACTTGTCCCTTGTTATTCAAGGAGAATCTCTGGCTTGGACCAAAATTTTGTCTGTATCTATTTGTAATCCACTGTTTCTCTCGTATGTACTCATTACTGCTACTTTCAAATGCTCAACAGCCAGAGGGAGTGCTAGTGGAAAAGGCTCACAGCTCCATCCTGTGTCCCAAAAAAGGGAGTCCAGCAGAGGAGTCTGTGTCCTTAACGTTGCCTCCAAATACGGTTGAAGGTTCAGTGAGAGCTACTGTCTCAGTCACTGGTGACCTCATGGGGACTGCACTGCAGAACTTGGACCACCTGGTGCATATGCCCCATGGCTGTGGGGAGCAGAACATGGTGCTGTTTGCCCCCATTGTCTATGTGCTGCAGTACCTGGAGAAGACGGGACAGATGACCCCTGAAATCAAGGAGAGGGCAACGGGATTCCTGCGCAATGGGTACCAGATACAGCTGCAGTATCAACACCCTGATGGTTCTTTCAGTGAATTTGGTACCAAGGATGAGTACGGTAATACTTGGCTGACTGCATTTGTGGTCAAATGCTTTGTCCAAGCCAAACCATACATTTTCCTGGACAATAGGAGCATCCAAGCTGCTCTCAACTGGCTGGAGTTCCACCAGCTTCCTAATGGGTGTTTCAGAAACGTGGGCCAGCTTTTTCACACAGCCATGAAAGGAGGTATGGATGGGGAAGTTCTCTTGGCTGCCTACATCACTGCTGCATACATGGAGAGAGGAGATACACCAGAGAGTACGGTGGTGCGCAAGGCTCTGGGCTGCATTGCTCCTTCCCTCCCCAAAGCTGCCAGCACTTACACACAGGCCCTCCTGGCCTACACCTTTGCCCTGGCTAAGGACCAGCAACGTACACAAGAGCTTCTCGACATGCTTGATCAAAAGGCAATCAGAGCAGGTGGGCAGATCCACTGGAGTCAGAGCCCATCCAAGGCACACAGCACTAGCCTTTGGTCACAGCCACTGTCTGTGGATGTGGAGCTGACAGCCTATGTGCTCCTGGCCCTGCTCTCCAAGCCAAATGTCACAAGGGCTGATCTCACCACAGCCTCTGGCATTGTGGCCTGGCTTACCAGGCAGCAGAATGCCTATGGAGGATTTGCCTCAACCCAGGATACAGTGGTTGCCCTGCAGGCCTTGGCTAAGTATGCAGCACTGACCTACAGCACAAAGGGGGTTGCAGAAGTGAGGGTGAGGTCCCAGAAAGGCTTTGGGAGGAAGTTCCAAGTCTCCTACCAGAACCGACTTTTGGTGCAGGAGGTGGCACTGACAGAAATCCCAGGGAAGTTCTCAGTGCAGGCCCAGGGCAGCTGCTGTGTCTTTACCCGGACAGTGCTGAGATACAACATTCCCTTCCCTCAGGTTTCCAAGTCCTTTGCCTTACAAGTGAAAACCAAGCCAGACAATTGCACTGAGGACGATGCATACTCTGTTACTCTTTATGTCAATGTCAGGTACATTGGGAAGAGAGCCATTTCCAGCATGGTGATTGTGGAGGTGTCCCTACTGTCTGGATTTGTCCTTGCTCCAGGATCTGGGATGTCTCCACATCATTGGTATCCTGTGAAAAGAACTGAAAAAACCCAAGCAGGTGTTGCCATCTATTTGGACAAGCTGAGCCATAAGTCTGAAACATATGTCCTGCACCTGGAGCGGGAGATTGGGGTGACCAACCTGAAGCCAGGCCATGTCAGGGTCTATGACTACTACCATCCAGAGGAGCAGGCCCTTGCTGATTATAATGTTTCCTGCATCTGA'
b='ATGTGCACTAAGTTCTGGGTTGCACCTCCAGCTGATGGCACAGAGGAGATTGCCACTGTCAGACTGATTATTACAGGTCAAGGGGTCAATATTGAGGAGAAGAAAAATGTCCTGATCCACAAGGCAAACAGTGGCACCTTCATTCAAATGGACAAGCCCATCTATAAACCAGGGCAAACAGTGAAATTTCGTATTGTGACTCTGGATGAGGACTTCATTGCATTTAATGATTCGATTTCCGTGTTTCTCCAGGACCCCAAGAACAACCGGATAGAGCAGTGGCTGAATGTGGTGCCCCAAGAAGGCATTGCAGATCTGTCTTTCCAGCTAAGTGATGAGCCTCTGCTGGGGACATATGTCATCAATGTAACCAACAGGAAAATATATGACAGCTTCACCGTTGAGGAGTATGTGCTGCCAAAATTTGAAGTGATCTTTGAGGCACCAGTGAAGATTTATGCACTAGATAAAACTTTTCCACTTCGGGTATGTGGCAGATACACCTATGGGAAAGCTGTCCAGGGGATGGTTTATGTGAGTCTTTGTCAGAAGATATCTCAGTTCTTGCCCAGTGCTTCGAAACCTGATCTCTGTCAGGAATTCTACAACCAGACAGACAATATGGGTTGCTTCTTCACAAATGTGACACTATCCTTCAGCCAAGACTTGAGGTACTATCGGGACAGCATAGTTGCAGAGGCCTCACTGTTGGAGGATGGCACAGAGATACAGGTCAATGCTTCCCATAAATTACTCATCTCCAAGATTGGCGGAATGGCCTTGTTTGATGATGTGAATTCTTACTATCACGCTGGAGAGATGTACAGAGGGAAGATCAAAGTCATTGACTACAAAGGCAAGATGCTGAAGTACAAAAAAGTCCTCCTTGTAGTAAGTTTTGGTGAGCAGCAGTTTCAGCAAAAGTACCTCACTGGGGACACTGGAACAGCTTCGTTTAGCCTAAACACAACTGCTTGGAACAGCACCTCAGTCTCCCTGGAGGCAAGTGTCCTGCATCAAGATATGGATAGAGAGCCAGGGACAGTTGATTTGAATTACATGAGAGCCTCTCATTTCATACGTCCATTCTACAGCACCAGCAGGAGTTTTCTCAGTATTGTCCATGTGCCAGAAATGATGCCCTGTGGTAAAAAGCAGGCTATCCAGGTGGACTTCAGAATTTACCAGGAAGACCTGGAACATGGGCCCAAGCGTGTAATTTTCTCCTACCTTGTCACAGGGAAAAGTGGAATAGTCCATGCAGGTCAGAAAACTGTTTGGGTTGGGCTGCCAAGAATGCTGAAAGGCTTCTTCTCCATCCCTGTTACCTTCAGCTCAGTCTATGCTCCAACTTCAACACTTATTGTTTATGTTATCTTCCCTAATGGGAAAACCATCGCAGATTCTGCTGTCTTCAGTGTCTCTATGTGTTTCAGAAATAAGGCAGAGCTGAGCTTCTCAGTGCCCAAGATTCTTCCTGGTTCAGAGGTTAATCTCCACCTGCAGGCAGCACCTGGGTCTACATGTGCTGTCTGGGCTGTGGATCAGACTGTCTTTTTGCTGAAGCCAGAAAAAGAGCTCAGCCACTCTATGATCTATGGGCTCTTTCCATCTATTCCATCTACATACTCCGGGTATCCTCATCAAGTGTCTGAAGATGACAATTCATGCGGGTTCCAAAATTCTGATCAGCCTGATGTGTTTACAGCATTCAGGGAAATGGGATTGAAAATTATGTCCAACACCAATATCAGGAAACCAAGACTGTGTCTAACTACTCAGTCAACAACCATGATGCAGGAAAGAGGGATGTTCACTTCCAGGCCTATGTTGATGTTTGCTCAGCCCCATAAGGAATCTAACACAGGACATCTGATGACATCTACCTATCAGCCCACTATGTTTTCACCTGTTTCTTCACCTGAGGAGAAAGTGCACAAGTATTTCACAAAAACCTGGCTATGGGATTTGTATTCTGTCGGTCCCAGTGGAAAACAGACTGTCACTGTCACTGTACCTAACACCATCACAGGATGGAAAGCTGGGATGTTCTGCACAGGACATAATGGCTTCGGACTTGCTCCAACCTCCAGTCTGCTTGTTTTCAAGCCCTTTTCTGTGGAGCTCACACTTCCGTCTTCTGTGATCCAGGGTGAGACCTTCATCTTGAAGGCCACAGTCCTCAGCTACCTGCAACAATGTATGAAGATCCAAGTGACTATGGAGGAGTTCCCACAGTTCCAGCTGAAGTCATGTGAGGGTTGTGTCTACAGCAGCTGCTTATGTGCTGGAGAAGTAAAGACATTTCTGTGGAGTGTCACAGCTGAGCGACTAGGGTTCACGAACATCACTCTCAGCACAGAGGCCATTGCCACAAAGAGCTCTGTGGCAAAGAGATACCATTTGTCCCAAACCAAGGACAGAAAGATACAATCACCAAACTCCTTTTATTTGGTGCAGAGTAATTCTAGGACTTGTCCCTTGTTATTCAAGGAGAATCTCTGGCTTGGACCAAAATTTTGTCTGTATCTATTTGTAATCCACTTTTTCTCTCCTATGTGCTCATTACTGCTACTATTGAATGCTCAACAGCCAGAGGGAGTGCTAATAGAAAAGGCTCACAGTTCCATCCTGTGTCCCAAGAAAGGGAGTCCAGCAGAGGAGTCTGTGTCCTTAACGTTGCCTCCAAATACGGTTGAAGGTTCAGTGAGAGCTACTGTCTCAGTCACTGGTGACCTCATGGGGACAGCACTGCAAAACTTGGACCACCTGGTGCAGATGCCCCATGGCTGTGGGGAGCAGAACATGGTACTGTTTGCCCCCATTGTCTATATGCTGCAGTACCTGGAGAAGACAAGGCAGCTGACTCCTGAGATTAAGGAGAGGGCAACAGGATTCTTGCGCAATGGGTATCAGATACAGCTGCAGTATCAACATCCTGATGGTTCTTTCAGTGAATTTGGTACCAAGGATGAGTACGGTAATACTTGGCTGACTGCATTTGTGGTCAAATGCTTTGCCCAAGCCAAGCCATACATTTTCCTGGACGACAGGAGCATTCAAGCTGCTTTCAATTGGCTGGAGTTCCACCAGCTTCCGAATGGCTGCTTCAGGGATGTGGGCCAACTTTTCCACACAGCCATGAAAGGAGGTATGGATGGGGAAGTTCTCTTGGCTGCCTACATCACTGCTGCATACATGGAGAGAGGAGATACACCAGAGAGTACAGTGGTGCGCAAGGCTCTGGGGTGTATCATTCCTTCCCTTCCCAAAGCTACCAGCACTTACACACAGGCCCTGCTGGCCTACACCTTTGCCCTGGCTAAGGATCCTCAGCGCACACAAGAGCTTCTTGACATACTTGATGAAAAGGCAATCAGAGCAGGTGGGCAGATCCATTGGAGTCAGACCCCATCCAAGGCACACAGCACTAGCCTTTGGTCACAGCCACTGTCTGTGGATGTGGAGTTAACAGCTTATGTCCTCCTGGCCCTGCTCTCCAAGCCAAATGTCACAGAGGCTGACTTCACCATAGCCTCTGGCATTGTGGCGTGGCTCACCAGACAGCAAAATGCCTATGGAGGATTTGCCTCAACCCAGGATACGGTAGTTGCCCTGCAGGCCTTGGCTAAGTATGCAGCGCTGACACACAACACAAAAGGGGTTGCAGAAGTGAGAGTGAGGTCCCAGAGAGGCTCTGGGAGGAAGTTCCAAGTTTCCTACCACAATCGGCTTTTGGTGCAGGAGATGGCACTGAGAGAAATCCCAGGAAAGTTCTCAGTGCAGGCCCATGGCAGCTGTTGTGTCTTTACCCGGACAGTGCTGAGATACAACATTCCCTTCCCTCAGGTTTCCAAGTCCTTTGCCTTACAAGTGAAAACCAAGCCAGACAATTGCACTGAGGACGATGCATACTCTGTTACTCTTTATGTCAATGTCAGGTACACTGGGAAGAGAGCCATTTCCAACATGGTGATTGTGGAAGTGTCCCTACTGTCTGGATTTGTCCTGGCTGCAAGATCTGGGATGTCTCCACATCATTGGTATCCTGTGAGAAGAACAGAGAAAACCCAAGCAGGTGTTGCCATCTACTTGGACAAGCTGAGCCATGTGTCTGAGACATATGTCCTGCATCTAGAAAGGGAAATTGAAGTGACCAACCTGAAGCCAGGACAAGTCAGAGTCTATGACTACTACCATCCAGAGGAGCAGGCCCTTGCTGATTATAATGTTTCCTGCATCTGA'
dnds(a,b)