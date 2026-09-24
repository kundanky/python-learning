# --- LEGAL AI TASK: COMPLETED RED-FLAG EXTRACTOR ---

def extract_red_flags(contract_text, risk_keywords):
    print("--- STARTING SCANNING PROCESS ---")
    
    # Split the text block into a list of individual sentences
    sentences = contract_text.split(". ")
    
    # Point-to-point nested iteration logic
    for sentence in sentences:
        for keyword in risk_keywords:
            # Logic check: Case-insensitive searching
            if keyword.lower() in sentence.lower():
                print(f"⚠️ CRITICAL RISK: Found '{keyword}' in sentence: \"{sentence.strip()}\"")

# --- TEST EXECUTIONS ---
sample_contract = "The parties agree to execute the project. In case of a breach, the vendor is fully responsible. The total payment is Rs 50,000. The liability of the client is completely capped."
my_risks = ["breach", "liability"]

extract_red_flags(sample_contract, my_risks)
