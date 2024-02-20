dietDict = {
    'd1': 'Balanced Diet',
    'd2': 'Mediterranean Diet',
    'd3': 'Keto Diet',
    'd4': 'Intermittent Fasting',
    'd5': 'Paleo Diet',
    'd6': 'DASH Diet',
    'd7': 'Zone Diet'
}

categoryDict = {
    'c1': 'Slender',
    'c2': 'Normal Weight and Healthy',
    'c3': 'Overweight',
    'c4': 'Obesity Class 1',
    'c5': 'Obesity Class 2',
    'c6': 'Obesity Class 3'
}

diabeticDict = {
    0: 'No',
    1: 'Yes',
    2: 'Not Sure'
}

def dietRec(category, diabetic):
    if diabetic == 0:
        if category == categoryDict['c1']:
            return dietDict['d1']
        elif category == categoryDict['c2']:
            return dietDict['d1']
        elif category == categoryDict['c3']:
            return dietDict['d6']
        elif category == categoryDict['c4']:
            return dietDict['d1']
        elif category == categoryDict['c5']:
            return dietDict['d1']
        elif category == categoryDict['c6']:
            return dietDict['d1']
    elif diabetic == 1:
        if category == categoryDict['c1']:
            return dietDict['d2']
        elif category == categoryDict['c2']:
            return dietDict['d2']
        elif category == categoryDict['c3']:
            return dietDict['d6']
        elif category == categoryDict['c4']:
            return dietDict['d3']
        elif category == categoryDict['c5']:
            return dietDict['d3']
        elif category == categoryDict['c6']:
            return dietDict['d3']
    elif diabetic == 2:
        if category == categoryDict['c1']:
            return dietDict['d7']
        elif category == categoryDict['c2']:
            return dietDict['d7']
        elif category == categoryDict['c3']:
            return dietDict['d7']
        elif category == categoryDict['c4']:
            return dietDict['d7']
        elif category == categoryDict['c5']:
            return dietDict['d7']
        elif category == categoryDict['c6']:
            return dietDict['d7']
        
category = categoryDict['c3']
diabetic = 0
recommended_diet = dietRec(category, diabetic)
print(f"For {category} and diabetic status {diabeticDict[diabetic]}, the recommended diet is: {recommended_diet}")
