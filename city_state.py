import random as rd

states_to_cities = {
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur"],
    "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat"],
    "Assam": ["Guwahati", "Dibrugarh", "Silchar"],"Bihar": ["Patna", "Gaya", "Bhagalpur"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur"],
    "Goa": ["Panaji", "Margao", "Vasco da Gama"],"Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Haryana": ["Gurugram", "Faridabad", "Panipat"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],"Karnataka": ["Bengaluru", "Mysuru", "Mangaluru"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Manipur": ["Imphal", "Churachandpur", "Bishnupur"],"Meghalaya": ["Shillong", "Tura", "Jowai"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai"],"Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
    "Punjab": ["Chandigarh", "Amritsar", "Ludhiana"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
    "Sikkim": ["Gangtok", "Pelling", "Namchi"],"Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Tripura": ["Agartala", "Dharmanagar", "Kailasahar"],"Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
    "Uttarakhand": ["Dehradun", "Nainital", "Haridwar"],
    "West Bengal": ["Kolkata", "Darjeeling", "Siliguri"]
}

def city(state):
    lis = states_to_cities[state]
    return rd.choice(lis)

def state():
    states = [i for i in states_to_cities]
    return rd.choice(states)