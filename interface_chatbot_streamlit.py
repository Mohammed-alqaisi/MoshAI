import streamlit as st
import requests

# Define the Flask API endpoint
API_URL = "http://127.0.0.1:5000/query"

# Set up Streamlit UI
st.set_page_config(page_title="Business Query Assistant", layout="wide")

st.title("Business Query Assistant")
st.subheader("Ask your business questions and get meaningful answers.")

# Maintain conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Input section
user_input = st.text_input("Enter your query here:", key="user_input")

# Function to extract business answer from query results
def extract_business_answer(result):
    if isinstance(result, list) and len(result) > 0:
        # Dynamically extract column names from the first row
        columns = result[0].keys()
        
        # Format results dynamically based on columns
        formatted_results = []
        for row in result:
            formatted_row = ", ".join([f"{col}: {row[col]}" for col in columns])
            formatted_results.append(formatted_row)
        
        # Join all rows with newlines for display
        return "\n".join(formatted_results)
    return "No data available."

# Handle form submission
if st.button("Submit"):
    if user_input.strip():
        try:
            # Send request to Flask API
            response = requests.post(API_URL, json={"user_input": user_input})
            response_data = response.json()
            
            if response.status_code == 200:
                sql_query = response_data.get("sql_query", "")
                result = response_data.get("result", [])

                if result:
                    # Check if result is tabular (list of dicts)
                    if isinstance(result, list) and isinstance(result[0], dict):
                        st.markdown("### Query Results:")
                        st.table(result)  # Display as a table
                    else:
                        # Fallback: Use the generic business answer extractor
                        business_answer = extract_business_answer(result)
                        st.markdown("### Answer:")
                        st.text(business_answer)
                else:
                    st.warning("No data found in the database.")

            else:
                error_message = response_data.get("error", "An error occurred.")
                st.error(f"Error: {error_message}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a query.")

# Display chat history
# st.markdown("## Conversation History")
# for msg in st.session_state.history:
#     if msg["role"] == "user":
#         st.markdown(f"**You:** {msg['content']}")
#     elif msg["role"] == "system":
#         st.markdown(f"**System:** {msg['content']}")

# Footer
st.markdown("---")
st.text("Powered by Streamlit and Flask")
