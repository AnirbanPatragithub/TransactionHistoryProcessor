import re
import streamlit as st
from pdfminer.high_level import extract_text

def main():
    st.title("Transaction History Analyzer")
    
    # File uploader for the PDF
    uploaded_file = st.file_uploader("Upload your transaction history PDF", type=["pdf"])
    
    # Input for the debtor's name
    debtor_name = st.text_input("Enter the name of the debtor:")
    
    if uploaded_file and debtor_name:
        # Extract text from the uploaded PDF
        text = extract_text(uploaded_file)
        
        # Regex pattern to match names and amounts in debit transactions
        pattern = r'Paid to (.+?)\s+DEBIT\s+₹([\d,]+)'
        
        # Find all matches
        matches = re.findall(pattern, text)
        
        # Calculate the total amount for the specified debtor and gather all matching records
        total_amount = 0
        low_amount = 0
        matching_records = []
        
        for match_name, amount in matches:
            if match_name.strip().lower() == debtor_name.strip().lower():
                transaction_amount = int(amount.strip().replace(',', ''))
                total_amount += transaction_amount
                matching_records.append((match_name, transaction_amount))
                if transaction_amount < 1200:
                    low_amount += 1
        
        # Display matching transactions
        if matching_records:
            st.write("### Matching Transactions:")
            for record in matching_records:
                st.write(f"Name: {record[0]}, Amount Debited: ₹{record[1]}")
                
            # Display the total amount
            st.success(f'Total amount debited to {debtor_name}: ₹{total_amount}')
            st.success(f'Amount after deducting courier charge for {debtor_name}: ₹{total_amount - low_amount*50}')
        else:
            st.warning(f'No transactions found for {debtor_name}.')
    elif uploaded_file:
        st.info("Please enter the name of the debtor to calculate the total amount.")
    elif debtor_name:
        st.info("Please upload a transaction history PDF.")
    
    # LinkedIn profile section
    st.markdown("""
    ### Connect with Me
    [LinkedIn Profile](https://www.linkedin.com/in/ani8159)  
    Feel free to connect with me on LinkedIn for networking and collaboration!
    """)

if __name__ == "__main__":
    main()
