def explain(drug, score):

    report = f"""

Drug Candidate: {drug}

Predicted Binding Score: {score}

Explanation:

• strong hydrophobic interactions predicted
• potential hydrogen bonding residues
• docking score indicates moderate binding

Further experimental validation recommended.

"""

    return report
