import json
import os

class data:
    def __init__(self):
        pass

    def user_data(self,want):
        generations = {
    "generation_tree": {
        "paternal": {
            "father": {
                "name": "Rajesh Kumar",
                "relation": "Father",
                "health_conditions": ["Diabetes Type 2", "Hypertension", "Bronchitis"],
                "born": "1975",
                "status": "Alive (Age 50)"
            },
            "paternal_grandfather": {
                "name": "Suresh Kumar",
                "relation": "Paternal Grandfather",
                "health_conditions": ["Hypertension", "Heart Disease", "Asthma"],
                "born": "1948",
                "status": "Deceased (Age 72)"
            },
            "paternal_grandmother": {
                "name": "Kamla Devi",
                "relation": "Paternal Grandmother",
                "health_conditions": ["Arthritis", "Osteoporosis", "Migraine"],
                "born": "1950",
                "status": "Alive (Age 75)"
            },
            "paternal_great_grandfather": {
                "name": "Hari Kumar",
                "relation": "Paternal Great-Grandfather",
                "health_conditions": ["Heart Disease", "Diabetes Type 2"],
                "born": "1920",
                "status": "Deceased (Age 80)"
            },
            "paternal_great_grandmother": {
                "name": "Savitri Kumar",
                "relation": "Paternal Great-Grandmother",
                "health_conditions": ["Arthritis", "High Cholesterol"],
                "born": "1923",
                "status": "Deceased (Age 85)"
            },
            "paternal_uncle": {
                "name": "Vikram Kumar",
                "relation": "Paternal Uncle",
                "health_conditions": ["Diabetes Type 2", "Allergic Reactions"],
                "born": "1978",
                "status": "Alive (Age 47)"
            },
            "paternal_cousin": {
                "name": "Rohan Kumar",
                "relation": "Paternal Cousin",
                "health_conditions": ["Asthma", "Allergic Reactions"],
                "born": "2003",
                "status": "Alive (Age 22)"
            }
        },
        "maternal": {
            "mother": {
                "name": "Priya Sharma",
                "relation": "Mother",
                "health_conditions": ["Thyroid Disorder", "Migraine", "Allergic Reactions"],
                "born": "1978",
                "status": "Alive (Age 47)"
            },
            "maternal_grandfather": {
                "name": "Vikram Sharma",
                "relation": "Maternal Grandfather",
                "health_conditions": ["Asthma", "Allergic Reactions", "Bronchitis"],
                "born": "1945",
                "status": "Alive (Age 80)"
            },
            "maternal_grandmother": {
                "name": "Lata Sharma",
                "relation": "Maternal Grandmother",
                "health_conditions": ["Common Cold Susceptibility", "Joint Pain", "Migraine"],
                "born": "1947",
                "status": "Deceased (Age 68)"
            },
            "maternal_great_grandfather": {
                "name": "Mohan Sharma",
                "relation": "Maternal Great-Grandfather",
                "health_conditions": ["Asthma", "Heart Disease"],
                "born": "1918",
                "status": "Deceased (Age 75)"
            },
            "maternal_great_grandmother": {
                "name": "Kamla Sharma",
                "relation": "Maternal Great-Grandmother",
                "health_conditions": ["Diabetes Type 1", "Arthritis"],
                "born": "1920",
                "status": "Deceased (Age 78)"
            },
            "maternal_aunt": {
                "name": "Anita Sharma",
                "relation": "Maternal Aunt",
                "health_conditions": ["Thyroid Disorder", "Migraine"],
                "born": "1980",
                "status": "Alive (Age 45)"
            },
            "maternal_cousin": {
                "name": "Sneha Sharma",
                "relation": "Maternal Cousin",
                "health_conditions": ["Allergic Reactions", "Migraine"],
                "born": "2005",
                "status": "Alive (Age 20)"
            }
        },
        "siblings": [
            {
                "name": "Amit Kumar",
                "relation": "Elder Brother",
                "health_conditions": ["Allergic Reactions", "Asthma"],
                "born": "2005",
                "status": "Alive (Age 20)"
            },
            {
                "name": "Neha Kumar",
                "relation": "Younger Sister",
                "health_conditions": ["Migraine", "Common Cold Susceptibility"],
                "born": "2012",
                "status": "Alive (Age 13)"
            }
        ],
        "patient": {
            "name": "Ayush Kumar",
            "relation": "Self",
            "health_conditions": ["History of Viral Infections", "Allergic Reactions", "Migraine Episodes", "Asthma", "Arthritis"],
            "born": "2010",
            "status": "Alive (Age 15)"
        }
    }
}

        history = {
    "history": [
        {
            "date_time": "2025-10-21 15:42",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2025-10-03 04:05",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2025-09-14 22:09",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Bronchitis, expectorant",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2025-07-22 21:08",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2025-07-22 16:04",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2025-06-25 21:43",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2025-06-25 17:29",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Henry Garcia",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Outpatient F"
        },
        {
            "date_time": "2025-04-23 09:35",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2025-04-01 03:02",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Bronchitis, expectorant",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2025-03-06 02:38",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "Specialist G"
        },
        {
            "date_time": "2025-02-24 03:02",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "City General Hospital"
        },
        {
            "date_time": "2025-02-19 19:51",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Bronchitis, expectorant",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2025-02-16 00:09",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Bronchitis, expectorant",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2025-01-13 13:41",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2025-01-03 21:23",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Henry Garcia",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "City General Hospital"
        },
        {
            "date_time": "2024-11-12 14:32",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2024-10-31 02:41",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Outpatient F"
        },
        {
            "date_time": "2024-09-26 10:36",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Food poisoning, hydration",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2024-09-11 22:26",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2024-09-08 17:23",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Food poisoning, hydration",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2024-09-07 17:08",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2024-09-06 19:34",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Bronchitis, expectorant",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2024-09-01 11:05",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "City General Hospital"
        },
        {
            "date_time": "2024-08-29 22:30",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Specialist G"
        },
        {
            "date_time": "2024-08-24 16:41",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2024-08-24 14:40",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "Specialist G"
        },
        {
            "date_time": "2024-07-17 11:36",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Food poisoning, hydration",
            "location": "Primary Care D"
        },
        {
            "date_time": "2024-06-30 17:51",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "City General Hospital"
        },
        {
            "date_time": "2024-06-10 17:38",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Specialist G"
        },
        {
            "date_time": "2024-05-19 11:59",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2024-03-23 17:37",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2024-02-18 21:40",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Specialist G"
        },
        {
            "date_time": "2024-02-18 19:04",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2024-02-06 17:56",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "Primary Care D"
        },
        {
            "date_time": "2024-01-20 08:09",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2023-12-05 20:18",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Specialist G"
        },
        {
            "date_time": "2023-09-29 02:46",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2023-09-27 23:56",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2023-09-23 03:25",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "City General Hospital"
        },
        {
            "date_time": "2023-09-11 00:58",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2023-09-10 02:18",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2023-08-16 23:05",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2023-08-08 03:29",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2023-07-27 10:20",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2023-07-23 23:38",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Outpatient F"
        },
        {
            "date_time": "2023-07-15 16:39",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2023-07-06 21:42",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Food poisoning, hydration",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2023-07-02 00:36",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2023-06-19 05:43",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Outpatient F"
        },
        {
            "date_time": "2023-06-13 04:02",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Specialist G"
        },
        {
            "date_time": "2023-05-08 19:03",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2023-03-21 06:22",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "City General Hospital"
        },
        {
            "date_time": "2023-02-08 07:13",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Specialist G"
        },
        {
            "date_time": "2023-01-30 04:02",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Common cold, symptomatic relief",
            "location": "City General Hospital"
        },
        {
            "date_time": "2022-11-30 07:55",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2022-11-29 15:42",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Henry Garcia",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2022-11-14 23:55",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Specialist G"
        },
        {
            "date_time": "2022-11-13 05:46",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Food poisoning, hydration",
            "location": "Specialist G"
        },
        {
            "date_time": "2022-10-17 20:42",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Bronchitis, expectorant",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2022-10-12 18:31",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2022-09-13 11:26",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2022-08-22 09:55",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Bronchitis, expectorant",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2022-08-13 04:08",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Primary Care D"
        },
        {
            "date_time": "2022-07-18 23:14",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Viral infection, rest and fluids",
            "location": "City General Hospital"
        },
        {
            "date_time": "2022-06-30 17:24",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2022-05-22 11:23",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Specialist G"
        },
        {
            "date_time": "2022-05-18 10:40",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2022-05-07 04:12",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2022-04-20 13:34",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2022-04-14 15:23",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Bronchitis, expectorant",
            "location": "Primary Care D"
        },
        {
            "date_time": "2022-04-04 17:58",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "Primary Care D"
        },
        {
            "date_time": "2022-03-25 12:15",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Viral infection, rest and fluids",
            "location": "City General Hospital"
        },
        {
            "date_time": "2021-12-06 04:39",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2021-11-27 04:46",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Primary Care D"
        },
        {
            "date_time": "2021-11-20 07:54",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Food poisoning, hydration",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2021-11-11 15:08",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2021-11-10 23:05",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Food poisoning, hydration",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2021-11-07 18:02",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Primary Care D"
        },
        {
            "date_time": "2021-10-21 03:06",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2021-09-04 18:53",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2021-08-09 09:47",
            "symptoms": "abdominal pain, diarrhea",
            "doctor_name": "Dr. Henry Garcia",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2021-07-25 10:39",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "City General Hospital"
        },
        {
            "date_time": "2021-07-20 01:53",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Food poisoning, hydration",
            "location": "Outpatient F"
        },
        {
            "date_time": "2021-07-06 13:50",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Food poisoning, hydration",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2021-06-21 01:06",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Primary Care D"
        },
        {
            "date_time": "2021-06-20 05:26",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2021-04-30 20:45",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Gastroenteritis, antibiotics",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2021-04-17 18:18",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Allergic reaction, antihistamine",
            "location": "Outpatient F"
        },
        {
            "date_time": "2021-01-25 11:45",
            "symptoms": "cough, wheezing",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2020-12-31 15:54",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Food poisoning, hydration",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2020-12-18 18:42",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Specialist G"
        },
        {
            "date_time": "2020-11-28 06:55",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. Jack Rodriguez",
            "conclusion": "Muscle strain, physiotherapy",
            "location": "Outpatient F"
        },
        {
            "date_time": "2020-11-15 13:33",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Bronchitis, expectorant",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2020-10-18 16:46",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Grace Lee",
            "conclusion": "Food poisoning, hydration",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2020-10-15 23:26",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2020-10-11 07:54",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Food poisoning, hydration",
            "location": "City General Hospital"
        },
        {
            "date_time": "2020-09-28 02:32",
            "symptoms": "fever, cough, fatigue",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2020-09-26 03:05",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Outpatient F"
        },
        {
            "date_time": "2020-08-06 11:11",
            "symptoms": "headache, nausea, dizziness",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Specialist G"
        },
        {
            "date_time": "2020-07-30 04:02",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Eve Brown",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2020-07-21 16:05",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Outpatient F"
        },
        {
            "date_time": "2020-07-08 16:46",
            "symptoms": "joint pain, swelling",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Viral infection, rest and fluids",
            "location": "Specialist G"
        },
        {
            "date_time": "2020-07-02 14:38",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Carol Davis",
            "conclusion": "Bronchitis, expectorant",
            "location": "Medical Hub C"
        },
        {
            "date_time": "2020-06-18 23:59",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Migraine, prescribe pain reliever",
            "location": "Wellness Center B"
        },
        {
            "date_time": "2020-05-11 21:22",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Henry Garcia",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Urgent Care I"
        },
        {
            "date_time": "2020-04-21 02:16",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2020-04-14 09:48",
            "symptoms": "vomiting, dehydration",
            "doctor_name": "Dr. Ivy Martinez",
            "conclusion": "Arthritis flare-up, anti-inflammatory",
            "location": "Family Doctor H"
        },
        {
            "date_time": "2020-03-01 18:55",
            "symptoms": "rash, itching",
            "doctor_name": "Dr. Alice Johnson",
            "conclusion": "Common cold, symptomatic relief",
            "location": "Health Clinic A"
        },
        {
            "date_time": "2020-02-12 01:02",
            "symptoms": "back pain, stiffness",
            "doctor_name": "Dr. David Wilson",
            "conclusion": "Possible asthma attack, inhaler",
            "location": "Emergency Room E"
        },
        {
            "date_time": "2020-02-04 21:40",
            "symptoms": "chest pain, shortness of breath",
            "doctor_name": "Dr. Bob Smith",
            "conclusion": "Viral infection, rest and fluids",
            "location": "City General Hospital"
        },
        {
            "date_time": "2020-01-15 08:27",
            "symptoms": "sore throat, runny nose",
            "doctor_name": "Dr. Frank Miller",
            "conclusion": "Common cold, symptomatic relief",
            "location": "City General Hospital"
        }
    ]
}
        if want == "history":
          return history
        elif want == "generations":
            return generations
        else:
            raise ValueError("command not found")
    
    def doctor_data(self,want):
        history = {
  "doctor_name": "Dr. Tanishqa",
  "patients_treated": [
    {
      "name": "Aditi Sharma",
      "age": 34,
      "symptoms": "fever, cough, fatigue",
      "visit_date": "2025-10-21"
    },
    {
      "name": "Rohan Patel",
      "age": 47,
      "symptoms": "chest pain, shortness of breath",
      "visit_date": "2025-10-20"
    },
    {
      "name": "Sneha Gupta",
      "age": 19,
      "symptoms": "rash, itching",
      "visit_date": "2025-10-18"
    },
    {
      "name": "Vikram Singh",
      "age": 62,
      "symptoms": "joint pain, swelling",
      "visit_date": "2025-10-15"
    },
    {
      "name": "Priya Nair",
      "age": 28,
      "symptoms": "headache, nausea, dizziness",
      "visit_date": "2025-10-12"
    },
    {
      "name": "Arjun Reddy",
      "age": 15,
      "symptoms": "cough, wheezing",
      "visit_date": "2025-10-10"
    },
    {
      "name": "Lakshmi Joshi",
      "age": 53,
      "symptoms": "abdominal pain, diarrhea",
      "visit_date": "2025-10-08"
    },
    {
      "name": "Soham Desai",
      "age": 9,
      "symptoms": "vomiting, dehydration",
      "visit_date": "2025-10-05"
    },
    {
      "name": "Ananya Verma",
      "age": 41,
      "symptoms": "sore throat, runny nose",
      "visit_date": "2025-10-03"
    },
    {
      "name": "Kiran Malhotra",
      "age": 67,
      "symptoms": "back pain, stiffness",
      "visit_date": "2025-10-01"
    },
    {
      "name": "Meera Kapoor",
      "age": 25,
      "symptoms": "fever, fatigue",
      "visit_date": "2025-09-28"
    },
    {
      "name": "Rahul Mehra",
      "age": 50,
      "symptoms": "chest pain, palpitations",
      "visit_date": "2025-09-25"
    },
    {
      "name": "Nisha Yadav",
      "age": 30,
      "symptoms": "rash, swelling",
      "visit_date": "2025-09-22"
    },
    {
      "name": "Amit Choudhary",
      "age": 38,
      "symptoms": "joint pain, fatigue",
      "visit_date": "2025-09-20"
    },
    {
      "name": "Divya Thakur",
      "age": 22,
      "symptoms": "headache, dizziness",
      "visit_date": "2025-09-18"
    },
    {
      "name": "Sanjay Rana",
      "age": 55,
      "symptoms": "cough, shortness of breath",
      "visit_date": "2025-09-15"
    },
    {
      "name": "Pooja Iyer",
      "age": 17,
      "symptoms": "abdominal pain, nausea",
      "visit_date": "2025-09-12"
    },
    {
      "name": "Ravi Menon",
      "age": 64,
      "symptoms": "vomiting, fever",
      "visit_date": "2025-09-10"
    },
    {
      "name": "Tara Bose",
      "age": 29,
      "symptoms": "sore throat, fatigue",
      "visit_date": "2025-09-08"
    },
    {
      "name": "Vivek Saxena",
      "age": 44,
      "symptoms": "back pain, muscle strain",
      "visit_date": "2025-09-05"
    },
    {
      "name": "Ishaan Pillai",
      "age": 12,
      "symptoms": "cough, wheezing",
      "visit_date": "2025-09-03"
    },
    {
      "name": "Kavita Shah",
      "age": 58,
      "symptoms": "joint pain, swelling",
      "visit_date": "2025-09-01"
    },
    {
      "name": "Nikhil Arora",
      "age": 36,
      "symptoms": "fever, runny nose",
      "visit_date": "2025-08-30"
    },
    {
      "name": "Shreya Dubey",
      "age": 24,
      "symptoms": "rash, itching",
      "visit_date": "2025-08-28"
    },
    {
      "name": "Manish Kulkarni",
      "age": 49,
      "symptoms": "chest pain, fatigue",
      "visit_date": "2025-08-25"
    },
    {
      "name": "Aarav Bansal",
      "age": 7,
      "symptoms": "vomiting, dehydration",
      "visit_date": "2025-08-22"
    },
    {
      "name": "Simran Gill",
      "age": 40,
      "symptoms": "headache, nausea",
      "visit_date": "2025-08-20"
    },
    {
      "name": "Yashwant Rao",
      "age": 70,
      "symptoms": "back pain, stiffness",
      "visit_date": "2025-08-18"
    },
    {
      "name": "Neha Varghese",
      "age": 31,
      "symptoms": "sore throat, cough",
      "visit_date": "2025-08-15"
    },
    {
      "name": "Rohit Chawla",
      "age": 53,
      "symptoms": "abdominal pain, diarrhea",
      "visit_date": "2025-08-12"
    },
    {
      "name": "Anjali Seth",
      "age": 26,
      "symptoms": "fever, fatigue",
      "visit_date": "2025-08-10"
    },
    {
      "name": "Kunal Mishra",
      "age": 42,
      "symptoms": "chest pain, shortness of breath",
      "visit_date": "2025-08-08"
    },
    {
      "name": "Saanvi Jha",
      "age": 14,
      "symptoms": "rash, swelling",
      "visit_date": "2025-08-05"
    },
    {
      "name": "Prakash Nair",
      "age": 65,
      "symptoms": "joint pain, stiffness",
      "visit_date": "2025-08-03"
    },
    {
      "name": "Riya Sood",
      "age": 27,
      "symptoms": "headache, dizziness",
      "visit_date": "2025-08-01"
    },
    {
      "name": "Akash Tiwari",
      "age": 39,
      "symptoms": "cough, wheezing",
      "visit_date": "2025-07-30"
    },
    {
      "name": "Tanvi Khanna",
      "age": 20,
      "symptoms": "vomiting, nausea",
      "visit_date": "2025-07-28"
    },
    {
      "name": "Devendra Pal",
      "age": 56,
      "symptoms": "sore throat, runny nose",
      "visit_date": "2025-07-25"
    },
    {
      "name": "Isha Dhawan",
      "age": 33,
      "symptoms": "abdominal pain, fatigue",
      "visit_date": "2025-07-22"
    },
    {
      "name": "Vijay Shetty",
      "age": 61,
      "symptoms": "back pain, muscle strain",
      "visit_date": "2025-07-20"
    },
    {
      "name": "Ayesha Khan",
      "age": 23,
      "symptoms": "fever, cough",
      "visit_date": "2025-07-18"
    },
    {
      "name": "Siddharth Roy",
      "age": 48,
      "symptoms": "chest pain, palpitations",
      "visit_date": "2025-07-15"
    },
    {
      "name": "Mira Bhardwaj",
      "age": 16,
      "symptoms": "rash, itching",
      "visit_date": "2025-07-12"
    },
    {
      "name": "Harish Vyas",
      "age": 68,
      "symptoms": "joint pain, swelling",
      "visit_date": "2025-07-10"
    },
    {
      "name": "Nandini Sen",
      "age": 35,
      "symptoms": "headache, nausea",
      "visit_date": "2025-07-08"
    },
    {
      "name": "Aditya Rathi",
      "age": 11,
      "symptoms": "cough, wheezing",
      "visit_date": "2025-07-05"
    },
    {
      "name": "Sunita Mistry",
      "age": 54,
      "symptoms": "abdominal pain, diarrhea",
      "visit_date": "2025-07-03"
    },
    {
      "name": "Kabir Ahuja",
      "age": 29,
      "symptoms": "vomiting, dehydration",
      "visit_date": "2025-07-01"
    },
    {
      "name": "Rekha Puri",
      "age": 46,
      "symptoms": "sore throat, fatigue",
      "visit_date": "2025-06-28"
    },
    {
      "name": "Gaurav Dutta",
      "age": 37,
      "symptoms": "back pain, stiffness",
      "visit_date": "2025-06-25"
    }
  ]
}
        if want == "history":
            return history
        else:
            raise ValueError("Value not found")

    def RFID_status(self,want):
        status = {
            "Status" : "offline"
        }
        if want == "Status":
            return status
        else:
            raise ValueError("Value not found")
    
    def console(self,want):
        temp={}
        
        if want == "create console":
            return temp
        else:
            raise ValueError("Value not found")

    def symptoms(self,want):
        temp={}
        
        if want == "symptoms":
            return temp
        else:
            raise ValueError("Value not found")


def createJSON(location_,combined_data):
    # Write the combined data to the file
    with open(location_, "w") as f:
        json.dump(combined_data, f, indent=4)
    return 0


class JSON:
    def __init__(self):
        self.data = data()

    def create_JSON(self, location, filename, code):
        try:
            # Ensure the directory exists
            os.makedirs(location, exist_ok=True)
            location_ = os.path.join(location, filename)

            # Combine history and generations into a single JSON object
            if code == "paitent profile":
                combined_data = {
                    "history": self.data.user_data("history")["history"],
                    "generation_tree": self.data.user_data("generations")["generation_tree"]
                }
                createJSON(location_,combined_data)

            elif code == "doctor profile":
                # Use the entire doctor_data dictionary or correct key
                combined_data = {
                    "doctor_name": self.data.doctor_data("history")["doctor_name"],
                    "patients_treated": self.data.doctor_data("history")["patients_treated"]
                }
                # Write the combined data to the file
                createJSON(location_,combined_data)
            
            elif code == "RFID status":
                createJSON(location_,self.data.RFID_status("Status"))

            elif code == "console":
                createJSON(location_,self.data.console("create console"))
            
            elif code == "Symptoms":
                createJSON(location_,self.data.console("symptoms"))
        
            else:
                raise ValueError("Invalid code provided. Use 'paitent profile' or 'doctor profile'.")

            return "file created"
        except KeyError as e:
            return f"KeyError: {str(e)} - Check the data structure in doctor_data or user_data."
        except OSError as e:
            return f"Error creating file: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"