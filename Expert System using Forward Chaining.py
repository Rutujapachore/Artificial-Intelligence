facts = ['fever', 'cough']
rules = {
    'flu': ['fever', 'cough'],
    'cold': ['cough'],
    'covid': ['fever', 'cough', 'breathlessness']
}

def forward_chaining(facts, rules):
    inferred = []
    for disease, symptoms in rules.items():
        if all(symptom in facts for symptom in symptoms):
            inferred.append(disease)
    return inferred

result = forward_chaining(facts, rules)
print("Possible Diseases:", result)
