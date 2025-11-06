import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime, timedelta, date, time
from io import BytesIO
import random
import hashlib
import pandas as pd

# Zodiac sign calculation ♈
def get_zodiac_sign(birth_date):
    month = birth_date.month
    day = birth_date.day
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries ♈'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus ♉'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini ♊'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer ♋'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo ♌'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo ♍'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra ♎'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio ♏'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius ♐'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricorn ♑'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius ♒'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces ♓'

# Zodiac element calculation 🌟
def get_zodiac_element(birth_date):
    month = birth_date.month
    day = birth_date.day
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Fire'  # Aries 🔥
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Earth'  # Taurus 🌍
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Air'  # Gemini 💨
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Water'  # Cancer 🌊
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Fire'  # Leo 🔥
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Earth'  # Virgo 🌍
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Air'  # Libra 💨
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Water'  # Scorpio 🌊
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Fire'  # Sagittarius 🔥
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Earth'  # Capricorn 🌍
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Air'  # Aquarius 💨
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Water'  # Pisces 🌊

# Element colors 🎨
element_colors = {
    'Fire': 'red',
    'Earth': 'green',
    'Air': 'yellow',
    'Water': 'blue'
}

# Astrology compatibility ♑❤️
zodiac_compatibility = {
    'Aries ♈': ['Leo ♌', 'Sagittarius ♐', 'Gemini ♊', 'Aquarius ♒'],
    'Taurus ♉': ['Virgo ♍', 'Capricorn ♑', 'Cancer ♋', 'Pisces ♓'],
    'Gemini ♊': ['Libra ♎', 'Aquarius ♒', 'Aries ♈', 'Leo ♌'],
    'Cancer ♋': ['Scorpio ♏', 'Pisces ♓', 'Taurus ♉', 'Virgo ♍'],
    'Leo ♌': ['Aries ♈', 'Sagittarius ♐', 'Gemini ♊', 'Libra ♎'],
    'Virgo ♍': ['Taurus ♉', 'Capricorn ♑', 'Cancer ♋', 'Scorpio ♏'],
    'Libra ♎': ['Gemini ♊', 'Aquarius ♒', 'Leo ♌', 'Sagittarius ♐'],
    'Scorpio ♏': ['Cancer ♋', 'Pisces ♓', 'Virgo ♍', 'Capricorn ♑'],
    'Sagittarius ♐': ['Aries ♈', 'Leo ♌', 'Libra ♎', 'Aquarius ♒'],
    'Capricorn ♑': ['Taurus ♉', 'Virgo ♍', 'Scorpio ♏', 'Pisces ♓'],
    'Aquarius ♒': ['Gemini ♊', 'Libra ♎', 'Aries ♈', 'Sagittarius ♐'],
    'Pisces ♓': ['Cancer ♋', 'Scorpio ♏', 'Taurus ♉', 'Capricorn ♑']
}

# Rune mappings (letter to rune name) ᚱ
runes_map = {
    'a': 'Ansuz',
    'b': 'Berkana',
    'c': 'Kaunaz',
    'd': 'Dagaz',
    'e': 'Eihwaz',
    'f': 'Fehu',
    'g': 'Gebo',
    'h': 'Hagalaz',
    'i': 'Isa',
    'j': 'Jera',
    'k': 'Kaunaz',
    'l': 'Laguz',
    'm': 'Mannaz',
    'n': 'Nauthiz',
    'o': 'Othala',
    'p': 'Pertho',
    'q': 'Kaunaz',  # approximate
    'r': 'Raido',
    's': 'Sowulo',
    't': 'Teiwaz',
    'u': 'Uruz',
    'v': 'Wunjo',  # approximate
    'w': 'Wunjo',
    'x': 'Eihwaz',  # approximate
    'y': 'Jera',
    'z': 'Algiz',
    'þ': 'Thurisaz'  # for th, but we'll handle in code if needed
}

# Rune meanings 📜
rune_meanings = {
    'Fehu': 'Cattle, prosperity, gain of some sort, fulfilment 💰',
    'Uruz': 'Wild ox, strength, life force, determination 💪',
    'Thurisaz': 'Giants, Thor, brutal force, unexpected change ⚡',
    'Ansuz': 'Mouth, Odin, communication, transmission of knowledge 🗣️',
    'Raido': 'Wagon, travel, movement, introspective journey 🚀',
    'Kaunaz': 'Fire, warmth, energy, power, positive attitude 🔥',
    'Gebo': 'Gift, fortuitous outcome, partnership, commitment 🎁',
    'Wunjo': 'Joy, success, lasting emotional happiness 😊',
    'Hagalaz': 'Hail, limitations, delays, forces outside your control ❄️',
    'Nauthiz': 'Patience, passing through a difficult learning situation, hardship, need ⏳',
    'Isa': 'Ice, plans on hold, frustrations 🧊',
    'Jera': 'Harvest, reaping of rewards for past efforts, justice 🌾',
    'Eihwaz': 'Yew, Yggdrassil, endurance, ability to achieve goals with resilience 🌳',
    'Pertho': 'Mystery, occult knowledge, randomness, coincidence, secrets uncovered 🔮',
    'Algiz': 'Elk, protection, support, wisdom of the Universe 🛡️',
    'Sowulo': 'Sun, victory, awareness, energy ☀️',
    'Teiwaz': 'Tyr, success in a competition, warrior strength ⚔️',
    'Berkana': 'Birth, new beginnings, fertility, true home 🌱',
    'Ehwaz': 'Horse, movement, steady progress, physical shift 🐎',
    'Mannaz': 'Humankind, interdependence, collective potential 👥',
    'Laguz': 'Water, evolution, cleansing, female figure 💧',
    'Ingwaz': 'Successful conclusion, relief, personal development 🏆',
    'Othala': 'Heritage, possessions, ancestral wisdom, home 🏡',
    'Dagaz': 'Day, increase, steady growth, awakening 🌅'
}

# Rune elements 🌟
rune_elements = {
    'Fehu': 'Fire 🔥',
    'Uruz': 'Earth 🌍',
    'Thurisaz': 'Fire 🔥',
    'Ansuz': 'Air 💨',
    'Raido': 'Air 💨',
    'Kaunaz': 'Fire 🔥',
    'Gebo': 'Air 💨',
    'Wunjo': 'Air 💨',
    'Hagalaz': 'Water 🌊',
    'Nauthiz': 'Fire 🔥',
    'Isa': 'Water 🌊',
    'Jera': 'Earth 🌍',
    'Eihwaz': 'Earth 🌍',
    'Pertho': 'Water 🌊',
    'Algiz': 'Air 💨',
    'Sowulo': 'Fire 🔥',
    'Teiwaz': 'Air 💨',
    'Berkana': 'Earth 🌍',
    'Ehwaz': 'Earth 🌍',
    'Mannaz': 'Air 💨',
    'Laguz': 'Water 🌊',
    'Ingwaz': 'Earth 🌍',
    'Othala': 'Earth 🌍',
    'Dagaz': 'Air 💨'
}

# Rune Unicode symbols ᚱ
rune_unicode = {
    'Fehu': 'ᚠ',
    'Uruz': 'ᚢ',
    'Thurisaz': 'ᚦ',
    'Ansuz': 'ᚨ',
    'Raido': 'ᚱ',
    'Kaunaz': 'ᚲ',
    'Gebo': 'ᚷ',
    'Wunjo': 'ᚹ',
    'Hagalaz': 'ᚺ',
    'Nauthiz': 'ᚾ',
    'Isa': 'ᛁ',
    'Jera': 'ᛃ',
    'Eihwaz': 'ᛇ',
    'Pertho': 'ᛈ',
    'Algiz': 'ᛉ',
    'Sowulo': 'ᛊ',
    'Teiwaz': 'ᛏ',
    'Berkana': 'ᛒ',
    'Ehwaz': 'ᛖ',
    'Mannaz': 'ᛗ',
    'Laguz': 'ᛚ',
    'Ingwaz': 'ᛜ',
    'Othala': 'ᛟ',
    'Dagaz': 'ᛞ'
}

# Rune colors 🌈
rune_colors = {
    'Fehu': 'gold',
    'Uruz': 'brown',
    'Thurisaz': 'darkred',
    'Ansuz': 'purple',
    'Raido': 'orange',
    'Kaunaz': 'red',
    'Gebo': 'pink',
    'Wunjo': 'yellow',
    'Hagalaz': 'white',
    'Nauthiz': 'gray',
    'Isa': 'lightblue',
    'Jera': 'green',
    'Eihwaz': 'darkgreen',
    'Pertho': 'magenta',
    'Algiz': 'lightgreen',
    'Sowulo': 'yellow',
    'Teiwaz': 'blue',
    'Berkana': 'lightpink',
    'Ehwaz': 'brown',
    'Mannaz': 'indigo',
    'Laguz': 'blue',
    'Ingwaz': 'lime',
    'Othala': 'brown',
    'Dagaz': 'yellow'
}

# Moon phase calculation 🌙
def get_moon_phase(birth_datetime):
    year = birth_datetime.year
    month = birth_datetime.month
    day = birth_datetime.day
    if month < 3:
        year -= 1
        month += 12
    a = year // 100
    b = a // 4
    c = 2 - a + b
    e = int(365.25 * (year + 4716))
    f = int(30.6001 * (month + 1))
    jd = c + day + e + f - 1524.5
    days_since_new = jd - 2451549.5
    new_moons = days_since_new / 29.530587881447267
    fractional = new_moons - int(new_moons)
    phase_index = int(fractional * 8)
    phases = ["New Moon 🌑", "Waxing Crescent 🌒", "First Quarter 🌓", "Waxing Gibbous 🌔",
              "Full Moon 🌕", "Waning Gibbous 🌖", "Last Quarter 🌗", "Waning Crescent 🌘"]
    return phases[phase_index % 8]

# Moon phase effects explanations 🔮🌙
moon_effects = {
    "New Moon 🌑": "Time for new beginnings and setting intentions! Plant those cosmic seeds and watch your dreams sprout like magical beans. 🌱✨ But beware, energy might be low – perfect for Netflix and chill with the universe. 📺🌌",
    "Waxing Crescent 🌒": "Building momentum! Your ideas are gaining traction like a snowball rolling downhill. Focus on growth and positive vibes – it's like the moon's giving you a thumbs up! 👍💪",
    "First Quarter 🌓": "Action time! Overcome obstacles and make decisions. The moon's half-lit, reminding you that balance is key – don't forget to hydrate your aura! 💧⚖️",
    "Waxing Gibbous 🌔": "Refinement phase! Polish your plans like a shiny crystal. Energy is high, but watch for perfectionism – remember, even the moon has craters! 🕳️🔮",
    "Full Moon 🌕": "Peak energy and illumination! Emotions run high, revelations abound. Great for manifestations, but if you're a werewolf, maybe stay indoors. 🐺🌕😂",
    "Waning Gibbous 🌖": "Gratitude and sharing! Reflect on achievements and spread the love. It's like the moon's saying 'Thanks for the memories!' 📸❤️",
    "Last Quarter 🌗": "Release and forgiveness! Let go of what no longer serves you. Think of it as cosmic decluttering – Marie Kondo your soul! 🧹✨",
    "Waning Crescent 🌘": "Rest and surrender! Prepare for the new cycle. Hibernate like a bear in winter, dreaming of future adventures. 🐻💤"
}

# Crystals for elements 💎
crystals_by_element = {
    'Fire': ['Carnelian 🔥', 'Red Jasper ❤️', 'Sunstone ☀️'],
    'Earth': ['Moss Agate 🌿', 'Jade 💚', 'Hematite ⚫'],
    'Air': ['Sodalite 🔵', 'Blue Lace Agate 🌀', 'Aquamarine 🌊'],
    'Water': ['Moonstone 🌙', 'Pearl 🤍', 'Aquamarine 🌊']
}

# Crystals for moon phases 💎🌙
crystals_by_moon = {
    "New Moon 🌑": ['Moonstone 🌙', 'Selenite 🤍', 'Pink Opal 💖'],
    "Waxing Crescent 🌒": ['Clear Quartz ⚪', 'Citrine 💛', 'Green Aventurine 💚'],
    "First Quarter 🌓": ['Amethyst 💜', 'Labradorite 🌈', 'Moonstone 🌙'],
    "Waxing Gibbous 🌔": ['Sodalite 🔵', 'Citrine 💛', 'Amethyst 💜'],
    "Full Moon 🌕": ['Amethyst 💜', 'Moonstone 🌙', 'Labradorite 🌈'],
    "Waning Gibbous 🌖": ['Black Tourmaline ⚫', 'Smoky Quartz 🖤', 'Hematite ⚫'],
    "Last Quarter 🌗": ['Clear Quartz ⚪', 'Selenite 🤍', 'Moonstone 🌙'],
    "Waning Crescent 🌘": ['Black Obsidian ⚫', 'Labradorite 🌈', 'Amethyst 💜']
}

# Tarot Major Arcana 🃏
tarot_cards = [
    {"name": "The Fool 🃏", "meaning": "New beginnings, innocence, spontaneity – leap into the unknown like a cosmic adventurer! 🚀😄"},
    {"name": "The Magician ✨", "meaning": "Manifestation, resourcefulness, power – you've got the tools, now make some magic happen! 🪄🔥"},
    {"name": "The High Priestess 🔮", "meaning": "Intuition, mystery, inner knowledge – trust your gut, it's probably right (and full of wisdom)! 🤫💡"},
    {"name": "The Empress 👑", "meaning": "Nurturing, abundance, creativity – mother nature's hug in card form! 🌸🤗"},
    {"name": "The Emperor 🏰", "meaning": "Structure, authority, stability – time to build your empire, one brick at a time! 🧱💪"},
    {"name": "The Hierophant 📜", "meaning": "Tradition, spiritual wisdom, conformity – follow the rules, or at least pretend to! 😉🙏"},
    {"name": "The Lovers 💕", "meaning": "Relationships, choices, harmony – love is in the air, but so are decisions! ❤️🤔"},
    {"name": "The Chariot 🛡️", "meaning": "Victory, determination, control – full speed ahead, but watch for potholes! 🏎️🏆"},
    {"name": "Strength 🦁", "meaning": "Courage, patience, inner strength – tame that inner lion with kindness! 🐱‍👤💖"},
    {"name": "The Hermit 🏮", "meaning": "Introspection, guidance, solitude – time for a solo quest in your blanket fort! 🛋️🔍"},
    {"name": "Wheel of Fortune 🎡", "meaning": "Cycles, fate, change – life's a carnival ride, hold on tight! 🎢🍀"},
    {"name": "Justice ⚖️", "meaning": "Fairness, truth, balance – karma's courtroom is in session! 👩‍⚖️📊"},
    {"name": "The Hanged Man 🙃", "meaning": "Surrender, new perspective, suspension – hang loose and see things upside down! 🔄😎"},
    {"name": "Death 💀", "meaning": "Transformation, endings, new beginnings – out with the old, in with the fabulous! 🦋🔄"},
    {"name": "Temperance 😇", "meaning": "Balance, moderation, harmony – mix it up, but don't overdo it! 🍹⚖️"},
    {"name": "The Devil 😈", "meaning": "Bondage, materialism, shadow self – break those chains, party pooper! ⛓️💥"},
    {"name": "The Tower 🏰💥", "meaning": "Sudden change, upheaval, revelation – when life gives you lightning, rebuild better! ⚡🏗️"},
    {"name": "The Star ⭐", "meaning": "Hope, inspiration, serenity – wish upon yourself, you're the star! 🌟💫"},
    {"name": "The Moon 🌙", "meaning": "Illusion, intuition, subconscious – things aren't always what they seem in moonlight! 🐺🕵️‍♀️"},
    {"name": "The Sun ☀️", "meaning": "Joy, success, positivity – sunshine and rainbows ahead! 🌈😊"},
    {"name": "Judgement 📯", "meaning": "Rebirth, inner calling, absolution – wake-up call from the universe! ☎️🌟"},
    {"name": "The World 🌍", "meaning": "Completion, integration, accomplishment – you've won the game of life... for now! 🏆🎉"}
]

# Function to create gradient image 🎨
def create_gradient(colors, width=400, height=200):
    if len(colors) < 2:
        colors = colors * 2  # Need at least two for gradient
    cmap = mcolors.LinearSegmentedColormap.from_list("aura_gradient", colors)
    gradient = np.linspace(0, 1, 256)
    gradient = np.tile(gradient, (height, 1))
    fig, ax = plt.subplots(figsize=(width/100, height/100))
    ax.imshow(gradient, aspect='auto', cmap=cmap, extent=[0, width, 0, height])
    ax.axis('off')
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', pad_inches=0, transparent=True)
    buf.seek(0)
    plt.close(fig)
    return buf

# Numerology functions 🔢
def reduce_number(num):
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_life_path(birth_date):
    month = reduce_number(birth_date.month)
    day = reduce_number(birth_date.day)
    year = reduce_number(birth_date.year)
    total = reduce_number(month + day + year)
    return total

def get_letter_value(letter):
    if not letter.isalpha():
        return 0
    val = ord(letter.lower()) - ord('a') + 1
    return val % 9 or 9  # Pythagorean: 1-9 cycle

def calculate_destiny_number(name):
    total = sum(get_letter_value(c) for c in name)
    return reduce_number(total)

def calculate_soul_urge(name):
    vowels = 'aeiou'
    total = sum(get_letter_value(c) for c in name.lower() if c in vowels)
    return reduce_number(total)

def calculate_personality_number(name):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    total = sum(get_letter_value(c) for c in name.lower() if c in consonants)
    return reduce_number(total)

# Expanded numerology meanings 🔢✨
numerology_meanings = {
    1: "The number 1 represents leadership, independence, and originality. You are a natural trailblazer, full of initiative and drive to achieve your goals. With a pioneering spirit, you thrive on new beginnings and are not afraid to stand alone. However, watch for tendencies toward selfishness or stubbornness. Embrace your inner innovator and lead with confidence! 🚀💪",
    2: "The number 2 symbolizes cooperation, sensitivity, and balance. You are the ultimate peacemaker, excelling in partnerships and diplomacy. Your empathetic nature makes you a great listener and mediator. Challenges may include indecisiveness or over-sensitivity. Focus on harmony in relationships and trust your intuition to guide you. ⚖️❤️",
    3: "The number 3 embodies creativity, self-expression, and joy. You are sociable, optimistic, and love to entertain others with your wit and charm. Artistic talents abound, making you a natural performer or communicator. Guard against scattering your energies or superficiality. Channel your vibrant energy into creative pursuits for fulfillment. 🎉😄",
    4: "The number 4 stands for stability, practicality, and hard work. You are reliable, disciplined, and excel at building strong foundations. Your methodical approach ensures long-term success in endeavors. Potential pitfalls include rigidity or overwork. Prioritize organization and perseverance to achieve your ambitions. 🏗️💼",
    5: "The number 5 signifies freedom, adventure, and versatility. You crave excitement and change, thriving in dynamic environments. Adaptable and resourceful, you love travel and new experiences. Beware of restlessness or irresponsibility. Embrace variety while maintaining balance in your life. 🌍🗺️",
    6: "The number 6 represents responsibility, nurturing, and harmony. You are compassionate, family-oriented, and often take on caretaker roles. Your sense of justice and love for beauty make you a harmonious influence. Avoid being overly controlling or self-sacrificing. Focus on creating loving environments for yourself and others. 🏡🤗",
    7: "The number 7 symbolizes introspection, spirituality, and analysis. You are a deep thinker, seeking truth and inner wisdom. Intuitive and philosophical, you excel in research and contemplation. Challenges may include isolation or skepticism. Trust your inner voice and pursue knowledge for personal growth. 🔍🧘‍♂️",
    8: "The number 8 denotes ambition, power, and material success. You are goal-oriented, efficient, and have strong leadership skills in business. Your resilience helps you overcome obstacles. Watch for materialism or authoritarianism. Use your organizational talents to achieve abundance and share it wisely. 💰🏆",
    9: "The number 9 embodies compassion, humanitarianism, and completion. You are idealistic, generous, and dedicated to helping others. Creative and wise, you see the bigger picture. Potential issues include resentment or unfinished business. Embrace universal love and use your talents for global good. 🌎💖",
    11: "The master number 11 represents intuition, inspiration, and enlightenment. You are highly sensitive, visionary, and spiritually aware. Your insights can inspire others profoundly. Challenges include nervousness or impracticality. Harness your heightened awareness for healing and guidance. 🌟🔮",
    22: "The master number 22 signifies master building, practicality, and large endeavors. You have the potential to turn dreams into reality on a grand scale. Ambitious and disciplined, you excel in architecture or leadership. Avoid self-doubt or overwork. Use your power to create lasting positive impact. 🏛️🛠️",
    33: "The master number 33 symbolizes master teaching, compassion, and healing. You are altruistic, nurturing, and dedicated to uplifting humanity. Your wisdom and love inspire others. Potential pitfalls include martyrdom or emotional overload. Focus on selfless service and spiritual growth. 📚🙏"
}

# App ✨
st.title("Aura Alchemy Simulator ✨🔮🌟")

st.write("Enter your details to simulate your aura transformation! 🌈💫")

name = st.text_input("Your Name 📛", value="Mahaan")
birth_date = st.date_input("Birth Date 📅", min_value=date(1900, 1, 1), max_value=date(2100, 12, 31), value=date(1993, 7, 12))
birth_time = st.time_input("Birth Time ⏰", value=time(12, 26), step=3600)
latitude = st.number_input("Birth Latitude (positive for North, negative for South) 🌍", -90.0, 90.0, 13.32)
longitude = st.number_input("Birth Longitude (positive for East, negative for West) 🗺️", -180.0, 180.0, 75.77)

if st.button("Simulate 🔮"):
    if name and birth_date:
        birth_datetime = datetime.combine(birth_date, birth_time)
        
        # Compute zodiac sign and element 🌟
        zodiac_sign = get_zodiac_sign(birth_date)
        element = get_zodiac_element(birth_date)
        base_color = element_colors.get(element, 'gray')
        
        # Transmute name to runes ᚱ
        runes = [runes_map.get(letter.lower(), 'Ansuz') for letter in name if letter.isalpha()]  # Default to Ansuz if missing
        
        # Get rune colors 🌈
        mix_colors = [rune_colors.get(rune, 'black') for rune in runes]
        
        # All colors for gradient: base + mixes 🎨
        all_colors = [base_color] + mix_colors
        
        # Display aura 🌀
        st.subheader("Your Aura Visualization 🌈✨")
        gradient_img = create_gradient(all_colors)
        st.image(gradient_img, caption="Your alchemical aura gradient 🔮")
        
        # Rune elemental associations explanation 🌟ᚱ
        st.subheader("Rune Elemental Associations Explained 🌟ᚱ🔍")
        st.write("Each rune is associated with one of the four elements (Fire, Earth, Air, Water), influencing its energy and symbolism. These associations enhance the alchemical transformation of your aura by blending elemental forces with rune magic. Below is the full table of rune elemental associations: 📜💫")
        elemental_data = {'Rune ᚱ': list(rune_elements.keys()), 'Element 🌟': list(rune_elements.values())}
        elemental_df = pd.DataFrame(elemental_data)
        st.table(elemental_df)
        
        # Your runes and meanings 📜ᚱ
        st.subheader("Your Runes and Meanings ᚱ📜✨")
        if runes:
            unique_runes = list(set(runes))  # Unique runes for cleaner display
            st.write("Based on your name, here are the transmuted runes, their symbols, elements, and mystical meanings: 🔮")
            for rune in unique_runes:
                symbol = rune_unicode.get(rune, '?')
                elem = rune_elements.get(rune, 'Unknown 🌌')
                meaning = rune_meanings.get(rune, "Ancient mystery unfolds... 🔮")
                st.write(f"**{rune} {symbol} ({elem})**: {meaning} 📜💫")
        else:
            st.write("Enter a name to reveal your runes and their meanings! 📛ᚱ")
        
        # Moon phase 🌙
        st.subheader("Moon Phase at Birth 🌕")
        moon_phase = get_moon_phase(birth_datetime)
        st.write(f"Your birth moon phase: {moon_phase} 🌙")
        st.write("Effects: " + moon_effects.get(moon_phase, "Mysterious lunar influences at play! 🌌"))
        
        # Crystal Healing 💎
        st.subheader("Crystal Healing Recommendations 💎🌟")
        element_crystals = crystals_by_element.get(element, [])
        moon_crystals = crystals_by_moon.get(moon_phase, [])
        recommended_crystals = list(set(element_crystals + moon_crystals))  # Unique
        if recommended_crystals:
            st.write("Based on your element and moon phase, try these crystals: ")
            for crystal in random.sample(recommended_crystals, min(3, len(recommended_crystals))):
                st.write(f"- {crystal} 💎")
        else:
            st.write("No specific crystals recommended. Explore Moonstone for general lunar energy! 🌙💎")
        
        # Astrology Compatibility ♑❤️
        st.subheader("Astrology Compatibility ♑❤️✨")
        compat_signs = zodiac_compatibility.get(zodiac_sign, [])
        st.write(f"Your zodiac sign: {zodiac_sign} ({element} element) 🌟")
        if compat_signs:
            st.write("Compatible signs (best matches for love, friendship, or partnerships): ❤️")
            for sign in compat_signs:
                st.write(f"- {sign}")
        else:
            st.write("Mysterious cosmic alignments – explore more! 🔮")
        
        # Numerology Calculator 🔢
        st.subheader("Numerology Calculator 🔢✨")
        life_path = calculate_life_path(birth_date)
        destiny = calculate_destiny_number(name)
        soul_urge = calculate_soul_urge(name)
        personality = calculate_personality_number(name)
        st.write(f"**Life Path Number**: {life_path} – {numerology_meanings.get(life_path, 'Mystical path ahead! 🔮')} 🔢💫")
        st.write(f"**Destiny Number**: {destiny} – {numerology_meanings.get(destiny, 'Destiny unfolds mysteriously! 🌟')} 🔢❤️")
        st.write(f"**Soul Urge Number**: {soul_urge} – {numerology_meanings.get(soul_urge, 'Inner desires revealed! 💖')} 🔢🧘‍♀️")
        st.write(f"**Personality Number**: {personality} – {numerology_meanings.get(personality, 'Outer self shines! 😊')} 🔢🌈")
        
        # Tarot Card Reading 🃏
        st.subheader("Tarot Card Reading 🃏✨")
        # Seed random with birth info for reproducibility
        seed_str = f"{name}{birth_datetime}"
        seed_hash = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
        random.seed(seed_hash)
        draw = random.sample(tarot_cards, 3)
        st.write("Your three-card spread: Past, Present, Future 🔮")
        for i, card in enumerate(draw):
            position = ["Past", "Present", "Future"][i]
            st.write(f"**{position}: {card['name']}** - {card['meaning']} 🃏")
        
        # Enhanced Potion Recipes 🧪
        st.subheader("Humorous Potion Recipes 🧪😂✨")
        if runes:
            aspects = ["love life ❤️", "career success 💼", "health and vitality 🏃‍♂️", "spiritual growth 🧘‍♀️", "wealth and prosperity 💰", "adventure seeking 🗺️", "creativity boost 🎨", "luck enhancement 🍀", "stress relief 😌", "friendship magnet 👯‍♀️"]
            attractions = ['unicorns 🦄', 'good fortune 🍀', 'positive vibes 😎', 'magical opportunities ✨', 'endless energy ⚡', 'hidden treasures 🗝️', 'cosmic high-fives ✋', 'rainbow farting puppies 🌈🐶', 'winning lottery tickets 🎟️', 'superhero capes 🦸‍♂️']
            for i in range(5):  # Five varied and humorous potions
                selected_rune = random.choice(runes)
                meaning = rune_meanings.get(selected_rune, "mysterious powers 🔮")
                selected_aspect = random.choice(aspects)
                selected_crystal = random.choice(recommended_crystals) if recommended_crystals else "Moonstone 🌙"
                selected_attraction = random.choice(attractions)
                potion = f"To supercharge your {selected_aspect}, brew a potion with essence of {selected_rune} ({meaning}), a dash of {selected_crystal}, and a sprinkle of fairy dust – results in an aura so dazzling it attracts {selected_attraction} (metaphorically, or who knows?!) 🧪💥😂"
                st.write(potion)
        else:
            st.write("Enter a name to get potion recipes! 📛🧪")
        
        # What if simulator 🔄
        st.subheader("What If Simulator 🔮⏳")
        delta_minutes = st.slider("Change birth time by minutes ⏱️", -1440, 1440, 0)
        original_datetime = birth_datetime
        new_datetime = original_datetime + timedelta(minutes=delta_minutes)
        new_date = new_datetime.date()
        new_element = get_zodiac_element(new_date)
        new_moon_phase = get_moon_phase(new_datetime)
        direction = "later" if delta_minutes > 0 else "earlier"
        abs_delta = abs(delta_minutes)
        narrative = f"Born {abs_delta} minutes {direction}? You'd have a {new_element} element aura with {new_moon_phase}, making you a shadowy enigma, perfect for midnight rituals! 🌑🔮"
        st.write(narrative)
        
        # Simulate earth energy 🌍
        earth_energy = "balanced ⚖️"
        if latitude > 66:
            earth_energy = "arctic chill – adds a cool blue tint ❄️"
        elif latitude < -66:
            earth_energy = "antarctic freeze – adds an icy white tint 🧊"
        elif latitude > 0:
            earth_energy = "northern vigor – boosts energy ⚡"
        else:
            earth_energy = "southern calm – enhances peace ☮️"
        st.write(f"Earth energy from location: {earth_energy} 🌏")
    
    else:
        st.write("Please fill in your name and birth date to begin. 📝✨")

# Note: If Matplotlib errors occur in Streamlit, set backend to TkAgg in ~/.matplotlib/matplotlibrc
