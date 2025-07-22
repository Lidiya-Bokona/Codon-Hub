Codon Hub



Your Offline Genetics Helper: Learn DNA, Codons, & Proteins, Visually




About

Codon Hub is a simple, console-based Python program designed to make learning Grade 11-12 genetics easier. Tired of confusing textbooks and abstract ideas? Codon Hub offers interactive tools, instant answers, and visual aids to help you understand DNA, proteins, and more, all offline.


Features

Strand Predictor (Option A): Input DNA bases line-by-line to get the complementary strand.

Amino Acid Visualizer (Option B):Enter an mRNA codon (e.g., CAA), and it shows the amino acid name and its structure photo (image pops up in a separate window!).

Genetics Q\&A (Option C): An AI assistant for genetics concepts. Ask exact questions for explanations, then get options for video links or explanatory photos.
    Specific Questions Recognized:
          what is dna?
          what is protein?
          what is aminoacid?
          what is transcription?
          what is translation?
          what is bioinformatics?
          what is chromosome?
          what is mutation?
          
   visual Learning Aids: Get YouTube video links (displayed in console) or explanatory photos (pop up in separate windows) for concepts.


Get Started

Requirements
  * Python 3.6+
  * `pip` (comes with Python)

Setup

1.  Clone the Repository:
    ```bash
    git clone https://github.com/Lidiya-Bokona/Codon-Hub.git
    cd Codon-Hub
    ```

2.  Install Dependencies:
    You'll need nltk for the AI and opencv-python for image display.
    ```bash
    pip install nltk opencv-python
    ```

3.  Download NLTK Data (one-time):
    The Natural Language Toolkit (NLTK) needs specific data for its functions. You'll run this command once after installation:
    ```bash
    python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet'); nltk.download('omw-1.4')"
    ```

Run

Once dependencies and NLTK data are installed, you can run the application offline:
```bash
python main.py
```


Usage

When you run python main.py, you'll see the main menu in your console:

```
Hello there!!!!
>I will be your genetic assitant!
>Enter A for identifying complimentary strand
>Enter B for mRNA codon to protien translator
>Enter C for an AI genetic assistant demo!
```
Choose A (Identifying Complimentary Strand):

     Enter nitrogen bases one by one (e.g., A, T, G).
     Press 0 then Enter when you are done to see the complementary strand.

Choose B (mRNA Codon to Protein Translator):

       Enter the codon you are looking for (e.g., CAA) in capital letters with no spaces.
       Press Enter to see the amino acid name and its structure in a photo that pops up in a separate window.

Choose C (AI Genetic Assistant Demo):

       Enter one of the exact specific questions listed in the Features section (e.g., what is dna?).
       After the explanation, it will ask: Should I provide furthur video or photo explanation for the question stated?(vedio/photo)
           Reply photo to see an explanatory image for the topic (image pops up in a separate window).
           Reply vedio to get a YouTube video link that explains the concept (displayed in the console).


Contributing

Got ideas or found a bug? Contributions are welcome!
Fork the repo, make your changes, and open a Pull Request.


Contact

Questions? Reach out via my GitHub profile: https://github.com/Lidiya-Bokona

