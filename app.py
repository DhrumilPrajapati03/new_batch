# import streamlit as st

# st.set_page_config(page_title="🐍 Python Data Type Quiz", page_icon="🎓", layout="centered")

# # Custom CSS to perfectly match the requested design aesthetic
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#     }

#     /* Vibrant Dark background */
#     .stApp {
#         background: radial-gradient(circle at top center, #1e1b4b 0%, #0f172a 100%);
#         color: #f8fafc;
#     }
    
#     h1, h2, h3 {
#         color: #f8fafc !important;
#     }

#     /* Container border matching a softer card style */
#     [data-testid="stVerticalBlockBorderWrapper"] {
#         background-color: #1e293b !important;
#         border: 2px solid #334155 !important;
#         border-radius: 12px !important;
#         box-shadow: 0 8px 16px -4px rgba(0, 0, 0, 0.5) !important;
#     }

#     /* Radio Group container layout */
#     div.stRadio > div[role="radiogroup"] {
#         display: flex;
#         flex-direction: column;
#         gap: 14px;
#         margin-top: 15px;
#     }
    
#     /* Option Custom Selector Box */
#     div.stRadio > div[role="radiogroup"] > label {
#         background-color: #334155 !important;
#         padding: 16px 20px;
#         border-radius: 8px;
#         border: 2px solid transparent !important;
#         margin: 0;
#         cursor: pointer;
#         transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
#         width: 100%;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
#     }

#     /* Hover effect */
#     div.stRadio > div[role="radiogroup"] > label:hover {
#         background-color: #2e264f !important;
#         border-color: #a78bfa !important;
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(167, 139, 250, 0.2) !important;
#     }

#     /* Selected state - A cheerful, bright green */
#     div.stRadio > div[role="radiogroup"] > label:has(input:checked) {
#         background-color: #064e3b !important;
#         border: 2px solid #34d399 !important;
#         box-shadow: 0 0 10px rgba(52, 211, 153, 0.4) !important;
#         color: #ffffff;
#     }

#     /* Hide the default circular radio button */
#     div.stRadio > div[role="radiogroup"] > label > div:first-child {
#         display: none !important;
#     }

#     /* Adjust font inside the option wrapper */
#     div.stRadio > div[role="radiogroup"] > label [data-testid="stMarkdownContainer"] p {
#         font-size: 16px !important;
#         font-weight: 600;
#         margin: 0 !important;
#         color: #f1f5f9 !important;
#         letter-spacing: 0.3px;
#     }

#     /* Custom submit button */
#     .stButton>button {
#         background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%) !important;
#         color: white !important;
#         font-size: 16px !important;
#         font-weight: bold !important;
#         border-radius: 10px !important;
#         padding: 12px 24px !important;
#         border: none !important;
#         margin-top: 25px;
#         width: 100%;
#         box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
#         transition: transform 0.2s, box-shadow 0.2s;
#     }
#     .stButton>button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6) !important;
#     }
    
#     hr {
#         margin: 15px 0 !important;
#         border-top: 2px dashed #475569 !important;
#     }
    
#     .question-number {
#         font-size: 14px;
#         font-weight: 800;
#         color: #ffffff;
#         background: linear-gradient(90deg, #3b82f6, #8b5cf6);
#         padding: 6px 14px;
#         border-radius: 20px;
#         display: inline-block;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.3);
#         text-transform: uppercase;
#         letter-spacing: 0.5px;
#     }
    
#     .question-text {
#         margin-bottom: 20px;
#         font-size: 18px;
#         font-weight: 600;
#         color: #f8fafc;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("Python Assessment")
# st.markdown("<p style='color: #64748b; font-size: 15px; font-weight: 500;'>Last Updated : Jan 10, 2025</p>", unsafe_allow_html=True)
# st.write("---")

# prefixes = ["Ⓐ", "Ⓑ", "Ⓒ", "Ⓓ"]

# practical_mcqs = [
#     {"q": "What is the output of `type(5 / 2)`?", "opts": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "Error"], "ans": "<class 'float'>"},
#     {"q": "What happens if you call `List.pop()` on an empty list?", "opts": ["Returns None", "Returns 0", "Raises IndexError", "Raises ValueError"], "ans": "Raises IndexError"},
#     {"q": "What is the output of: `a = [1, 2, 3]; a[1] = 4; print(a)`?", "opts": ["[1, 2, 3]", "[4, 2, 3]", "[1, 4, 3]", "[1, 2, 4]"], "ans": "[1, 4, 3]"},
#     {"q": "What is the result of `\"a\" * 3`?", "opts": ["Error", "\"a3\"", "\"aaa\"", "\"a a a\""], "ans": "\"aaa\""},
#     {"q": "What is the output of `len({\"a\": 1, \"b\": 2, \"a\": 3})`?", "opts": ["1", "2", "3", "Error"], "ans": "2"},
#     {"q": "What does `bool([])` evaluate to?", "opts": ["True", "False", "None", "Error"], "ans": "False"},
#     {"q": "What is the result of `10 % 3`?", "opts": ["3.33", "3", "1", "0"], "ans": "1"},
#     {"q": "What happens with this code: `t = (1, 2); t[0] = 3`?", "opts": ["t becomes (3, 2)", "t becomes [3, 2]", "Raises TypeError", "Raises SyntaxError"], "ans": "Raises TypeError"},
#     {"q": "What is the output of `[1, 2, 3, 4][1:3]`?", "opts": ["[1, 2]", "[2, 3]", "[2, 3, 4]", "[1, 2, 3]"], "ans": "[2, 3]"},
#     {"q": "What list is equivalent to `list(range(3))`?", "opts": ["[1, 2, 3]", "[0, 1, 2]", "[1, 2]", "[0, 1]"], "ans": "[0, 1, 2]"},
#     {"q": "What is the output of `len({1, 2, 2, 3})`?", "opts": ["2", "3", "4", "Error"], "ans": "3"},
#     {"q": "Output of: `def f(x=1): return x+1; print(f())`?", "opts": ["TypeError", "None", "1", "2"], "ans": "2"},
#     {"q": "What is the result of `'hello'.upper()`?", "opts": ["'Hello'", "'HELLO'", "Error", "'hello'"], "ans": "'HELLO'"},
#     {"q": "`print('a' in 'banana')` outputs:", "opts": ["True", "False", "0", "1"], "ans": "True"},
#     {"q": "Output of: `x = 5; x += 3; print(x)`?", "opts": ["5", "3", "8", "53"], "ans": "8"},
#     {"q": "What is the output of `\"1\" + \"2\"`?", "opts": ["3", "\"12\"", "Error", "\"3\""], "ans": "\"12\""},
#     {"q": "What happens when you run `int(\"10.5\")`?", "opts": ["Returns 10", "Returns 11", "Returns 10.5", "Raises ValueError"], "ans": "Raises ValueError"},
#     {"q": "What is the output of `a = 10; b = 10; print(a is b)`?", "opts": ["True", "False", "Error", "None"], "ans": "True"},
#     {"q": "Evaluate `(1, 2, 3) * 2`:", "opts": ["(2, 4, 6)", "(1, 2, 3, 1, 2, 3)", "((1, 2, 3), (1, 2, 3))", "Error"], "ans": "(1, 2, 3, 1, 2, 3)"},
#     {"q": "Output of `{1: 'a', 2: 'b'}.get(3, 'c')`?", "opts": ["Error", "None", "'c'", "'b'"], "ans": "'c'"}
# ]

# theoretical_mcqs = [
#     {"q": "Which of these is not a core data type?", "opts": ["Lists", "Dictionary", "Tuples", "Class"], "ans": "Class"},
#     {"q": "Which of the following is an immutable data type?", "opts": ["List", "Dictionary", "Set", "Tuple"], "ans": "Tuple"},
#     {"q": "What is the primary difference between a list and a tuple?", "opts": ["Lists are mutable, tuples are immutable", "Tuples are mutable, lists are immutable", "Lists can store different data types", "Tuples can store different data types"], "ans": "Lists are mutable, tuples are immutable"},
#     {"q": "Which keyword is used to define a custom function?", "opts": ["func", "define", "def", "lambda"], "ans": "def"},
#     {"q": "What best describes a Python dictionary?", "opts": ["An ordered sequence of items", "A collection of key-value pairs", "An immutable list", "A set of unique numbers"], "ans": "A collection of key-value pairs"},
#     {"q": "What is the purpose of the `continue` statement?", "opts": ["Exit a loop immediately", "Skip rest of iteration and move next", "Restart the loop from beginning", "Return a value from function"], "ans": "Skip rest of iteration and move next"},
#     {"q": "How do you start a single-line comment in Python?", "opts": ["//", "/*", "<!--", "#"], "ans": "#"},
#     {"q": "What is 'Type Casting'?", "opts": ["Checking variable type", "Converting between data types", "Assigning strict types", "Deleting data type"], "ans": "Converting between data types"},
#     {"q": "What is the scope of a variable defined inside a function?", "opts": ["Global", "Local", "Nonlocal", "Module"], "ans": "Local"},
#     {"q": "What is the default return value of a function missing a return?", "opts": ["0", "False", "None", "Error"], "ans": "None"}
# ]

# with st.form("quiz_form"):
#     user_answers = {}
    
#     st.subheader("💻 Practical Set")
#     for i, mcq in enumerate(practical_mcqs):
#         with st.container(border=True):
#             st.markdown(f"<div class='question-number'>Question {i+1}</div>", unsafe_allow_html=True)
#             st.markdown(f"<hr>", unsafe_allow_html=True)
#             st.markdown(f"<div class='question-text'>{mcq['q']}</div>", unsafe_allow_html=True)
            
#             # Prepend A, B, C, D visually
#             formatted_opts = [f"{prefixes[idx]} \u00A0\u00A0 {opt}" for idx, opt in enumerate(mcq['opts'])]
            
#             selection = st.radio(
#                 f"prac_{i}", 
#                 formatted_opts, 
#                 key=f"p_{i}", 
#                 label_visibility="collapsed", 
#                 index=None
#             )
            
#             # Map the selected string back to the original answer
#             if selection:
#                 # remove prefix logic (first 4 chars: "Ⓐ    ")
#                 user_answers[f"prac_{i}"] = selection[4:].strip()
#             else:
#                 user_answers[f"prac_{i}"] = None
                
#     st.write("---")
    
#     st.subheader("💭 Theoretical Set")
#     for i, mcq in enumerate(theoretical_mcqs):
#         with st.container(border=True):
#             st.markdown(f"<div class='question-number'>Question {i+21}</div>", unsafe_allow_html=True)
#             st.markdown(f"<hr>", unsafe_allow_html=True)
#             st.markdown(f"<div class='question-text'>{mcq['q']}</div>", unsafe_allow_html=True)
            
#             formatted_opts = [f"{prefixes[idx]} \u00A0\u00A0 {opt}" for idx, opt in enumerate(mcq['opts'])]
            
#             selection = st.radio(
#                 f"theo_{i}", 
#                 formatted_opts, 
#                 key=f"t_{i}", 
#                 label_visibility="collapsed", 
#                 index=None
#             )
            
#             if selection:
#                 user_answers[f"theo_{i}"] = selection[4:].strip()
#             else:
#                 user_answers[f"theo_{i}"] = None

#     submitted = st.form_submit_button("🚀 Submit Quiz")

#     if submitted:
#         score = 0
#         for i, mcq in enumerate(practical_mcqs):
#             if user_answers.get(f"prac_{i}") == mcq['ans']:
#                 score += 1
#         for i, mcq in enumerate(theoretical_mcqs):
#             if user_answers.get(f"theo_{i}") == mcq['ans']:
#                 score += 1

#         if score == 30:
#             st.balloons()
#             st.markdown(f"<div style='background-color:#064e3b; padding:20px; border-radius:10px; color:#34d399; font-weight:bold; font-size:20px; text-align:center;'>🎉 Perfect Score! You got {score} / 30 marks!</div>", unsafe_allow_html=True)
#         elif score >= 20:
#             st.markdown(f"<div style='background-color:#1e3a8a; padding:20px; border-radius:10px; color:#60a5fa; font-weight:bold; font-size:20px; text-align:center;'>🌟 Great job! You got {score} / 30 marks.</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div style='background-color:#7f1d1d; padding:20px; border-radius:10px; color:#f87171; font-weight:bold; font-size:20px; text-align:center;'>👍 Good effort. You got {score} / 30 marks. Keep reviewing the concepts!</div>", unsafe_allow_html=True)
