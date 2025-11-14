"""
Script to populate precautions data in MongoDB
"""
from database import mongo
from app import app

# Comprehensive precautions data for all diseases in the training dataset
precautions_data = [
    {"disease": "Fungal infection", "precautions": ["Keep affected area clean and dry", "Avoid sharing personal items", "Wear breathable clothing", "Use antifungal medications as prescribed", "Maintain good hygiene"]},
    {"disease": "Allergy", "precautions": ["Identify and avoid allergens", "Keep windows closed during high pollen seasons", "Use air purifiers at home", "Shower after being outdoors", "Consider allergy medications or immunotherapy"]},
    {"disease": "GERD", "precautions": ["Avoid trigger foods (spicy, fatty, acidic)", "Eat smaller meals", "Don't lie down immediately after eating", "Elevate head while sleeping", "Maintain healthy weight"]},
    {"disease": "Chronic cholestasis", "precautions": ["Follow prescribed medication regimen", "Avoid alcohol", "Eat a balanced low-fat diet", "Regular medical monitoring", "Take vitamin supplements as recommended"]},
    {"disease": "Drug Reaction", "precautions": ["Inform doctors of all medications", "Read medication labels carefully", "Keep list of known drug allergies", "Seek immediate medical attention if reaction occurs", "Don't self-medicate"]},
    {"disease": "Peptic ulcer diseae", "precautions": ["Avoid NSAIDs and aspirin", "Limit alcohol and caffeine", "Quit smoking", "Eat regular balanced meals", "Manage stress effectively"]},
    {"disease": "AIDS", "precautions": ["Take antiretroviral therapy as prescribed", "Practice safe sex", "Don't share needles", "Regular medical check-ups", "Maintain healthy lifestyle"]},
    {"disease": "Diabetes ", "precautions": ["Monitor blood sugar regularly", "Follow diabetic diet plan", "Exercise regularly", "Take medications as prescribed", "Regular foot and eye examinations"]},
    {"disease": "Gastroenteritis", "precautions": ["Stay hydrated with ORS", "Practice good hand hygiene", "Avoid contaminated food and water", "Rest adequately", "Avoid preparing food for others when sick"]},
    {"disease": "Bronchial Asthma", "precautions": ["Avoid allergens and triggers", "Keep inhaler accessible", "Monitor air quality", "Get vaccinated against flu", "Follow asthma action plan"]},
    {"disease": "Hypertension ", "precautions": ["Reduce sodium intake", "Maintain healthy weight", "Exercise regularly", "Limit alcohol", "Take medications as prescribed"]},
    {"disease": "Migraine", "precautions": ["Maintain regular sleep schedule", "Avoid trigger foods", "Stay hydrated", "Manage stress", "Keep headache diary"]},
    {"disease": "Cervical spondylosis", "precautions": ["Maintain good posture", "Do neck exercises regularly", "Use proper pillow support", "Avoid heavy lifting", "Apply heat or cold therapy"]},
    {"disease": "Paralysis (brain hemorrhage)", "precautions": ["Seek immediate emergency care", "Control blood pressure", "Avoid smoking and alcohol", "Follow rehabilitation therapy", "Take prescribed medications regularly"]},
    {"disease": "Jaundice", "precautions": ["Rest adequately", "Stay hydrated", "Avoid alcohol", "Eat light easily digestible food", "Maintain good hygiene"]},
    {"disease": "Malaria", "precautions": ["Use mosquito nets", "Apply insect repellent", "Wear long-sleeved clothing", "Take antimalarial medication if traveling", "Eliminate standing water"]},
    {"disease": "Chicken pox", "precautions": ["Isolate from others", "Avoid scratching blisters", "Keep nails short and clean", "Use calamine lotion for relief", "Stay hydrated"]},
    {"disease": "Dengue", "precautions": ["Prevent mosquito breeding", "Use mosquito repellent", "Wear protective clothing", "Stay hydrated", "Rest and monitor platelet count"]},
    {"disease": "Typhoid", "precautions": ["Drink safe water", "Eat properly cooked food", "Wash hands frequently", "Get vaccinated before travel", "Avoid street food in endemic areas"]},
    {"disease": "hepatitis A", "precautions": ["Practice good hygiene", "Wash hands before meals", "Drink safe water", "Get vaccinated", "Avoid raw or undercooked food"]},
    {"disease": "Hepatitis B", "precautions": ["Get vaccinated", "Practice safe sex", "Don't share needles", "Screen blood products", "Avoid sharing personal items"]},
    {"disease": "Hepatitis C", "precautions": ["Don't share needles or personal items", "Practice safe sex", "Screen blood products", "Get tested if at risk", "Follow treatment regimen"]},
    {"disease": "Hepatitis D", "precautions": ["Get Hepatitis B vaccination", "Avoid sharing needles", "Practice safe sex", "Regular medical monitoring", "Avoid alcohol"]},
    {"disease": "Hepatitis E", "precautions": ["Drink safe water", "Practice good hygiene", "Avoid contaminated food", "Pregnant women take extra precautions", "Cook food thoroughly"]},
    {"disease": "Alcoholic hepatitis", "precautions": ["Stop alcohol consumption immediately", "Follow nutritious diet", "Take prescribed medications", "Regular liver function tests", "Consider counseling"]},
    {"disease": "Tuberculosis", "precautions": ["Complete full course of antibiotics", "Cover mouth when coughing", "Stay isolated during active phase", "Ensure good ventilation", "Regular follow-up tests"]},
    {"disease": "Common Cold", "precautions": ["Wash hands frequently", "Avoid close contact with sick people", "Get adequate rest", "Stay hydrated", "Cover mouth when coughing"]},
    {"disease": "Pneumonia", "precautions": ["Get vaccinated", "Practice good hygiene", "Don't smoke", "Maintain strong immune system", "Seek prompt treatment for respiratory infections"]},
    {"disease": "Dimorphic hemmorhoids(piles)", "precautions": ["Eat high-fiber diet", "Stay hydrated", "Avoid straining during bowel movements", "Exercise regularly", "Don't sit for long periods"]},
    {"disease": "Heart attack", "precautions": ["Control blood pressure and cholesterol", "Exercise regularly", "Eat heart-healthy diet", "Don't smoke", "Manage stress and diabetes"]},
    {"disease": "Varicose veins", "precautions": ["Exercise regularly", "Elevate legs when resting", "Avoid prolonged standing", "Maintain healthy weight", "Wear compression stockings"]},
    {"disease": "Hypothyroidism", "precautions": ["Take thyroid medication as prescribed", "Regular thyroid function tests", "Eat balanced diet", "Monitor symptoms", "Avoid soy if advised"]},
    {"disease": "Hyperthyroidism", "precautions": ["Take prescribed medications", "Regular monitoring of thyroid levels", "Avoid excess iodine", "Manage stress", "Get adequate rest"]},
    {"disease": "Hypoglycemia", "precautions": ["Eat regular meals", "Carry quick sugar source", "Monitor blood sugar", "Adjust medications with doctor", "Avoid excessive alcohol"]},
    {"disease": "Osteoarthristis", "precautions": ["Maintain healthy weight", "Exercise regularly with low impact", "Use joint protection techniques", "Apply heat or cold therapy", "Take prescribed pain relief"]},
    {"disease": "Arthritis", "precautions": ["Stay physically active", "Maintain healthy weight", "Protect joints from overuse", "Use assistive devices if needed", "Follow treatment plan"]},
    {"disease": "(vertigo) Paroymsal  Positional Vertigo", "precautions": ["Avoid sudden head movements", "Get up slowly from lying position", "Do prescribed exercises", "Avoid driving during episodes", "Keep surroundings well-lit"]},
    {"disease": "Acne", "precautions": ["Wash face twice daily", "Avoid touching face", "Use non-comedogenic products", "Don't pop pimples", "Manage stress levels"]},
    {"disease": "Urinary tract infection", "precautions": ["Drink plenty of water", "Urinate frequently", "Wipe front to back", "Avoid irritating feminine products", "Empty bladder after intercourse"]},
    {"disease": "Psoriasis", "precautions": ["Moisturize skin regularly", "Avoid triggers (stress, alcohol)", "Limit sun exposure but get some vitamin D", "Don't scratch affected areas", "Follow prescribed treatment"]},
    {"disease": "Impetigo", "precautions": ["Keep affected area clean", "Avoid touching or scratching", "Don't share personal items", "Wash hands frequently", "Complete antibiotic course"]},
    {"disease": "Gastritis", "precautions": ["Avoid spicy and acidic foods", "Eat smaller meals", "Avoid alcohol and smoking", "Manage stress", "Avoid NSAIDs"]},
    {"disease": "Tension Headache", "precautions": ["Practice good posture", "Take screen breaks", "Apply heat to neck", "Practice relaxation", "Stay hydrated"]},
    {"disease": "Stress", "precautions": ["Practice mindfulness", "Exercise regularly", "Maintain sleep schedule", "Connect with others", "Seek counseling if needed"]},
    {"disease": "Indigestion", "precautions": ["Eat slowly", "Avoid lying down after eating", "Limit fatty foods", "Reduce caffeine", "Avoid large meals before bed"]},
    {"disease": "Food Poisoning", "precautions": ["Stay hydrated", "Rest adequately", "Practice hygiene", "Store food properly", "Avoid raw foods"]}
]

def seed_precautions():
    """Insert precautions data into MongoDB"""
    with app.app_context():
        try:
            # Clear existing precautions
            mongo.db.precautions.delete_many({})
            print("✅ Cleared existing precautions")
            
            # Insert new precautions
            result = mongo.db.precautions.insert_many(precautions_data)
            print(f"✅ Inserted {len(result.inserted_ids)} disease precautions successfully!")
            
            # Verify insertion
            count = mongo.db.precautions.count_documents({})
            print(f"📊 Total diseases with precautions in database: {count}")
            
            # Show sample
            sample = mongo.db.precautions.find_one({"disease": "Paralysis (brain hemorrhage)"})
            if sample:
                print(f"✅ Sample verified: {sample['disease']} has {len(sample['precautions'])} precautions")
            
        except Exception as e:
            print(f"❌ Error seeding precautions: {str(e)}")

if __name__ == "__main__":
    seed_precautions()
