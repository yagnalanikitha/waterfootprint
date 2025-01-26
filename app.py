from flask import Flask, render_template, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(24)  # Secret key for session management

# Water footprint data (initially empty or simplified for demonstration purposes)
water_footprints = {
    'fruits': {'tomato': 214 ,'apple': 822,
        'banana': 560,
        'orange': 560,
        'grapes': 560,
        'strawberry': 287,
        'watermelon': 370,
        'pineapple': 560,
        'peach': 560,
        'plum': 560,
        'mango': 560,
        'lemon': 560,
        'avocado': 1611,
        'blueberry': 1030,
        'papaya': 560,
        'cherries': 1460,
        'coconut': 2058,
        'fig': 560,
        'kiwi': 562,
        'pear': 720,
        'pomegranate': 1115,},  # Example: 1 kg of tomato
    'vegetables': {'amaranth_leaves': 300,
        'ash_gourd': 1200,
        'bitter_gourd': 600,
        'bottle_gourd': 1000,
        'brinjal': 570,
        'cabbage': 500,
        'carrot': 180,
        'cauliflower': 600,
        'chili': 390,
        'cluster_beans': 550,
        'coriander_leaves': 600,
        'drumstick': 800,
        'fenugreek': 340,
        'ginger': 1300,
        'green_beans': 900,
        'jackfruit': 900,
        'kale': 1000,
        'kohlrabi': 390,
        'lettuce': 235,
        'mango_ginger': 1500,
        'mint_leaves': 500,
        'mustard_greens': 660,
        'okra': 1000,
        'onion': 1130,
        'papaya': 800,
        'parsnip': 370,
        'peas': 900,
        'pumpkin': 500,
        'radish': 230,
        'ridge_gourd': 800,
        'spinach': 1500,
        'sweet_potato': 387,
        'tomato': 214,
        'taro': 1100,
        'turnip': 190,
        'water_chestnut': 700,
        'yam': 770,
        'arugula': 600,
        'beetroot': 326,
        'bok_choy': 550,
        'chayote': 800,
        'chili_pepper': 400,
        'chinese_broccoli': 1100,
        'colocasia': 1100,
        'cucumber': 300,
        'elephant_foot_yam': 1200,
        'fennel': 1000,
        'ginger_root': 1300,
        'green_pumpkin': 520,
        'horse_gram': 1300,
        'ice_plant': 1000,
        'kale_lacinato': 1200,
        'kundru': 900,
        'methi': 500,
        'mushroom': 1200,
        'oregano': 650,
        'pea_shoots': 400,
        'purslane': 250,
        'radicchio': 1200,
        'sage': 600,
        'sikandar': 450,
        'sorrel': 500,
        'spinach_red': 1500,
        'spring_onion': 600,
        'suran': 1100,
        'sweet_corn': 1400,
        'tamarind_leaves': 1000,
        'thymus': 650,
        'watercress': 250,
        'curry_leaves': 400,
        'drumstick_moringa': 800,
        'echium': 950,
        'lemon_balm': 750,
        'soursop': 900,
        'kachri': 500,
        'kolar': 600,
        'kundru_ivygourd': 520,
        'palak': 1500,
        'red_amaranth': 400,
        'sopari': 1000,
        'surajmukhi': 2000,
        'bamboo_shoots': 500,
        'chilies_bird_eye': 450,
        'fiddlehead_fern': 1000,
        'chili_pepper_indian': 400,
        'moringa_pod': 800,
        'cress': 250,
        'beet_greens': 500,
        'edamame': 2000,
        'tamarind_leaves': 1000,
        'aloe_vera': 800,
        'mango_leaf': 1500,
        'sweet_basil': 500,
        'guar': 600,
        'bitter_gourd_pavakka': 900,},  # Example: 1 kg of carrot
    'kharif': {'rice': 250,  # 1 kg of rice
        'maize': 300,
        'cotton': 1200,
        'soybean': 900,
        'groundnut': 1100,
        'pulses': 400,
        'sorghum': 700,
        'millets': 600,
        'jowar': 750,
        'bajra': 600,
        'moong': 700,
        'urad': 850,
        'pigeon_pea': 750,
        'black_gram': 900,
        'chana': 600,
        'sesame': 1000,
        'sunflower': 1300,
        'pearl_millet': 650,
        'green_gram': 750,
        'red_gram': 900,
        'castor': 1200,
        'gourd': 1200,
        'pumpkin': 500,
        'tobacco': 1500,
        'chili': 600,
        'cotton': 1500,
        'watermelon': 1200,
        'gourds': 800,
        'bottle_gourd': 1000,
        'okra': 1200,
        'cucumber': 900,
        'tomato': 214,
        'brinjal': 570,
        'carrot': 180,
        'green_beans': 800,
        'bitter_gourd': 600,
        'cabbage': 500,
        'cauliflower': 600,
        'lemon': 900,
        'green_chili': 450,
        'pumpkin': 500,
        'potato': 900,
        'sweet_potato': 387,
        'groundnut': 1100,
        'ginger': 1300,
        'tamarind': 1200,
        'peanuts': 1000,
        'tomato': 200,
        'onion': 1130,
        'garlic': 800,
        'okra': 1000,
        'peas': 900,
        'moong_bean': 1000,
        'watermelon': 1300,
        'onion': 1100,
        'mustard': 800,
        'sugarcane': 2500,
        'jute': 700},  # Example: 1 kg of rice
    'rabi': {'wheat': 250, 
        'barley': 450,
        'mustard': 800,
        'chickpea': 600,
        'pea': 900,
        'lentil': 800,
        'oats': 450,
        'fenugreek': 600,
        'sesame': 1000,
        'pulses': 400,
        'coriander': 1200,
        'garlic': 800,
        'onion': 1130,
        'carrot': 180,
        'spinach': 550,
        'cabbage': 500,
        'cauliflower': 600,
        'broccoli': 700,
        'tomato': 214,
        'turnip': 550,
        'beetroot': 500,
        'sweet_potato': 387,
        'peas': 900,
        'fennel': 1200,
        'chili': 600,
        'green_gram': 750,
        'black_gram': 850,
        'green_chili': 450,
        'groundnut': 1100,
        'mustard_seed': 1000,
        'carrot': 180,
        'brinjal': 570,
        'potato': 900,
        'pomegranate': 500,
        'apple': 1500,
        'guava': 1200,
        'date': 2500,
        'banana': 1500,
        'papaya': 1300,
        'tobacco': 1500,
        'cotton': 1200,
        'sunflower': 1300,
        'watermelon': 1200,
        'melon': 1300,
        'bottle_gourd': 1000,
        'bitter_gourd': 600,
        'pumpkin': 500,
        'gourd': 1200,
        'ginger': 1300,
        'tamarind': 1200,
        'turmeric': 1400,
        'cucumber': 900,
        'ginger': 1300,
        'lemon': 900,
        'sorghum': 700,
        'jowar': 750,
        'ragi': 850,
        'bajra': 600,
        'maize': 300,
        'mango': 2000,
        'cashew': 1500,
        'pistachio': 3000,
        'peach': 1300,
        'plum': 1500,
        'apricot': 1300,
        'apples': 1500,
        'grapes': 1300,
        'cherry': 1500,
        'fig': 1300,
        'dates': 2500,
        'banana': 1500,
        'papaya': 1300,
        'berries': 900,
        'strawberry': 1100,
        'avocado': 1500,
        'blueberry': 2000,
        'cabbage': 500,
        'methi': 1200,
        'okra': 1000,
        'chickpeas': 600,
        'fenugreek': 700,
        'fennel': 900,
        'spinach': 700,
        'radish': 300,
        'onion': 1130,
        'green_gram': 750,
        'black_gram': 850,  # Example: 1 kg of wheat
}}

# Translation dictionary (same as before)
translations = {
    'en': {
        'home': 'Home',
        'water_footprint_calculator': 'Water Footprint Calculator',
        'category': 'Category',
        'product': 'Product',
        'quantity': 'Quantity (kg)',
        'calculate': 'Calculate',
        'add_water_footprint_data': 'Add Water Footprint Data',
        'invalid_input': 'Invalid input',
        'go_back': 'Go Back to Home',
        'added_successfully': 'added successfully!',
        'choose_language': 'Choose Language',
        'water_footprint_chart': 'Water Footprint Chart',
        'result': 'Result',
    },
    'hi': {
        'home': 'मुख्य पृष्ठ',
        'water_footprint_calculator': 'जल पदचिह्न गणना',
        'category': 'श्रेणी',
        'product': 'उत्पाद',
        'quantity': 'मात्रा (किग्रा)',
        'calculate': 'गणना करें',
        'add_water_footprint_data': 'जल पदचिह्न डेटा जोड़ें',
        'invalid_input': 'अमान्य इनपुट',
        'go_back': 'मुख्य पृष्ठ पर वापस जाएं',
        'added_successfully': 'सफलतापूर्वक जोड़ा गया!',
        'choose_language': 'भाषा चुनें',
        'water_footprint_chart': 'जल पदचिह्न चार्ट',
        'result': 'परिणाम',
    },
    'bn': {
        'home': 'হোম',
        'water_footprint_calculator': 'পানি পদচিহ্ন ক্যালকুলেটর',
        'category': 'ক্যাটেগরি',
        'product': 'পণ্য',
        'quantity': 'পরিমাণ (কেজি)',
        'calculate': 'গণনা করুন',
        'add_water_footprint_data': 'পানি পদচিহ্ন তথ্য যোগ করুন',
        'invalid_input': 'অবৈধ ইনপুট',
        'go_back': 'হোম পৃষ্ঠায় ফিরে যান',
        'added_successfully': 'সফলভাবে যোগ করা হয়েছে!',
        'choose_language': 'ভাষা নির্বাচন করুন',
        'water_footprint_chart': 'পানি পদচিহ্ন চার্ট',
        'result': 'ফলাফল',
    },
}

# Set default language to English
@app.before_request
def set_language():
    lang = request.args.get('lang', None)  # Get language from query parameter
    if lang and lang in translations:
        session['lang'] = lang
    elif 'lang' not in session:
        session['lang'] = 'en'  # Default language is English

@app.route('/')
def index():
    lang = session.get('lang', 'en')  # Get language from session
    return render_template('index.html', translations=translations[lang], water_footprints=water_footprints)

@app.route('/switch_language/<lang>')
def switch_language(lang):
    if lang in translations:
        session['lang'] = lang
    return redirect(request.referrer) 

@app.route('/voice_recognition', methods=['GET'])
def voice_recognition():
    lang = session.get('lang', 'en')
    return render_template('voice_recognition.html', translations=translations[lang])

@app.route('/process_voice_input', methods=['POST'])
def process_voice_input():
    lang = session.get('lang', 'en')
    voice_input = request.form.get('voice_input').lower().strip()

    # Example of extracting category and product from voice input
    # Assuming format "category product"
    parts = voice_input.split()
    category = parts[0]  # Category is the first word
    product = parts[1] if len(parts) > 1 else ""

    # Check if category and product are valid
    if category in water_footprints and product in water_footprints[category]:
        water_per_kg = water_footprints[category][product]
        total_water = water_per_kg * 1  # Assuming 1 kg
        return render_template('result.html', total_water=total_water, product=product, quantity=1, translations=translations[lang])

    return render_template('error.html', message=translations[lang]['invalid_input'], translations=translations[lang])

@app.route('/add_water_footprint', methods=['GET', 'POST'])
def add_water_footprint():
    lang = session.get('lang', 'en')
    
    if request.method == 'POST':
        # Get the data from the form
        category = request.form.get('category').lower()
        product = request.form.get('product').lower()
        water_per_kg = request.form.get('water_per_kg')

        # Validate the input
        if category and product and water_per_kg:
            try:
                water_per_kg = float(water_per_kg)  # Convert to float
                if category not in water_footprints:
                    water_footprints[category] = {}  # If category doesn't exist, add it
                water_footprints[category][product] = water_per_kg
                return render_template('success.html', message=translations[lang]['added_successfully'], translations=translations[lang])

            except ValueError:
                return render_template('error.html', message=translations[lang]['invalid_input'], translations=translations[lang])

    return render_template('add_water_footprint.html', translations=translations[lang])

if __name__ == '__main__':
    app.run(debug=True)

