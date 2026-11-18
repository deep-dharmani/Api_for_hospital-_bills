import uvicorn
from fastapi import FastAPI
hospital_fees_api=FastAPI()
diseases={
    "commoncold":{"Doctor fee":1000,"Tests":500,"medicines":800,\
"Total":2300},
    "typhoid":{"Doctor fee":1500,"Tests":2000,"medicines":2500,\
"Total":6000},
    "dengue":{"Doctor fee":2000,"Tests":2500,"medicines":2000,\
"Total":6500},
    "diabetes":{"Doctor fee":2500,"Tests":1500,"medicines":2000,\
"Total":6000},
    "hypertension":{"Doctor fee":2000,"Tests":1000,"medicines":1500,\
"Total":4500},
    "asthma":{"Doctor fee":2500,"Tests":2000,"medicines":2500,\
"Total":7000},
    "migraine":{"Doctor fee":3000,"Tests":1500,"medicines":1500,\
"Total":6000},
    "skinallergy":{"Doctor fee":2000,"Tests":1000,"medicines":1000,\
"Total":4000},
    "gastritis":{"Doctor fee":2500,"Tests":1500,"medicines":1500,\
"Total":5500},
    "kidneystone":{"Doctor fee":3000,"Tests":3000,"medicines":3000,\
"Total":9000}
}
diseases.update({

    "flu": {"Doctor fee": 1000, "Tests": 500, "medicines": 1000, "Total": 2500},
    "covid19": {"Doctor fee": 1500, "Tests": 2000, "medicines": 1500, "Total": 5000},
    "pneumonia": {"Doctor fee": 2500, "Tests": 3000, "medicines": 2500, "Total": 8000},
    "bronchitis": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "tuberculosis": {"Doctor fee": 2500, "Tests": 3000, "medicines": 4000, "Total": 9500},
    "sinusitis": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1200, "Total": 3700},
    "tonsillitis": {"Doctor fee": 1500, "Tests": 800, "medicines": 1200, "Total": 3500},
    "pharyngitis": {"Doctor fee": 1200, "Tests": 500, "medicines": 1000, "Total": 2700},
    "laryngitis": {"Doctor fee": 1200, "Tests": 500, "medicines": 1000, "Total": 2700},
    "earinfection": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1200, "Total": 3700},

    "conjunctivitis": {"Doctor fee": 1500, "Tests": 500, "medicines": 1000, "Total": 3000},
    "cataract": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1500, "Total": 6000},
    "glaucoma": {"Doctor fee": 3000, "Tests": 2500, "medicines": 2000, "Total": 7500},
    "dryeye": {"Doctor fee": 1200, "Tests": 500, "medicines": 800, "Total": 2500},
    "eczema": {"Doctor fee": 2000, "Tests": 1000, "medicines": 1200, "Total": 4200},
    "psoriasis": {"Doctor fee": 2500, "Tests": 1500, "medicines": 2000, "Total": 6000},
    "acne": {"Doctor fee": 1500, "Tests": 500, "medicines": 1000, "Total": 3000},
    "ringworm": {"Doctor fee": 1500, "Tests": 800, "medicines": 1000, "Total": 3300},
    "scabies": {"Doctor fee": 1500, "Tests": 500, "medicines": 1000, "Total": 3000},
    "urticaria": {"Doctor fee": 2000, "Tests": 1000, "medicines": 1200, "Total": 4200},

    "anemia": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "irondeficiency": {"Doctor fee": 1500, "Tests": 1200, "medicines": 1000, "Total": 3700},
    "vitaminddeficiency": {"Doctor fee": 1500, "Tests": 1200, "medicines": 1000, "Total": 3700},
    "vitaminb12deficiency": {"Doctor fee": 1800, "Tests": 1500, "medicines": 1200, "Total": 4500},
    "hypothyroidism": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1500, "Total": 6000},
    "hyperthyroidism": {"Doctor fee": 2500, "Tests": 2500, "medicines": 2000, "Total": 7000},
    "obesity": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1000, "Total": 4500},
    "malnutrition": {"Doctor fee": 1500, "Tests": 1500, "medicines": 1200, "Total": 4200},
    "osteoporosis": {"Doctor fee": 2500, "Tests": 2500, "medicines": 2000, "Total": 7000},
    "arthritis": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1800, "Total": 6300},

    "rheumatoidarthritis": {"Doctor fee": 3000, "Tests": 2500, "medicines": 2500, "Total": 8000},
    "backpain": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1000, "Total": 3500},
    "jointpain": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1000, "Total": 3500},
    "sciatica": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "slipdisc": {"Doctor fee": 2500, "Tests": 3000, "medicines": 2000, "Total": 7500},
    "gout": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "musclecramps": {"Doctor fee": 1000, "Tests": 500, "medicines": 800, "Total": 2300},
    "neckpain": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1000, "Total": 3500},
    "osteomyelitis": {"Doctor fee": 3000, "Tests": 3000, "medicines": 3000, "Total": 9000},
    "fibromyalgia": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1800, "Total": 6300},

    "diarrhea": {"Doctor fee": 1000, "Tests": 800, "medicines": 800, "Total": 2600},
    "constipation": {"Doctor fee": 1000, "Tests": 500, "medicines": 800, "Total": 2300},
    "foodpoisoning": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1200, "Total": 3700},
    "acidreflux": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1000, "Total": 3500},
    "pepticulcer": {"Doctor fee": 2000, "Tests": 2000, "medicines": 1800, "Total": 5800},
    "irritablebowelsyndrome": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1500, "Total": 6000},
    "hepatitisA": {"Doctor fee": 2500, "Tests": 2500, "medicines": 2000, "Total": 7000},
    "hepatitisB": {"Doctor fee": 3000, "Tests": 3000, "medicines": 2500, "Total": 8500},
    "hepatitisC": {"Doctor fee": 3000, "Tests": 3500, "medicines": 3000, "Total": 9500},
    "jaundice": {"Doctor fee": 2000, "Tests": 2000, "medicines": 1500, "Total": 5500},

    "urinarytractinfection": {"Doctor fee": 1500, "Tests": 1200, "medicines": 1500, "Total": 4200},
    "kidneyinfection": {"Doctor fee": 2500, "Tests": 2500, "medicines": 2500, "Total": 7500},
    "bladderinfection": {"Doctor fee": 1500, "Tests": 1200, "medicines": 1500, "Total": 4200},
    "prostatitis": {"Doctor fee": 2500, "Tests": 2000, "medicines": 2000, "Total": 6500},
    "polycystickidneydisease": {"Doctor fee": 3000, "Tests": 3000, "medicines": 2500, "Total": 8500},
    "gallstones": {"Doctor fee": 2500, "Tests": 2500, "medicines": 1500, "Total": 6500},
    "appendicitis": {"Doctor fee": 3000, "Tests": 3000, "medicines": 2000, "Total": 8000},
    "hemorrhoids": {"Doctor fee": 1500, "Tests": 1000, "medicines": 1200, "Total": 3700},
    "analfissure": {"Doctor fee": 1500, "Tests": 800, "medicines": 1000, "Total": 3300},
    "hernia": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1500, "Total": 6000},

    "heartdisease": {"Doctor fee": 3000, "Tests": 3500, "medicines": 2500, "Total": 9000},
    "coronaryarterydisease": {"Doctor fee": 3500, "Tests": 4000, "medicines": 3000, "Total": 10500},
    "arrhythmia": {"Doctor fee": 3000, "Tests": 2500, "medicines": 2000, "Total": 7500},
    "heartfailure": {"Doctor fee": 3500, "Tests": 4000, "medicines": 3000, "Total": 10500},
    "highcholesterol": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "stroke": {"Doctor fee": 4000, "Tests": 5000, "medicines": 3000, "Total": 12000},
    "varicoseveins": {"Doctor fee": 2000, "Tests": 1500, "medicines": 1500, "Total": 5000},
    "deepveinthrombosis": {"Doctor fee": 3000, "Tests": 3000, "medicines": 2500, "Total": 8500},
    "peripheralneuropathy": {"Doctor fee": 2500, "Tests": 2000, "medicines": 1800, "Total": 6300},
    "epilepsy": {"Doctor fee": 3000, "Tests": 2500, "medicines": 2000, "Total": 7500},

    "insomnia": {"Doctor fee": 1500, "Tests": 500, "medicines": 1000, "Total": 3000},
    "sleepapnea": {"Doctor fee": 2500, "Tests": 3000, "medicines": 1500, "Total": 7000},
    "parkinsons": {"Doctor fee": 3000, "Tests": 2500, "medicines": 2500, "Total": 8000},
    "alzheimers": {"Doctor fee": 3500, "Tests": 3000, "medicines": 2500, "Total": 9000},
    "anxietydisorder": {"Doctor fee": 2000, "Tests": 500, "medicines": 1500, "Total": 4000},
    "depression": {"Doctor fee": 2000, "Tests": 500, "medicines": 1500, "Total": 4000},
    "panicdisorder": {"Doctor fee": 2000, "Tests": 500, "medicines": 1500, "Total": 4000},
    "ocd": {"Doctor fee": 2500, "Tests": 500, "medicines": 1500, "Total": 4500},
    "adhd": {"Doctor fee": 2500, "Tests": 1000, "medicines": 2000, "Total": 5500},
    "meningitis": {"Doctor fee": 3500, "Tests": 4000, "medicines": 3000, "Total": 10500}

})
@hospital_fees_api.post("/")
def add_disease(disease:str):
    if disease not in diseases:
        msg=f"we did'nt treat that disease"
    else:
        msg=diseases[disease.lower().replace(" ","")]
    return msg
if __name__=="__main__":
    uvicorn.run("main:hospital_fees_api",\
host="127.0.0.1",port=8000)
