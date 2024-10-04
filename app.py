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
        
        # Calculate the total amount for the specified debtor
        total_amount = 0
        for match_name, amount in matches:
            if match_name.strip().lower() == debtor_name.strip().lower():
                total_amount += int(amount.strip().replace(',', ''))
        
        # Display the result
        if total_amount > 0:
            st.success(f'Total amount debited to {debtor_name}: ₹{total_amount}')
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
