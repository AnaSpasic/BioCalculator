import customtkinter
import os
from Bio import SeqIO
from DNASequence import DNASequence
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="BioCalculator", font=('',20))
label.pack(pady=12, padx=10)

# Choose dataset from falling menu
datasets_dir = os.getcwd() + '/Datasets'
files = os.listdir(datasets_dir)
datasets = [file for file in files if file.endswith(".txt")]

dataset_var = customtkinter.StringVar(value="Choose dataset")
def dateset_callback(choice):
    print("Chosen dataset:", choice)
    file_path = datasets_dir + '/' + dataset_choice.get()
    sequences = read_fasta(file_path)
    sequence_choice.configure(values=sequences.values()) # after we choose dataset, we configure the sequence_choice box
    # with sequences from the dataset

dataset_choice = customtkinter.CTkComboBox(master=frame,
                                     values=datasets,
                                     command=dateset_callback,
                                     variable=dataset_var)
dataset_choice.pack(padx=20, pady=10)

# Choose sequence from falling menu after you chose dataset
def read_fasta(file_path):
    sequences = {}

    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences[record.id] = str(record.seq)

    return sequences

sequences_var = customtkinter.StringVar(value="Choose sequence")
def sequence_callback(choice):
    print("Chosen sequence:", choice)
    global dna_seq
    dna_seq = DNASequence(choice, 'id')
    action_choice.configure(values=["Sequence info", "Transcribe to RNA"])  # after we choose dataset, we configure the sequence_choice box

sequence_choice = customtkinter.CTkComboBox(master=frame,
                                     values=[], # it's empty before we choose dataset
                                     command=sequence_callback,
                                     variable=sequences_var)
sequence_choice.pack(padx=20, pady=10)

# Choose action
action_var = customtkinter.StringVar(value="Choose action")
def action_callback(choice):
    print("Chosen action:", choice)
    textbox.delete("0.0", "end")
    if choice == 'Sequence info':
        textbox.insert("0.0", "DNA sequence info:\n" +
                       f"GC content: {dna_seq.GC_content()}\n" +
                       f"Nucleotide frequency: {dna_seq.count_nucleotides()}"
                       )
    elif choice == 'Transcribe to RNA':
        try:
            textbox.insert("0.0", f"Transcribed RNA: {dna_seq.transcribe_to_rna()}")
        except:
            print("Function not defined")

action_choice = customtkinter.CTkComboBox(master=frame,
                                     values=[], # it's empty before we choose sequence
                                     command=action_callback,
                                     variable=action_var)
action_choice.pack(padx=20, pady=10)

textbox = customtkinter.CTkTextbox(frame, height=100, width=350)
textbox.pack(padx=10, pady=10)

root.mainloop()
