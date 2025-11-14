"""
Script to populate diseases, specializations, and doctors in MongoDB
"""
from database import mongo
from app import app
from bson import ObjectId

# Specializations
specializations_data = [
    {"_id": 1, "specialty_name": "General Medicine", "description": "General medical conditions"},
    {"_id": 2, "specialty_name": "Cardiology", "description": "Heart and cardiovascular diseases"},
    {"_id": 3, "specialty_name": "Neurology", "description": "Brain and nervous system disorders"},
    {"_id": 4, "specialty_name": "Gastroenterology", "description": "Digestive system disorders"},
    {"_id": 5, "specialty_name": "Pulmonology", "description": "Respiratory system diseases"},
    {"_id": 6, "specialty_name": "Infectious Diseases", "description": "Bacterial, viral, and parasitic infections"},
    {"_id": 7, "specialty_name": "Dermatology", "description": "Skin conditions"},
    {"_id": 8, "specialty_name": "Orthopedics", "description": "Bone and joint disorders"},
    {"_id": 9, "specialty_name": "Rheumatology", "description": "Arthritis and autoimmune diseases"},
    {"_id": 10, "specialty_name": "Endocrinology", "description": "Hormonal and metabolic disorders"},
    {"_id": 11, "specialty_name": "Nephrology", "description": "Kidney diseases"},
    {"_id": 12, "specialty_name": "Hepatology", "description": "Liver diseases"},
    {"_id": 13, "specialty_name": "Oncology", "description": "Cancer care"},
    {"_id": 14, "specialty_name": "Hematology", "description": "Blood disorders"},
    {"_id": 15, "specialty_name": "Ophthalmology", "description": "Eye care"},
    {"_id": 16, "specialty_name": "ENT", "description": "Ear, Nose, and Throat"}
]

# Disease to Specialty mapping
diseases_data = [
    {"_id": 1, "disease_name": "Fungal infection", "specialty_id": 7},
    {"_id": 2, "disease_name": "Allergy", "specialty_id": 1},
    {"_id": 3, "disease_name": "GERD", "specialty_id": 4},
    {"_id": 4, "disease_name": "Chronic cholestasis", "specialty_id": 12},
    {"_id": 5, "disease_name": "Drug Reaction", "specialty_id": 1},
    {"_id": 6, "disease_name": "Peptic ulcer diseae", "specialty_id": 4},
    {"_id": 7, "disease_name": "AIDS", "specialty_id": 6},
    {"_id": 8, "disease_name": "Diabetes ", "specialty_id": 10},
    {"_id": 9, "disease_name": "Gastroenteritis", "specialty_id": 4},
    {"_id": 10, "disease_name": "Bronchial Asthma", "specialty_id": 5},
    {"_id": 11, "disease_name": "Hypertension ", "specialty_id": 2},
    {"_id": 12, "disease_name": "Migraine", "specialty_id": 3},
    {"_id": 13, "disease_name": "Cervical spondylosis", "specialty_id": 8},
    {"_id": 14, "disease_name": "Paralysis (brain hemorrhage)", "specialty_id": 3},
    {"_id": 15, "disease_name": "Jaundice", "specialty_id": 12},
    {"_id": 16, "disease_name": "Malaria", "specialty_id": 6},
    {"_id": 17, "disease_name": "Chicken pox", "specialty_id": 6},
    {"_id": 18, "disease_name": "Dengue", "specialty_id": 6},
    {"_id": 19, "disease_name": "Typhoid", "specialty_id": 6},
    {"_id": 20, "disease_name": "hepatitis A", "specialty_id": 12},
    {"_id": 21, "disease_name": "Hepatitis B", "specialty_id": 12},
    {"_id": 22, "disease_name": "Hepatitis C", "specialty_id": 12},
    {"_id": 23, "disease_name": "Hepatitis D", "specialty_id": 12},
    {"_id": 24, "disease_name": "Hepatitis E", "specialty_id": 12},
    {"_id": 25, "disease_name": "Alcoholic hepatitis", "specialty_id": 12},
    {"_id": 26, "disease_name": "Tuberculosis", "specialty_id": 5},
    {"_id": 27, "disease_name": "Common Cold", "specialty_id": 1},
    {"_id": 28, "disease_name": "Pneumonia", "specialty_id": 5},
    {"_id": 29, "disease_name": "Dimorphic hemmorhoids(piles)", "specialty_id": 4},
    {"_id": 30, "disease_name": "Heart attack", "specialty_id": 2},
    {"_id": 31, "disease_name": "Varicose veins", "specialty_id": 2},
    {"_id": 32, "disease_name": "Hypothyroidism", "specialty_id": 10},
    {"_id": 33, "disease_name": "Hyperthyroidism", "specialty_id": 10},
    {"_id": 34, "disease_name": "Hypoglycemia", "specialty_id": 10},
    {"_id": 35, "disease_name": "Osteoarthristis", "specialty_id": 8},
    {"_id": 36, "disease_name": "Arthritis", "specialty_id": 9},
    {"_id": 37, "disease_name": "(vertigo) Paroymsal  Positional Vertigo", "specialty_id": 3},
    {"_id": 38, "disease_name": "Acne", "specialty_id": 7},
    {"_id": 39, "disease_name": "Urinary tract infection", "specialty_id": 11},
    {"_id": 40, "disease_name": "Psoriasis", "specialty_id": 7},
    {"_id": 41, "disease_name": "Impetigo", "specialty_id": 7},
    {"_id": 42, "disease_name": "Gastritis", "specialty_id": 4},
    {"_id": 43, "disease_name": "Tension Headache", "specialty_id": 3},
    {"_id": 44, "disease_name": "Stress", "specialty_id": 1},
    {"_id": 45, "disease_name": "Indigestion", "specialty_id": 4},
    {"_id": 46, "disease_name": "Food Poisoning", "specialty_id": 4}
]

# Doctors data (with updated hospitals from Prayagraj)
doctors_data = [
    # Cardiology Doctors (specialty_id: 2)
    {
        "_id": 1,
        "name": "Dr. Rajesh Kumar",
        "specialty_id": 2,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.rajesh@mnmc.com",
        "contact_no": "+91-9876543210",
        "education": "MBBS, MD (Cardiology)",
        "experience": "15 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri: 9:00 AM-5:00 PM"]
    },
    {
        "_id": 2,
        "name": "Dr. Priya Sharma",
        "specialty_id": 2,
        "hospital_id": 2,  # Kamla Nehru Memorial Hospital
        "email": "dr.priya@knmh.com",
        "contact_no": "+91-9876543211",
        "education": "MBBS, DM (Cardiology)",
        "experience": "12 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Thu-Sat: 10:00 AM-6:00 PM"]
    },
    
    # Neurology Doctors (specialty_id: 3)
    {
        "_id": 3,
        "name": "Dr. Amit Verma",
        "specialty_id": 3,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.amit@mnmc.com",
        "contact_no": "+91-9876543212",
        "education": "MBBS, DM (Neurology)",
        "experience": "18 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Tue-Thu: 9:00 AM-4:00 PM"]
    },
    {
        "_id": 4,
        "name": "Dr. Sneha Gupta",
        "specialty_id": 3,
        "hospital_id": 13,  # Guru Kripa Jagrati Hospital
        "email": "dr.sneha@gkjh.com",
        "contact_no": "+91-9876543213",
        "education": "MBBS, MD (Neurology)",
        "experience": "10 years",
        "languages": ["Hindi", "English"],
        "availability": ["Wed-Fri-Sat: 11:00 AM-7:00 PM"]
    },
    
    # Gastroenterology Doctors (specialty_id: 4)
    {
        "_id": 5,
        "name": "Dr. Anil Singh",
        "specialty_id": 4,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.anil@mnmc.com",
        "contact_no": "+91-9876543214",
        "education": "MBBS, DM (Gastroenterology)",
        "experience": "14 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri: 9:00 AM-5:00 PM"]
    },
    {
        "_id": 6,
        "name": "Dr. Kavita Rao",
        "specialty_id": 4,
        "hospital_id": 7,  # Awadh Hospital
        "email": "dr.kavita@awadh.com",
        "contact_no": "+91-9876543215",
        "education": "MBBS, MD (Gastroenterology)",
        "experience": "11 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Thu-Sat: 10:00 AM-6:00 PM"]
    },
    
    # General Medicine Doctors (specialty_id: 1)
    {
        "_id": 7,
        "name": "Dr. Suresh Yadav",
        "specialty_id": 1,
        "hospital_id": 1,  # Swaroop Rani Nehru Hospital
        "email": "dr.suresh@srnh.com",
        "contact_no": "+91-9876543216",
        "education": "MBBS, MD (Medicine)",
        "experience": "20 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Tue-Wed-Thu-Fri: 9:00 AM-5:00 PM"]
    },
    {
        "_id": 8,
        "name": "Dr. Meena Patel",
        "specialty_id": 1,
        "hospital_id": 10,  # Asha Hospital
        "email": "dr.meena@asha.com",
        "contact_no": "+91-9876543217",
        "education": "MBBS, MD",
        "experience": "13 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri-Sat: 10:00 AM-6:00 PM"]
    },
    
    # Pulmonology Doctors (specialty_id: 5)
    {
        "_id": 9,
        "name": "Dr. Vikram Chaudhary",
        "specialty_id": 5,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.vikram@mnmc.com",
        "contact_no": "+91-9876543218",
        "education": "MBBS, MD (Pulmonology)",
        "experience": "16 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Thu-Fri: 9:00 AM-4:00 PM"]
    },
    
    # Infectious Diseases (specialty_id: 6)
    {
        "_id": 10,
        "name": "Dr. Rahul Mishra",
        "specialty_id": 6,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.rahul@mnmc.com",
        "contact_no": "+91-9876543219",
        "education": "MBBS, MD (Infectious Diseases)",
        "experience": "12 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Sat: 9:00 AM-5:00 PM"]
    },
    
    # Dermatology (specialty_id: 7)
    {
        "_id": 11,
        "name": "Dr. Anjali Tiwari",
        "specialty_id": 7,
        "hospital_id": 2,  # Kamla Nehru Memorial Hospital
        "email": "dr.anjali@knmh.com",
        "contact_no": "+91-9876543220",
        "education": "MBBS, MD (Dermatology)",
        "experience": "9 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Tue-Thu-Fri: 10:00 AM-6:00 PM"]
    },
    
    # Orthopedics (specialty_id: 8)
    {
        "_id": 12,
        "name": "Dr. Manoj Pandey",
        "specialty_id": 8,
        "hospital_id": 17,  # Ashutosh Hospital & Trauma Centre
        "email": "dr.manoj@ashutosh.com",
        "contact_no": "+91-9876543221",
        "education": "MBBS, MS (Orthopedics)",
        "experience": "17 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri-Sat: 9:00 AM-5:00 PM"]
    },
    
    # Rheumatology (specialty_id: 9)
    {
        "_id": 13,
        "name": "Dr. Sunita Joshi",
        "specialty_id": 9,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.sunita@mnmc.com",
        "contact_no": "+91-9876543222",
        "education": "MBBS, DM (Rheumatology)",
        "experience": "11 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Thu-Sat: 10:00 AM-6:00 PM"]
    },
    
    # Endocrinology (specialty_id: 10)
    {
        "_id": 14,
        "name": "Dr. Deepak Saxena",
        "specialty_id": 10,
        "hospital_id": 1,  # Swaroop Rani Nehru Hospital
        "email": "dr.deepak@srnh.com",
        "contact_no": "+91-9876543223",
        "education": "MBBS, DM (Endocrinology)",
        "experience": "14 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri: 9:00 AM-5:00 PM"]
    },
    
    # Nephrology (specialty_id: 11)
    {
        "_id": 15,
        "name": "Dr. Pankaj Kumar",
        "specialty_id": 11,
        "hospital_id": 1,  # Swaroop Rani Nehru Hospital
        "email": "dr.pankaj@srnh.com",
        "contact_no": "+91-9876543224",
        "education": "MBBS, DM (Nephrology)",
        "experience": "13 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Thu-Sat: 10:00 AM-6:00 PM"]
    },
    
    # Hepatology (specialty_id: 12)
    {
        "_id": 16,
        "name": "Dr. Ashok Tripathi",
        "specialty_id": 12,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.ashok@mnmc.com",
        "contact_no": "+91-9876543225",
        "education": "MBBS, DM (Hepatology)",
        "experience": "15 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Tue-Wed-Fri: 9:00 AM-5:00 PM"]
    },
    
    # Oncology (specialty_id: 13)
    {
        "_id": 17,
        "name": "Dr. Ritu Agarwal",
        "specialty_id": 13,
        "hospital_id": 2,  # Kamla Nehru Memorial Hospital (Regional Cancer Centre)
        "email": "dr.ritu@knmh.com",
        "contact_no": "+91-9876543226",
        "education": "MBBS, MD (Oncology)",
        "experience": "16 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Thu-Fri: 9:00 AM-5:00 PM"]
    },
    
    # Ophthalmology (specialty_id: 15)
    {
        "_id": 18,
        "name": "Dr. Vinod Sharma",
        "specialty_id": 15,
        "hospital_id": 10,  # Placeholder for ASG Eye Hospital
        "email": "dr.vinod@asgeye.com",
        "contact_no": "+91-9876543227",
        "education": "MBBS, MS (Ophthalmology)",
        "experience": "19 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Tue-Thu-Fri-Sat: 9:00 AM-6:00 PM"]
    },
    
    # ENT (specialty_id: 16)
    {
        "_id": 19,
        "name": "Dr. Sanjay Dubey",
        "specialty_id": 16,
        "hospital_id": 12,  # Dwarka Hospital
        "email": "dr.sanjay@dwarka.com",
        "contact_no": "+91-9876543228",
        "education": "MBBS, MS (ENT)",
        "experience": "12 years",
        "languages": ["Hindi", "English"],
        "availability": ["Tue-Wed-Fri-Sat: 10:00 AM-6:00 PM"]
    },
    
    # Hematology (specialty_id: 14)
    {
        "_id": 20,
        "name": "Dr. Pooja Mehta",
        "specialty_id": 14,
        "hospital_id": 3,  # Motilal Nehru Medical College
        "email": "dr.pooja@mnmc.com",
        "contact_no": "+91-9876543229",
        "education": "MBBS, DM (Hematology)",
        "experience": "10 years",
        "languages": ["Hindi", "English"],
        "availability": ["Mon-Wed-Fri: 9:00 AM-5:00 PM"]
    }
]

def seed_all():
    """Insert all data into MongoDB"""
    with app.app_context():
        try:
            # 1. Seed Specializations
            mongo.db.specializations.delete_many({})
            mongo.db.specializations.insert_many(specializations_data)
            print(f"✅ Inserted {len(specializations_data)} specializations")
            
            # 2. Seed Diseases
            mongo.db.diseases.delete_many({})
            mongo.db.diseases.insert_many(diseases_data)
            print(f"✅ Inserted {len(diseases_data)} diseases")
            
            # 3. Seed Doctors
            mongo.db.doctors.delete_many({})
            mongo.db.doctors.insert_many(doctors_data)
            print(f"✅ Inserted {len(doctors_data)} doctors")
            
            # Verify
            print(f"\n📊 Database Summary:")
            print(f"   Specializations: {mongo.db.specializations.count_documents({})}")
            print(f"   Diseases: {mongo.db.diseases.count_documents({})}")
            print(f"   Doctors: {mongo.db.doctors.count_documents({})}")
            print(f"   Hospitals: {mongo.db.hospitals.count_documents({})}")
            print(f"   Precautions: {mongo.db.precautions.count_documents({})}")
            
            # Show sample doctor recommendation
            sample_disease = mongo.db.diseases.find_one({"disease_name": "Migraine"})
            if sample_disease:
                specialty_id = sample_disease['specialty_id']
                doctors = list(mongo.db.doctors.find({"specialty_id": specialty_id}))
                print(f"\n✅ Sample: For 'Migraine', specialty_id={specialty_id}")
                print(f"   Recommended doctors: {len(doctors)}")
                for doc in doctors:
                    print(f"   - {doc['name']} at hospital_id {doc['hospital_id']}")
            
        except Exception as e:
            print(f"❌ Error seeding data: {str(e)}")

if __name__ == "__main__":
    seed_all()
