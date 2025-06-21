import os
import PyPDF2

def brute_force_pdf(pdf_path, dict_path):
    # Read the dictionary file
    try:
        with open(dict_path, 'r') as file:
            wordlist = file.read().splitlines()
    except FileNotFoundError:
        print(f"Dictionary file not found: {dict_path}")
        return

    # Open the PDF file
    try:
        with open(pdf_path, 'rb') as file:
            pdfreader = PyPDF2.PdfFileReader(file)

            if not pdfreader.isEncrypted:
                print("The PDF file is not encrypted.")
                return

            # Try each password from the wordlist
            for word in wordlist:
                result = pdfreader.decrypt(word)
                if result == 1:  # Password found
                    print(f"Password found: {word}")
                    return word
            print("Password not found in the dictionary update the dictionary with new passwords and try.")
    except FileNotFoundError:
        print(f"PDF file not found: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# === Choose PDF and Dictionary File Paths ===
pdf_file_path = input("Enter the path to the PDF file: ").strip()
dictionary_path = input("Enter the path to the dictionary file: ").strip()

brute_force_pdf(pdf_file_path, dictionary_path)
