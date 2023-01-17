import json
import streamlit as st

file_qna = "output.json"

if "index" not in st.session_state:
    st.session_state['index'] = 0
    
if "data" not in st.session_state:   
    with open(file_qna, "r") as file:
        st.session_state["data"] = json.load(file)
    


def main():
    # Read JSON file
    print("Index:", st.session_state['index'])

    question = st.session_state["data"][st.session_state['index']]["instruction"]
    answer = st.session_state["data"][st.session_state['index']]["response"]
    
    # Display question and answer
    st.write("Instruction:", question)
    st.write("Response:", answer)
    
    # Ask for explanation
    updated_response = st.text_input("Updated response:") or answer
    next = st.button("Next")
    
    # Append explanation to file
    if next:
        st.session_state['data'][st.session_state['index']]["response"] = updated_response
        output_json = json.dumps(st.session_state["data"], indent=4)

        with open("output.json", "w") as f:
            f.write(output_json)
            
        st.success("Explanation saved!")
        st.session_state['index'] += 1


if __name__== "__main__":
    main()
