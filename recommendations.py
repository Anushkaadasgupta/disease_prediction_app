"""
recommendations.py
-------------------
Rule-based wellness recommendation engine.

This module maps a predicted disease class to general, well-established
lifestyle guidance: diet, yoga/exercise, things to avoid, and a link to
help the user find real nearby care (via Google Maps search, not a
fabricated directory).

IMPORTANT: This intentionally contains NO medicine names, dosages, or
fabricated doctor/clinic contact details. Recommending specific drugs
requires a medical license and is out of scope. Real-time, real doctor
discovery is handled via a dynamic Google Maps search link instead of
hardcoded (and potentially fake/outdated) contact information.
"""

RECOMMENDATIONS = {
    "Diabetes": {
        "summary": "Markers suggest elevated diabetic risk. Diet and activity changes are the most effective first-line response.",
        "diet": {
            "eat_more": [
                "Leafy greens (spinach, fenugreek, kale)",
                "Whole grains (oats, brown rice, millets/jowar/ragi)",
                "Legumes & pulses (lentils, chickpeas, beans)",
                "Bitter gourd & fenugreek seeds — traditionally linked to glucose control",
                "Nuts in moderation (almonds, walnuts)",
                "Low-GI fruits (apples, pears, berries, guava)"
            ],
            "avoid": [
                "Refined sugar & sweets",
                "White rice & refined flour (maida)",
                "Sugary beverages & packaged juices",
                "Deep-fried snacks",
                "White bread & processed cereals"
            ],
            "pattern": "Smaller, more frequent meals (5-6/day) rather than large meals. Pair carbs with protein or fiber to slow glucose spikes."
        },
        "yoga": [
            {"name": "Dhanurasana (Bow Pose)", "benefit": "Stimulates pancreas function"},
            {"name": "Paschimottanasana (Seated Forward Bend)", "benefit": "Massages abdominal organs, aids digestion"},
            {"name": "Ardha Matsyendrasana (Half Spinal Twist)", "benefit": "Improves pancreatic circulation"},
            {"name": "Surya Namaskar (Sun Salutation)", "benefit": "Full-body metabolic activation"}
        ],
        "exercise": [
            "Brisk walking — 30 minutes daily, ideally after meals",
            "Swimming or cycling — 3-4x per week, low joint impact",
            "Resistance/strength training — 2x per week to improve insulin sensitivity"
        ],
        "lifestyle": [
            "Monitor blood sugar regularly with a glucometer",
            "Prioritize 7-8 hours of sleep — poor sleep worsens insulin resistance",
            "Stay hydrated; reduce sodium and processed food intake",
            "Manage stress — cortisol spikes raise blood sugar"
        ],
        "specialist": "Endocrinologist or Diabetologist",
        "search_query": "endocrinologist+near+me"
    },

    "Heart Disease": {
        "summary": "Markers suggest elevated cardiovascular risk. Blood pressure and cholesterol management are the priority areas.",
        "diet": {
            "eat_more": [
                "Oats & whole grains",
                "Fatty fish rich in Omega-3 (salmon, mackerel, sardines)",
                "Leafy greens & cruciferous vegetables (broccoli, spinach)",
                "Berries & citrus fruits",
                "Nuts & seeds (walnuts, flaxseed)",
                "Olive oil instead of saturated fats"
            ],
            "avoid": [
                "Trans fats & deep-fried food",
                "Excess salt & sodium-heavy processed food",
                "Red & processed meats",
                "Sugary drinks and desserts",
                "Full-fat dairy in excess"
            ],
            "pattern": "Follow a DASH-style or Mediterranean-style eating pattern — emphasizes vegetables, whole grains, and healthy fats while limiting sodium."
        },
        "yoga": [
            {"name": "Vajrasana (Thunderbolt Pose)", "benefit": "Aids digestion, gentle and safe for heart patients"},
            {"name": "Sukhasana with Pranayama (Easy Pose + Breathing)", "benefit": "Lowers resting heart rate and blood pressure"},
            {"name": "Setu Bandhasana (Bridge Pose)", "benefit": "Improves circulation, strengthens heart muscles gently"},
            {"name": "Anulom Vilom (Alternate Nostril Breathing)", "benefit": "Reduces stress and blood pressure"}
        ],
        "exercise": [
            "Brisk walking — 20-30 minutes daily, low intensity",
            "Light cycling on flat terrain",
            "Avoid sudden high-intensity exertion without medical clearance",
            "Stretching and mobility work to support circulation"
        ],
        "lifestyle": [
            "Quit smoking — single biggest modifiable risk factor",
            "Monitor blood pressure regularly at home",
            "Limit alcohol intake",
            "Manage stress through meditation or breathing exercises",
            "Maintain a healthy weight to reduce strain on the heart"
        ],
        "specialist": "Cardiologist",
        "search_query": "cardiologist+near+me"
    },

    "No Disease": {
        "summary": "Markers fall within a range associated with low risk. Maintaining current habits — and tightening a few — will help keep it that way.",
        "diet": {
            "eat_more": [
                "A varied diet with vegetables, fruits, whole grains, and lean protein",
                "Adequate hydration (2-3 liters of water daily)",
                "Healthy fats — nuts, seeds, olive oil"
            ],
            "avoid": [
                "Excess processed sugar and ultra-processed snacks",
                "Frequent fast food",
                "Excess alcohol"
            ],
            "pattern": "Balanced plate method: 1/2 vegetables, 1/4 protein, 1/4 whole grains at each meal."
        },
        "yoga": [
            {"name": "Surya Namaskar (Sun Salutation)", "benefit": "Full-body conditioning and flexibility"},
            {"name": "Tadasana (Mountain Pose)", "benefit": "Improves posture and body awareness"},
            {"name": "Bhujangasana (Cobra Pose)", "benefit": "Strengthens spine and opens chest"}
        ],
        "exercise": [
            "150 minutes of moderate cardio per week (WHO recommendation)",
            "Strength training 2x per week",
            "Stay active throughout the day — avoid prolonged sitting"
        ],
        "lifestyle": [
            "Routine annual health checkups even when feeling healthy",
            "Maintain consistent sleep schedule",
            "Manage stress proactively"
        ],
        "specialist": "General Physician (for routine checkups)",
        "search_query": "general+physician+near+me"
    }
}


def get_recommendations(disease: str) -> dict:
    """Return the recommendation bundle for a predicted disease class."""
    return RECOMMENDATIONS.get(disease, RECOMMENDATIONS["No Disease"])