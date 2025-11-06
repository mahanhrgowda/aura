import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime, timedelta
from io import BytesIO
import random

# Zodiac element calculation
def get_zodiac_element(birth_date):
    month = birth_date.month
    day = birth_date.day
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Fire'  # Aries
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Earth'  # Taurus
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Air'  # Gemini
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Water'  # Cancer
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Fire'  # Leo
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Earth'  # Virgo
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Air'  # Libra
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Water'  # Scorpio
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Fire'  # Sagittarius
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Earth'  # Capricorn
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Air'  # Aquarius
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Water'  # Pisces

# Element colors
element_colors = {
    'Fire': 'red',
    'Earth': 'green',
    'Air': 'yellow',
    'Water': 'blue'
}

# Rune mappings (letter to rune name)
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

# Rune meanings
rune_meanings = {
    'Fehu': 'Cattle, prosperity, gain of some sort, fulfilment',
    'Uruz': 'Wild ox, strength, life force, determination',
    'Thurisaz': 'Giants, Thor, brutal force, unexpected change',
    'Ansuz': 'Mouth, Odin, communication, transmission of knowledge',
    'Raido': 'Wagon, travel, movement, introspective journey',
    'Kaunaz': 'Fire, warmth, energy, power, positive attitude',
    'Gebo': 'Gift, fortuitous outcome, partnership, commitment',
    'Wunjo': 'Joy, success, lasting emotional happiness',
    'Hagalaz': 'Hail, limitations, delays, forces outside your control, disruption',
    'Nauthiz': 'Patience, passing through a difficult learning situation, hardship, need',
    'Isa': 'Ice, plans on hold, frustrations',
    'Jera': 'Harvest, reaping of rewards for past efforts, justice',
    'Eihwaz': 'Yew, Yggdrassil, endurance, ability to achieve goals with resilience',
    'Pertho': 'Mystery, occult knowledge, randomness, coincidence, secrets uncovered',
    'Algiz': 'Elk, protection, support, wisdom of the Universe',
    'Sowulo': 'Sun, victory, awareness, energy',
    'Teiwaz': 'Tyr, success in a competition, warrior strength',
    'Berkana': 'Birth, new beginnings, fertility, true home',
    'Ehwaz': 'Horse, movement, steady progress, physical shift',
    'Mannaz': 'Humankind, interdependence, collective potential',
    'Laguz': 'Water, evolution, cleansing, female figure',
    'Ingwaz': 'Successful conclusion, relief, personal development',
    'Othala': 'Heritage, possessions, ancestral wisdom, home',
    'Dagaz': 'Day, increase, steady growth, awakening'
}

# Some predefined colors for runes (arbitrary assignments based on themes)
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

# Function to create gradient image
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

# App
st.title("Aura Alchemy Simulator")

st.write("Enter your details to simulate your aura transformation!")

name = st.text_input("Your Name")
birth_date = st.date_input("Birth Date")
birth_time = st.time_input("Birth Time")
latitude = st.number_input("Birth Latitude (e.g., 37.77 for San Francisco)", -90.0, 90.0, 0.0)
longitude = st.number_input("Birth Longitude (e.g., -122.41 for San Francisco)", -180.0, 180.0, 0.0)

if name and birth_date:
    # Compute element
    element = get_zodiac_element(birth_date)
    base_color = element_colors.get(element, 'gray')
    
    # Transmute name to runes
    runes = [runes_map.get(letter.lower(), 'Ansuz') for letter in name if letter.isalpha()]  # Default to Ansuz if missing
    
    # Get rune colors
    mix_colors = [rune_colors.get(rune, 'black') for rune in runes]
    
    # All colors for gradient: base + mixes
    all_colors = [base_color] + mix_colors
    
    # Display aura
    st.subheader("Your Aura Visualization")
    gradient_img = create_gradient(all_colors)
    st.image(gradient_img, caption="Your alchemical aura gradient")
    
    # Humorous potion recipe
    st.subheader("Potion Recipe")
    if runes:
        selected_rune = random.choice(runes)
        meaning = rune_meanings.get(selected_rune, "mysterious powers")
        potion = f"To boost your love life, mix lavender essence with the essence of {selected_rune} ({meaning}) – results in a sparkling pink aura that attracts unicorns (metaphorically)."
        st.write(potion)
    else:
        st.write("Enter a name to get a potion recipe!")
    
    # What if simulator
    st.subheader("What If Simulator")
    delta_minutes = st.slider("Change birth time by minutes", -1440, 1440, 0)
    original_datetime = datetime.combine(birth_date, birth_time)
    new_datetime = original_datetime + timedelta(minutes=delta_minutes)
    new_date = new_datetime.date()
    new_element = get_zodiac_element(new_date)
    direction = "later" if delta_minutes > 0 else "earlier"
    abs_delta = abs(delta_minutes)
    narrative = f"Born {abs_delta} minutes {direction}? You'd have a {new_element} element aura, making you a shadowy enigma, perfect for midnight rituals!"
    st.write(narrative)
    
    # Simulate earth energy (simple based on latitude)
    earth_energy = "balanced"
    if latitude > 66:
        earth_energy = "arctic chill – adds a cool blue tint"
    elif latitude < -66:
        earth_energy = "antarctic freeze – adds an icy white tint"
    elif latitude > 0:
        earth_energy = "northern vigor – boosts energy"
    else:
        earth_energy = "southern calm – enhances peace"
    st.write(f"Earth energy from location: {earth_energy}")

else:
    st.write("Please fill in your name and birth date to begin.")
