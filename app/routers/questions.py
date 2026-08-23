from fastapi import APIRouter

router = APIRouter()

@router.get("/questions")
def questions():
    return [

        {
            "id": 1,
            "question": "How many people live in this household?",
            "type": "number"
        },
        {
            "id": 2,
            "question": "Are there any children under 5 years old in this household?",
            "type": "boolean"
        },
        {
            "id": 3,
            "question": "Are there any adults over 60 years old in this household?",
            "type": "boolean"
        },
        {
            "id": 4,
            "question": "Has any household member been diagnosed with a chronic condition such as diabetes, hypertension, asthma, or heart disease?",
            "type": "boolean"
        },
        {
            "id": 5,
            "question": "Has any household member died from a potentially preventable illness in the last 5 years?",
            "type": "boolean"
        },

        {
            "id": 6,
            "question": "Is there a functioning health facility available to your community?",
            "type": "boolean"
        },
        {
            "id": 7,
            "question": "How long does it take to reach the nearest healthcare facility?",
            "type": "choice",
            "options": [
                "Under 15 minutes",
                "15-30 minutes",
                "30-60 minutes",
                "Over 60 minutes"
            ]
        },
        {
            "id": 8,
            "question": "During your last healthcare visit, how long did you wait to see a provider?",
            "type": "choice",
            "options": [
                "Less than 30 minutes",
                "30 minutes to 2 hours",
                "More than 2 hours",
                "Could not be seen"
            ]
        },
        {
            "id": 9,
            "question": "In the past year, was needed medical care delayed because services were unavailable?",
            "type": "boolean"
        },
        {
            "id": 10,
            "question": "Have you ever skipped seeking medical care because travel was difficult or expensive?",
            "type": "boolean"
        },

        {
            "id": 11,
            "question": "Has your blood pressure been checked by a healthcare worker in the last 12 months?",
            "type": "boolean"
        },
        {
            "id": 12,
            "question": "Has your blood sugar been checked in the last 12 months?",
            "type": "boolean"
        },
        {
            "id": 13,
            "question": "Have you received a general health check-up in the last 2 years?",
            "type": "boolean"
        },
        {
            "id": 14,
            "question": "Have you received counseling on diet, exercise, tobacco use, or disease prevention?",
            "type": "boolean"
        },
        {
            "id": 15,
            "question": "Have you participated in any health awareness or screening camp in the past year?",
            "type": "boolean"
        },

        {
            "id": 16,
            "question": "Has every child in the household received all recommended vaccinations?",
            "type": "choice",
            "options": [
                "All",
                "Some",
                "None",
                "Not Applicable"
            ]
        },
        {
            "id": 17,
            "question": "Has any child missed a vaccination because the service was unavailable?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Don't Know",
                "Not Applicable"
            ]
        },
        {
            "id": 18,
            "question": "During the most recent pregnancy, did the mother receive at least four antenatal visits?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Don't Know",
                "Not Applicable"
            ]
        },
        {
            "id": 19,
            "question": "Did a healthcare worker provide nutrition counseling during pregnancy?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Don't Know",
                "Not Applicable"
            ]
        },
        {
            "id": 20,
            "question": "Was the child's growth monitored in the last year?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Don't Know",
                "Not Applicable"
            ]
        },

        {
            "id": 21,
            "question": "How was the chronic condition first discovered?",
            "type": "choice",
            "options": [
                "Routine Screening",
                "Community Health Worker Visit",
                "Health Camp",
                "Hospital Visit After Symptoms",
                "Emergency Hospitalization",
                "Not Applicable"
            ]
        },
        {
            "id": 22,
            "question": "Was the condition diagnosed before serious complications occurred?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Not Sure",
                "Not Applicable"
            ]
        },
        {
            "id": 23,
            "question": "Has a healthcare worker explained how to prevent disease progression?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Not Applicable"
            ]
        },
        {
            "id": 24,
            "question": "Do you receive regular follow-up visits or appointments for chronic disease care?",
            "type": "choice",
            "options": [
                "Regularly",
                "Occasionally",
                "Rarely",
                "Never",
                "Not Applicable"
            ]
        },
        {
            "id": 25,
            "question": "Have you ever stopped treatment because medicine was unavailable?",
            "type": "choice",
            "options": [
                "Frequently",
                "Sometimes",
                "Never",
                "Not Applicable"
            ]
        },

        {
            "id": 26,
            "question": "Do you currently take medication to prevent complications from a chronic disease?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Not Applicable"
            ]
        },
        {
            "id": 27,
            "question": "Have you ever missed medication doses because of cost?",
            "type": "choice",
            "options": [
                "Frequently",
                "Sometimes",
                "Never",
                "Not Applicable"
            ]
        },
        {
            "id": 28,
            "question": "Have you ever missed medication because it was unavailable?",
            "type": "choice",
            "options": [
                "Frequently",
                "Sometimes",
                "Never",
                "Not Applicable"
            ]
        },
        {
            "id": 29,
            "question": "Do you understand why your medication is prescribed?",
            "type": "choice",
            "options": [
                "Fully",
                "Partially",
                "No",
                "Not Applicable"
            ]
        },
        {
            "id": 30,
            "question": "Has a healthcare provider reviewed your medications in the last year?",
            "type": "choice",
            "options": [
                "Yes",
                "No",
                "Not Applicable"
            ]
        },

        {
            "id": 31,
            "question": "What health problem concerns your household the most?",
            "type": "choice",
            "options": [
                "Diabetes",
                "High Blood Pressure",
                "Heart Disease",
                "Cancer",
                "Maternal Health",
                "Child Health",
                "Infectious Diseases",
                "Mental Health",
                "Other"
            ]
        },
        {
            "id": 32,
            "question": "What preventive service would most improve your family's health?",
            "type": "choice",
            "options": [
                "More Screenings",
                "Mobile Clinics",
                "Health Education",
                "Medicine Availability",
                "Specialist Access",
                "Transportation Support"
            ]
        },
        {
            "id": 33,
            "question": "What is the biggest barrier preventing your household from staying healthy?",
            "type": "choice",
            "options": [
                "Cost",
                "Distance",
                "Lack of Doctors",
                "Lack of Medicines",
                "Lack of Awareness",
                "Transportation",
                "Other"
            ]
        }
    ]