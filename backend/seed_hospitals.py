"""
Script to populate hospitals data in MongoDB for Allahabad and Lucknow
"""
from database import mongo
from app import app

# Hospital data for Allahabad (Prayagraj) and Lucknow
hospitals_data = [
    # Prayagraj (Allahabad) Hospitals
    {
        "_id": 1,
        "name": "Swaroop Rani Nehru Hospital",
        "address": "MG Marg, Civil Lines",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2460000",
        "email": "srnh@prayagraj.gov.in",
        "latitude": 25.4358,
        "longitude": 81.8463,
        "facilities": ["Emergency", "ICU", "Laboratory", "Pharmacy", "Radiology"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics", "Gynecology", "Orthopedics"]
    },
    {
        "_id": 2,
        "name": "Kamla Nehru Memorial Hospital",
        "address": "1, Hasimpur Road, Tagore Town",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211002",
        "contact_no": "+91-532-2460395",
        "email": "knmh@prayagraj.com",
        "latitude": 25.4484,
        "longitude": 81.8411,
        "facilities": ["Emergency", "ICU", "Laboratory", "CT Scan", "X-Ray"],
        "specializations": ["Cardiology", "Neurology", "General Medicine", "Surgery", "Pediatrics"]
    },
    {
        "_id": 3,
        "name": "Motilal Nehru Medical College / Hospital",
        "address": "Colvin Road",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2460174",
        "email": "mln.mc@gmail.com",
        "latitude": 25.4333,
        "longitude": 81.8444,
        "facilities": ["24x7 Emergency", "ICU", "NICU", "Laboratory", "Blood Bank", "Advanced Diagnostics"],
        "specializations": ["All Major Specialties", "Cardiology", "Neurology", "Orthopedics", "Gastroenterology"]
    },
    {
        "_id": 4,
        "name": "Dufferin Hospital (District Women Hospital)",
        "address": "GT Road, Chowk",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211003",
        "contact_no": "+91-532-2420000",
        "email": "dufferin@prayagraj.gov.in",
        "latitude": 25.4520,
        "longitude": 81.8520,
        "facilities": ["Emergency", "Maternity", "NICU", "Laboratory"],
        "specializations": ["Gynecology", "Obstetrics", "Pediatrics", "Women's Health"]
    },
    {
        "_id": 5,
        "name": "Tej Bahadur Sapru Hospital",
        "address": "Stanley Road",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2461000",
        "email": "tbsh@prayagraj.com",
        "latitude": 25.4401,
        "longitude": 81.8325,
        "facilities": ["Emergency", "Laboratory", "X-Ray", "Pharmacy"],
        "specializations": ["General Medicine", "Pediatrics", "Surgery", "Gynecology"]
    },
    {
        "_id": 6,
        "name": "North Central Railway Hospital",
        "address": "Nawab Yusuf Road, Civil Lines",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2408000",
        "email": "ncr.hospital@indianrailways.gov.in",
        "latitude": 25.4370,
        "longitude": 81.8450,
        "facilities": ["Emergency", "ICU", "Laboratory", "Radiology", "Pharmacy"],
        "specializations": ["General Medicine", "Surgery", "Orthopedics", "ENT"]
    },
    {
        "_id": 7,
        "name": "Awadh Hospital (Multispeciality)",
        "address": "Jhunsi, Lilapur Road, Chamangaj",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211019",
        "contact_no": "+91-532-2700000",
        "email": "info@awadhhospital.com",
        "latitude": 25.4800,
        "longitude": 81.8800,
        "facilities": ["24x7 Emergency", "ICU", "CT Scan", "MRI", "Laboratory"],
        "specializations": ["Cardiology", "Neurology", "Orthopedics", "General Medicine", "Surgery"]
    },
    {
        "_id": 8,
        "name": "Ayan Hospital",
        "address": "Kareli",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211016",
        "contact_no": "+91-532-2650000",
        "email": "contact@ayanhospital.com",
        "latitude": 25.4200,
        "longitude": 81.8100,
        "facilities": ["Emergency", "ICU", "Laboratory", "X-Ray"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics"]
    },
    {
        "_id": 9,
        "name": "Ganga Hospital",
        "address": "Near DM Office, Civil Lines",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2425000",
        "email": "info@gangahospital.com",
        "latitude": 25.4350,
        "longitude": 81.8430,
        "facilities": ["Emergency", "Laboratory", "Radiology", "Pharmacy"],
        "specializations": ["General Medicine", "Surgery", "Orthopedics"]
    },
    {
        "_id": 10,
        "name": "Asha Hospital",
        "address": "89/276, Muir Road, Rajapur",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211002",
        "contact_no": "+91-532-2470000",
        "email": "asha.hospital@gmail.com",
        "latitude": 25.4420,
        "longitude": 81.8380,
        "facilities": ["Emergency", "ICU", "Laboratory", "Ultrasound"],
        "specializations": ["General Medicine", "Pediatrics", "Gynecology", "Surgery"]
    },
    {
        "_id": 11,
        "name": "Bhola Hospital",
        "address": "12/13, Darbhanga Colony, Lowther Road",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2465000",
        "email": "bhola.hospital@gmail.com",
        "latitude": 25.4390,
        "longitude": 81.8420,
        "facilities": ["Emergency", "Laboratory", "X-Ray", "Pharmacy"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics"]
    },
    {
        "_id": 12,
        "name": "Dwarka Hospital",
        "address": "3/4, K.P. Kakkar Road",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211003",
        "contact_no": "+91-532-2480000",
        "email": "dwarka.hospital@gmail.com",
        "latitude": 25.4500,
        "longitude": 81.8500,
        "facilities": ["Emergency", "ICU", "Laboratory", "Radiology"],
        "specializations": ["General Medicine", "Surgery", "Orthopedics", "ENT"]
    },
    {
        "_id": 13,
        "name": "Guru Kripa Jagrati Hospital & Research Centre",
        "address": "124/A/1, Civil Station, Thornbill Road",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2455000",
        "email": "gkjhrc@gmail.com",
        "latitude": 25.4340,
        "longitude": 81.8410,
        "facilities": ["Emergency", "ICU", "Laboratory", "CT Scan", "Research Center"],
        "specializations": ["Cardiology", "Neurology", "General Medicine", "Research"]
    },
    {
        "_id": 14,
        "name": "Alka Hospital",
        "address": "42/17 A, Church Lane",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2445000",
        "email": "alka.hospital@gmail.com",
        "latitude": 25.4380,
        "longitude": 81.8400,
        "facilities": ["Emergency", "Laboratory", "X-Ray"],
        "specializations": ["General Medicine", "Pediatrics", "Surgery"]
    },
    {
        "_id": 15,
        "name": "Amardeep Hospital & Research Centre",
        "address": "17A/22, K.P. Kakkar Road, Opp. Rajarshi Mandappam",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211003",
        "contact_no": "+91-532-2490000",
        "email": "amardeep.hrc@gmail.com",
        "latitude": 25.4510,
        "longitude": 81.8510,
        "facilities": ["Emergency", "ICU", "Laboratory", "Research Facility"],
        "specializations": ["Cardiology", "General Medicine", "Surgery", "Research"]
    },
    {
        "_id": 16,
        "name": "Anand Hospital",
        "address": "11/17 Kasturba Gandhi Marg",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211001",
        "contact_no": "+91-532-2435000",
        "email": "anand.hospital@gmail.com",
        "latitude": 25.4360,
        "longitude": 81.8390,
        "facilities": ["Emergency", "Laboratory", "Pharmacy"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics"]
    },
    {
        "_id": 17,
        "name": "Ashutosh Hospital & Trauma Centre",
        "address": "15/20 Hashimpur Road, near Kamla Nehru Hospital",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211002",
        "contact_no": "+91-532-2475000",
        "email": "ashutosh.trauma@gmail.com",
        "latitude": 25.4490,
        "longitude": 81.8415,
        "facilities": ["24x7 Emergency", "Trauma Center", "ICU", "Laboratory"],
        "specializations": ["Trauma Care", "Emergency Medicine", "Surgery", "Orthopedics"]
    },
    {
        "_id": 18,
        "name": "Ayushi Hospital (IVF & Laparoscopy)",
        "address": "800/603 Lajpat Rai Road, Mumford Ganj",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pin_code": "211002",
        "contact_no": "+91-532-2485000",
        "email": "ayushi.ivf@gmail.com",
        "latitude": 25.4410,
        "longitude": 81.8330,
        "facilities": ["IVF Center", "Laparoscopy", "Laboratory", "Ultrasound"],
        "specializations": ["Fertility", "IVF", "Laparoscopy", "Gynecology"]
    },
    
    # Lucknow Hospitals
    {
        "_id": 19,
        "name": "King George's Medical University",
        "address": "Shah Mina Road, Chowk",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226003",
        "contact_no": "+91-522-2257450",
        "email": "registrar@kgmu.org",
        "latitude": 26.8571,
        "longitude": 80.9410,
        "facilities": ["Trauma Center", "ICU", "NICU", "Blood Bank", "Advanced Diagnostics"],
        "specializations": ["All Major Specialties", "Neurosurgery", "Cardiology", "Oncology"]
    },
    {
        "_id": 20,
        "name": "Sahara Hospital",
        "address": "Viraj Khand, Gomti Nagar",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226010",
        "contact_no": "+91-522-6700000",
        "email": "info@saharahospital.com",
        "latitude": 26.8552,
        "longitude": 81.0157,
        "facilities": ["24x7 Emergency", "ICU", "Cath Lab", "MRI", "CT Scan"],
        "specializations": ["Cardiology", "Neurology", "Orthopedics", "Gastroenterology", "Oncology"]
    },
    {
        "_id": 21,
        "name": "Medanta Lucknow",
        "address": "Sector B, Amar Shaheed Path",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226028",
        "contact_no": "+91-522-4580000",
        "email": "enquiry.lucknow@medanta.org",
        "latitude": 26.9157,
        "longitude": 81.0042,
        "facilities": ["Emergency", "ICU", "Transplant Unit", "Advanced Diagnostics", "Blood Bank"],
        "specializations": ["Cardiology", "Cardiac Surgery", "Neurology", "Oncology", "Transplant"]
    },
    {
        "_id": 22,
        "name": "Apollomedics Super Speciality Hospital",
        "address": "Sector B, Bargawan, LDA Colony",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226012",
        "contact_no": "+91-522-4920000",
        "email": "info@apollomedics.com",
        "latitude": 26.8997,
        "longitude": 81.0042,
        "facilities": ["24x7 Emergency", "ICU", "Cath Lab", "CT Scan", "MRI"],
        "specializations": ["Cardiology", "Neurology", "Orthopedics", "Nephrology", "Urology"]
    },
    {
        "_id": 23,
        "name": "Regency Hospital",
        "address": "Block E, Kanpur - Lucknow Road, Sushant Golf City",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226030",
        "contact_no": "+91-522-4040000",
        "email": "info@regencyhealthcare.in",
        "latitude": 26.9124,
        "longitude": 80.9735,
        "facilities": ["Emergency", "ICU", "Laboratory", "Radiology", "Pharmacy"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics", "Gynecology", "Orthopedics"]
    },
    {
        "_id": 24,
        "name": "Vivekananda Polyclinic",
        "address": "Vivekananda Polyclinic Road, Nirala Nagar",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226020",
        "contact_no": "+91-522-4108888",
        "email": "info@vivekanandahospital.com",
        "latitude": 26.8708,
        "longitude": 80.9906,
        "facilities": ["Emergency", "ICU", "Laboratory", "X-Ray", "Ultrasound"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics", "Orthopedics", "ENT"]
    },
    {
        "_id": 25,
        "name": "Mayo Hospital",
        "address": "Civil Lines",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "pin_code": "226001",
        "contact_no": "+91-522-2627078",
        "email": "mayohospital@lucknow.com",
        "latitude": 26.8640,
        "longitude": 80.9453,
        "facilities": ["Emergency", "ICU", "Laboratory", "Radiology"],
        "specializations": ["General Medicine", "Surgery", "Pediatrics", "Gynecology"]
    }
]

def seed_hospitals():
    """Insert hospital data into MongoDB"""
    with app.app_context():
        try:
            # Clear existing hospitals
            result = mongo.db.hospitals.delete_many({})
            print(f"✅ Cleared {result.deleted_count} existing hospitals")
            
            # Insert new hospitals
            result = mongo.db.hospitals.insert_many(hospitals_data)
            print(f"✅ Inserted {len(result.inserted_ids)} hospitals successfully!")
            
            # Verify insertion
            allahabad_count = mongo.db.hospitals.count_documents({"city": "Prayagraj"})
            lucknow_count = mongo.db.hospitals.count_documents({"city": "Lucknow"})
            total_count = mongo.db.hospitals.count_documents({})
            
            print(f"📊 Prayagraj (Allahabad) hospitals: {allahabad_count}")
            print(f"📊 Lucknow hospitals: {lucknow_count}")
            print(f"📊 Total hospitals in database: {total_count}")
            
            # Show sample
            sample = mongo.db.hospitals.find_one({"city": "Prayagraj"})
            if sample:
                print(f"\n✅ Sample hospital: {sample['name']}, {sample['city']}")
                print(f"   Contact: {sample['contact_no']}")
            
        except Exception as e:
            print(f"❌ Error seeding hospitals: {str(e)}")

if __name__ == "__main__":
    seed_hospitals()
