import os
import sys
import cv2
import webbrowser
import time
import cv2
import nltk
from nltk.chat.util import Chat,reflections

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

selector=input('''
>Hello there!!!!
>I will be your genetic assitant!
>Enter A for identifying complimentary strand
>Enter B for mRNA codon to protien translator
>Enter C for an AI genetic assistant demo!
     ''')


if selector == 'A' or selector == 'a':
        #The following program accepts a set of neuclotide strand and gives the coresponding strand which joins with it.
        store=[]
        f=1
        while f==1:
            x=input("Enter base of the neuclotide(A,T,G,C)")
            store.append(x)
            print ("to quit enter 0")
            if x=="0":
                f=f+1
        print("The given dna strand sequence",store)
        finalstore=[]
        while len(store)>0:
            
                length=len(store)
                if store[(length-1)]=="A":
                    finalstore.append("T")
                elif store[(length-1)]=="T" or store[(length-1)]=="U":
                    finalstore.append("A")
                elif store[(length-1)]=="G":
                    finalstore.append("C")
                elif store[(length-1)]=="C":
                    finalstore.append("G")
                store.pop(length-1)
                length=length-1

            

        finalstore.reverse()
        print ("Adjoint dna strand",finalstore)

elif selector == 'B' or selector == 'b':
    z=1
    while z==1: 
            codon=input("Please enter a 3 base mRNA codon:")
            if len(list(codon))==3:
                print("searching for a match.......")
                z=z+1
            else:
                 print("Please enter a 3 base codon")
    Amino_Acid_list= {"GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
        "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGA": "Arginine", "AGG": "Arginine",
        "AAU": "Asparagine", "AAC": "Asparagine",
        "GAU": "Aspartic Acid", "GAC": "Aspartic Acid",
        "UGU": "Cysteine", "UGC": "Cysteine",
        "CAA": "Glutamine", "CAG": "Glutamine",
        "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",
        "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine",
        "CAU": "Histidine", "CAC": "Histidine",
        "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",
        "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
        "AAA": "Lysine", "AAG": "Lysine",
        "AUG": "Methionine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "AGU": "Serine", "AGC": "Serine",
        "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
        "UGG": "Tryptophan",
        "UAU": "Tyrosine", "UAC": "Tyrosine",
        "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine" , "UAA":"STOP CODON", "UAG":"STOP CODON", 
        "UGA":"STOP CODON", "TAA":"STOP CODON", "TAG":"STOP CODON", 
        "TGA":"STOP CODON"
     }
     
    Amino_Acid=Amino_Acid_list.get(codon,"NO AMINO ACID FOUND!") 
    print(Amino_Acid)
    images=os.listdir()
    if Amino_Acid+".jpg" in images:
         img = cv2.imread(Amino_Acid+".jpg", cv2.IMREAD_ANYCOLOR)

         while True:
                cv2.imshow(Amino_Acid,img)
                cv2.waitKey(0)
                sys.exit() # to exit from all the processes
    
         cv2.destroyAllWindows() # destroy all windows
         
    #pp=input("press enter to close the program:")

    else:
       print ("Please try again")
       pp=input("press enter to close the program:")
elif selector=="C" or selector=="c":
        
        def showimage(imagedir):
             img = cv2.imread(imagedir, cv2.IMREAD_ANYCOLOR)
             print("Thank you for using my service have a nice time!")
             while True:
                      cv2.imshow("DNA>><<",img)
                      cv2.waitKey(0)
                      sys.exit()
                      
                    
                      
             cv2.destroyAllWindows()
             
pairs = [
            (
                r'what is DNA\?',
                [ '''DNA (deoxyribonucleic acid) is the hereditary material in humans and other organisms.It exists in a double helix formed by base pairs attached to a sugar-phosphate backbone.'
'RNA (ribonucleic acid) serves as the genetic codes in some viruses. It is involved in protein synthesis in cells.
The structure of DNA is a ladder-like double helix twisted into a spiral shape, in which the sugar and phosphate groups form the two vertical ladder and the nitrogenous bases form the ladder’s rungs.' 
'It consists of two long chains of chemicals called polynucleotide that twist around each other to form a double helix. Nucleotides are the basic building blocks of a DNA molecule.  
Each nucleotide is composed of a sugar, phosphate group and a nitrogenous base.'
'There are four types of nitrogenous bases. These are: Adenine (A), Thymine (T), Guanine (G) and Cytosine (C).
 A pairs with T and C pairs with G to form units called base pairs.'
 'Each base is also attached to a sugar molecule and a phosphate molecule to form a nucleotide, the building blocks of the DNA called nucleotide.  
The function of DNA is to store all of the genetic information that an organism needs to grow, develop, reproduce, control the cell and survive.'
'While DNA determines the characteristics of an organism, it is also responsible for carrying and transmitting the hereditary materials or the genetic instructions from parents to the offspring.'
'The transmission of this information from the mother to daughter cells occurs through the process of DNA replication during cell division.'
'DNA replication is the process by which DNA makes a copy of itself during cell division. DNA has a unique property of replication or production of carbon copies.'
'This is essential for transfer of genetic information from one cell to its daughters and from one generation to the next.'
' DNA gives rise to RNAs through the process of transcription.'  
'DNA replication is a semiconservative, which means that each strand in the DNA double helix acts as a template for the synthesis of a new, complementary strand.' 
'In other words, the two original DNA strands separate during replication; each strand then serves as a template for a new DNA strand.'
'Each newly synthesized double helix is a combination of one old and one new DNA strand. DNA replication involves the following enzymes. DNA Helicases,DNA Polymerase, RNA Polymerase, DNA Ligase, Topoisomerase'
'RNA has single strand structure.  RNA contains the sugar ribose, phosphates, and the nitrogenous bases adenine (A), guanine (G), cytosine (C) and uracil (U) which replaces thymine in DNA.'
'There are three most well-known types of RNA in all organisms. These are messenger RNA (mRNA), transfer RNA (tRNA) and ribosomal RNA (rRNA).
 All types of RNAs are formed on DNA strands by transcription process.'
'RNA is the most important molecule in all lives. RNA is involved in a variety of functions within the cell and is found in all living organisms. RNA functions in protein synthesis and used as a storage of genetic information in some viruses.'
'RNA facilitates the translation of the DNA into different proteins required by organisms.  For example, it serves as a messenger in conveying instructions between the DNA and the ribosome during proteins synthesis.'
'''],),
             
            (  
                r'what is protein\?',
                ['''Proteins are large, complex molecules that play crucial roles in the body. They are made up of long chains of amino acids, which are linked together by peptide bonds.'
'Proteins are organic compound made of amino acids joined together by peptide bonds. There are essential for the maintenance of structural attributes and the functioning of all living cells and viruses.'
'There are 20 different naturally occurring amino acids but each protein is different in structure and function due to the sequence in which these amino acids are arranged.'
'Protein synthesis is the stepwise process of the production of different types of proteins from amino acids. It involves DNA, RNA (mRNA, tRNA and rRNA), amino acids, various enzymes and ribosome.'
'Messenger RNA (mRNA) transcribes genetic information from DNA in the nucleus with the help of enzyme RNA polymerase.'  
'Transfer RNA (tRNA) brings amino acids from the cytoplasm to the ribosome and it translates the message within the nucleotide sequence of mRNA to a specific amino acid sequence.'
'Ribosomal RNA (rRNA) is a molecule in cells that forms part of the ribosome that help translate the information in messenger RNA (mRNA) into protein'  
'Proteins are essential for various biological functions, including:'

        '1. Enzymes: Proteins act as catalysts in biochemical reactions, speeding up the rate of reactions in the body.'
        '2. Structural Components: Proteins provide structural support to cells, tissues, and organs.'
        '3. Hormones: Certain proteins act as hormones that regulate various physiological processes.'
        '4. Transport Proteins: Proteins help transport molecules such as oxygen and nutrients throughout the body.'
        '5. Immune System Function: Antibodies are proteins that play a key role in the immune response.'

        '''
        ],
            ),
            (
                r'what are aminoacid \?',
                ['''Amino acids are organic compounds that serve as the building blocks of proteins.'
                 'Proteins are essential macromolecules that play a wide variety of roles in the body, including serving as enzymes, structural components, hormones, and more.'
                 'There are 20 different amino acids that are commonly found in proteins, each with its own unique side chain that gives it specific properties.'
                 'Amino acids consist of an amino group (NH2), a carboxyl group (COOH), and a side chain (R group) attached to a central carbon atom. The sequence of amino acids in a protein determines its structure and function. Proteins are made up of long chains of amino acids that are linked together by peptide bonds.'
        '''],
            ),
             
            (
                r'what is transcription\?',
                ['''Transcription is the synthesis of mRNA molecules within the cell nucleus with the code for a protein copied from the genetic information contained in the DNA.'
'In other words, transcription produces an exact copy of a section of DNA known as messenger RNA (mRNA).' 
'It carries complementary genetic code copied from DNA during transcription, in the form of triplets of nucleotides called codons.' 
'A codon is a sequence of three nucleotides and four nitrogenous bases on an mRNA strand derived from the  DNA that encodes a specific amino acid.'
'Each codon specifies a particular amino acid.' 
'For example, amino acid tryptophan is coded by a codon TAG, alanine by GCA, GCC, glycine by GGA, AGG, etc for each 20 amino acids.'
'There are only 20 naturally existing amino acids but the number of possible amino acids combination is 43 = 64 triplets.'  
'Out of the 64 codons, three are stop codons, which stop the process of protein synthesis (UAG, UAA, and UGA) and one of the codons is an initiator codon or start codons that initiates protein synthesis (AUG).'
'During Transcription:'
'Inside the nucleus a small portion of the DNA separates'
'Free RNA nucleotides attach to appropriate base pairs on the DNA template and mRNA is formed with code (triplets of nucleotides called codons) for protein synthesis. Similarly, tRNA and rRNA also transcribed from DNA. 
mRNA detaches from the DNA' 
'mRNA leaves the nucleus to go out into the cytoplasm and binds to ribosomes Translation'
'''],
            ),
             (
                r'what is translation\?',
                ['''Translation is the synthesis of protein from the building blocks of protein /amino acids/ based on the genetic information instructed on mRNA with the help of rRNA, tRNA and enzymes.'
'Transfer RNA (tRNA) carries a specific amino acid from cytoplasm. This  tRNA contains an anticodon  which is three nucleotides long that is complementary to the three nucleotides long genetic codon on the mRNA.'
'The anticodon on tRNA enables to recognize the codon of mRNA through complementary base pairing. For example, the genetic codon GUG (guanine-uracine- guanine) specifies particular amino acid valine.'  
'By binding its anticodon (CAC) that is complementary with mRNA codon /GUG/, the tRNA acts as an adapter, bringing the specific amino acid based on base complementarily.'
'The complementary bases on the codon and anticodon held together by hydrogen bonds to from peptides bond in growing protein chain.'
' The ribosome guides the tRNA to bind to the mRNA if it is carrying an amino acid.'  
'During Translation:'
'1. mRNA carries the information from DNA align on the  ribosome in the cytoplasm '
'2. The ribosomes attach on to mRNA and let the tRNA loaded with specific amino acid to enter  '
'3. tRNA with anti-codon brings amino acids from the cytoplasm to the ribosomes '
'4. The anti-codon of tRNA pairs with the codon of mRNA on the ribosome '
'5. the information in messenger RNA (mRNA) translated into protein with the help of rRNA  '
'6. A polypeptide chain of amino acids will then form a protein'
'''],
            ),
             (
                r'what is bioinformatics\?',
                ['''Bioinformatics is a modern, growing hybrid field that links biology, computer science, and information technology'
'to support the storage, organization, and retrieval of biological data.'
'It is the design, constructions and use of software tools to generate, store, Inquiry, interpret and analyze data and information related to biology.'
'Bioinformatics provides tools to comprehensively analyze and save large amounts of biological data that would be impossible to investigate without informaticsbased approaches. '
'Bioinformatics has also become useful to improve the diagnosis and detection of diseases, to promote vaccine development by screening databases for pathogen genomes, and to increase our understanding of evolutionary processes'
'through the analysis of nucleotide/protein sequence mutations.'  
'The field of bioinformatics incorporates three main areas:'
'1) genomics'
'2) proteomics'
'3) systems biology.' 
'Genomics includes DNA sequence data, whereas proteomics deals with the function, shapes, interactions, and abundance of proteins.'
'Systems biology that examines the extensive role of protein and DNA interactions on the function of cells, tissues, and organs,'
'as a whole is the most recent and complex branch in the field of bioinformatics.'
 'Systems biology can describe the pathway of enzymes and their various metabolites by using computer data models.'
 'It can illustrate brain function by using computer images. '
 '''],
            ),
            (
   r'what is chromosome\?',    
        [''' Sections of the DNA structure that contain the set of instructions that determine the characteristics of an organism are called genes.'
'Genes are the basic structural and functional units of inheritance in nature.'
' Genes pass from parents to offspring during both sexual and asexual reproduction through cell division.' 
'Genes are located on chromosomes. Chromosomes are threadlike structures made of a protein called histone and DNA molecule. 
Each chromosome may contain hundreds to thousands of genes that are arranged linearly along the length of each chromosome (like beads on a string),'
'with each gene having its own unique position on to chromosomes called locus / loci (plural).' 
'For example a human cell contains 46 chromosomes which exist in 23 pairs of chromosomes'
'''],
            ),
            (
        r'what is mutation\?', 
            ['''Mutation is a random chance in genetic information.'
'Mutation can be caused by several factors but is devided into two parts.' 
'If the agent that caused the mutation cannot be identifid then it is called spontaneous mutation.' 
'if the mutation can be identified then it is called an induced mutation.'
' substances that cause mutation are radiation, x-ray, uv radiation, nuclear radiation and certain chemical substances.' 
'these agents can also be called mutagenic agents or mutagens.' 
'there can be large structural changes involving the whole chromosomes or parts of chromosome or changes that involve only a single base.'
' the changes involving only a single base are called point mutations. types of point mutation include substitution, addition, deletion. '
'chromosomal mutation is a mutation involving a long segment of DNA. '
'types of chromosomal DNA includes duplication, inversion, deletion, aneuplody, polyploidy'
'''],
       ),      
        ]

def chatbot():
            print("AI: Hello there! I am your Genetic assistant AI. How can I help you today?")
            chat = Chat(pairs, reflections)
            
            while True:
                user_input = input("User: ")
                response = chat.respond(user_input)
                print("AI:",print_s(response))             
                query_understood=input("Should I provide furthur video or photo explanation for the question stated?(vedio/photo) ")
                if query_understood =="vedio" or query_understood =="Vedio":
                       
                        if user_input=="what is dna?" or user_input=="What is DNA?":
                            print_s(" For more in- depth comprehension, consider watching this youtube vedio.https://www.youtube.com/watch?v=GIzNlISbCxI" )
                        if user_input=="what is protien?" or user_input=="What is Protien ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio. https://www.youtube.com/watch?v=DdNv8VtXjRg&pp=ygUPd2hhdCBpcyBwcm90aWVu")
                        if user_input=="what is aminoacid?" or user_input=="what is aminoacid ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio. https://www.youtube.com/watch?v=J6R8zDAl_vw&pp=ygUUd2hhdCBhcmUgYW1pbm8gYWNpZHM%3D")
                        if user_input=="what is transcription?" or user_input=="what is transcription ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio.https://www.youtube.com/watch?v=itsb2SqR-R0  ")
                        if user_input=="what is translation?" or user_input=="what is translation ?":
                            print_s(" For more in- depth comprehension, consider watching this youtube vedio. https://www.youtube.com/watch?v=3z5n9OYc3Gw ")   
                        if user_input=="what is bioinformatics?" or user_input=="what is bioinformatics ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio.https://www.youtube.com/watch?v=7p8ZuJlF4CQ  ")
                        if user_input=="what is chromosome?" or user_input=="what is chromosome ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio.https://www.youtube.com/watch?v=1gNQpD0hSx0  ")
                        if user_input=="what is mutation?" or user_input=="what is mutation ?":
                            print_s("For more in- depth comprehension, consider watching this youtube vedio.https://www.youtube.com/watch?v=ZLJLbK9WnQY  ")
                            
                elif query_understood =="photo" or query_understood =="Photo":
                        if user_input=="what is dna?" or user_input=="what is DNA?":
                            showimage("DNA.jpg")
                        if user_input=="what is protein?" or user_input=="what is protien ?":
                            showimage("protein.jpg")
                        if user_input=="what is aminoacid?" or user_input=="what is aminoacid ?":
                            showimage("aminoacid.jpg")
                        if user_input=="what is transcription?" or user_input=="what is transcription ?":
                            showimage("transcription.jpg")
                        if user_input=="what is translation?" or user_input=="what is translation?":
                            showimage("translation.jpg")   
                        if user_input=="what is bioinformatics?" or user_input=="what is bioinformatics?":
                            showimage("bioinformatics.jpg")
                        if user_input=="what is chromosome?" or user_input=="what is chromosome?":
                            showimage("chromosome.jpg")
                        if user_input=="what is mutation?" or user_input=="what is mutation ?":
                            showimage("mutation.jpg")  

                

                

                else:

                    print_s(" I trust that i have addressed your question effectively. Have a wonderful day! ")
                        
            
if __name__ == "__main__":
  chatbot()
         

   
                


                 
